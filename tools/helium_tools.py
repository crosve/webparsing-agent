from smolagents import tool
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import helium



@tool
def click_top_trending_repo() -> None:
    """Clicks the top trending GitHub repository"""
    driver.get("https://github.com/trending")

    link = driver.find_element(
        By.XPATH,
        "(//article//h2//a)[1]"
    )
    href = link.get_attribute("href")
    link.click()

@tool
def safe_click(text: str) -> bool:
    """Clicks an element only if it exists and returns True if it was successful.
        Args:
            text: The text to search for
    """
    from helium import Text, click

    if not Text(text).exists():
        return False
    click(text)
    return True


@tool
def get_links_with_slash() -> int:
    """Returns the number of links whose href contains '/'"""
    links = driver.find_elements(By.XPATH, "//a[contains(@href, '/')]")
    return len(links)

@tool
def search_item_ctrl_f(text: str, nth_result: int = 1) -> str:
    """
    Searches for text on the current page via Ctrl + F and jumps to the nth occurrence.
    Args:
        text: The text to search for
        nth_result: Which occurrence to jump to (default: 1)
    """
    elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{text}')]")
    if nth_result > len(elements):
        raise Exception(f"Match n°{nth_result} not found (only {len(elements)} matches found)")
    result = f"Found {len(elements)} matches for '{text}'."
    elem = elements[nth_result - 1]
    driver.execute_script("arguments[0].scrollIntoView(true);", elem)
    result += f"Focused on element {nth_result} of {len(elements)}"
    return result

@tool
def go_back() -> None:
    """Goes back to previous page."""
    driver.back()

@tool
def close_popups() -> str:
    """
    Closes any visible modal or pop-up on the page. Use this to dismiss pop-up windows!
    This does not work on cookie consent banners.
    """
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--force-device-scale-factor=1")
chrome_options.add_argument("--window-size=1000,1350")
chrome_options.add_argument("--disable-pdf-viewer")
chrome_options.add_argument("--window-position=0,0")

# Initialize the browser
driver = helium.start_chrome(headless=False, options=chrome_options)