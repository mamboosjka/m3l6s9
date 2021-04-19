link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_is_present_form(browser):
    browser.get(link)
    add_button = browser.find_element_by_css_selector("button.btn.btn-add-to-basket[type='submit']")
    assert bool(add_button) == True, "Cant find 'Add to Basket' button."