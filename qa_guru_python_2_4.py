def open_browser(browser_name):
    printer(open_browser, browser_name, '123')


def go_to_companyname_homepage(page_url):
    printer(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    printer(find_registration_button_on_login_page, page_url, button_text, button="кнопка", another_param = '4to-to')

def printer(func, *args,**kwargs):
    print()
    print('Вызвавшая функция:', func.__name__)
    [print(arg, end='. ') for arg in args]
    [print(f"{key} - {value}", end='. ') for key, value in kwargs.items()]

open_browser('Chrome')
go_to_companyname_homepage('google.com')
find_registration_button_on_login_page('google.com', 'Подтвердить')



