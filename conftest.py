from pathlib import Path
import shutil

import pytest

from playwright.sync_api import sync_playwright
import pytest_html


from config import BASE_URL


@pytest.fixture
def page(request):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    videos_dir = Path("videos")
    traces_dir = Path("traces")
    videos_dir.mkdir(exist_ok=True)
    traces_dir.mkdir(exist_ok=True)
    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(videos_dir),
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    page.goto(BASE_URL)
    page.wait_for_load_state("load")

    request.node.trace_path = traces_dir / f"{request.node.name}.zip"
    request.node.video_path = videos_dir / f"{request.node.name}.webm"
    yield page

    recorded_video = page.video
    context.close()
    if recorded_video:
        generated_video = Path(recorded_video.path())
        if getattr(request.node, "rep_call", None) and request.node.rep_call.passed:
            shutil.move(str(generated_video), str(request.node.video_path))
        elif generated_video.exists():
            generated_video.unlink()
    browser.close()
    p.stop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call":
        item.rep_call = report
        page = item.funcargs.get("page")

        if page:
            page.context.tracing.stop(path=str(item.trace_path))
            extras.append(pytest_html.extras.url(
                str(item.trace_path),
                name="Playwright trace",
            ))

        if report.failed and page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)
            file_name = screenshots_dir / f"{item.name}.png"
            page.screenshot(path=str(file_name))
            extras.append(pytest_html.extras.image(str(file_name)))

        report.extras = extras

    if report.when == "teardown" and getattr(item, "rep_call", None):
        if item.rep_call.passed and item.video_path.exists():
            extras.append(pytest_html.extras.url(
                str(item.video_path),
                name="Test video",
            ))
            report.extras = extras

