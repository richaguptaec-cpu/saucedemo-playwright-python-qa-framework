import pytest
from datetime import datetime


@pytest.hookimpl(hookwrapper=True)

def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            timestamp = datetime.now().strftime(
                "%Y-%m-%d_%H-%M-%S"
            )

            screenshot_path = (
                f"reports/{item.name}_{timestamp}.png"
            )

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )