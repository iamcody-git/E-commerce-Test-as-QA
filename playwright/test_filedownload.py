import os
from playwright.sync_api import Page, expect


def test_verify_download(page: Page):
    page.goto("https://practice-automation.com/file-download/")

    with page.expect_download() as download_info:
        page.get_by_role("link", name="Download", exact=True).first.click()

    download = download_info.value  
    download_path = os.path.join(os.getcwd(), download.suggested_filename)
    download.save_as(download_path)

    file_name_only, file_extension = os.path.splitext(download.suggested_filename)

    expected_name = "test.pdf"
    assert download.suggested_filename == expected_name, (
        f"Expected filename '{expected_name}', got '{download.suggested_filename}'"
    )
    assert file_extension == ".pdf"
    assert os.path.exists(download_path), "Downloaded file not found on disk"
    assert os.path.getsize(download_path) > 0, "Downloaded file is empty"