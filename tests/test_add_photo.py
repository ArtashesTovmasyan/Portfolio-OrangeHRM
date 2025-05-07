# tests/test_add_photo.py
import time

import allure
import pytest
from pages.employee_list_page import EmployeeListPage
from pages.personal_details_page import PersonalDetailsPage
from pages.pim_page import PimPage

@allure.feature("Employee Management")
@allure.story("Add Employee Photo")
@allure.severity(allure.severity_level.NORMAL)
def test_add_photo(login, create_employee, cleanup_employee, request):
    employee_id = create_employee
    request.node.employee_id = employee_id

    pim_page = PimPage(login)
    employee_list_page = EmployeeListPage(login)
    personal_details_page = PersonalDetailsPage(login)

    pim_page.click_employee_list()
    employee_list_page.enter_employee_id(employee_id)
    employee_list_page.click_search_button()
    employee_list_page.click_on_employee(employee_id)
    personal_details_page.click_profile_picture()
    time.sleep(5)
    # Получаем src ДО загрузки
    old_src = personal_details_page.get_preview_photo_src()

    # Загружаем файл
    personal_details_page.upload_profile_picture(
        "C:/Users/atovmasyan/PycharmProjects/old-projects/PortfolioProject/resources/profile_pic.jpg"
    )
    time.sleep(5)
    # Проверяем, что src изменился
    assert personal_details_page.is_preview_photo_changed(old_src), "src изображения не изменился, возможно файл не загружен"
    time.sleep(5)
    personal_details_page.click_save_button()
