from selenium.common.exceptions import NoSuchElementException


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_is_present_form(browser):
    browser.get(link)
    try:
        add_button = browser.find_element_by_css_selector("button.btn.btn-add-to-basket[type='submit']")
    except NoSuchElementException:
        add_button = False
    finally:
        assert add_button, "Cant find 'Add to Basket' button."