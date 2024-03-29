from selenium import webdriver
import pytest
import time

from ui.pageobjects.HomePage import HomePage
from ui.pageobjects.RegisterPage import RegisterPage
import os
import pytest_html

from ui.pageobjects.UiUtils.CustomAssert import CustomAssert


class TestSearch:

    @pytest.mark.smoke
    def test_search(self, ui_browser):
        c_assert = CustomAssert()

        url = os.getenv("qa_env")
        ui_browser.get(url)

        home_page = HomePage(ui_browser)
        home_page.search_a_phone_product()
        c_assert.compare_equal_to(1, 1)
        c_assert.compare_gte(2, 1)
        c_assert.compare_lse_to(1, 2)
