import os

import allure


class BaseAPI:
    def __init__(self):
        self.BASE_API = os.getenv("BASE_URL")
        self.TIMEOUT = None
        self.REQUEST_PARAMS = None

        self.STATUS_CODE = None
        self.RESPONSE_DATA = None
        self.ERROR_MESSAGE = None
        self.UNAUTHORIZED_ERROR_MESSAGE = "Unauthorized"

    @allure.step("Assert response status is {status_code}")
    def assert_response_status(self, status_code):
        assert (
            self.STATUS_CODE == status_code
        ), f"Expected status code {status_code}, but got {self.STATUS_CODE}"

    @allure.step("Assert error message")
    def assert_error_message(self):
        expected_error_message = self.ERROR_MESSAGE
        actual_error_message = self.RESPONSE_DATA.detail
        assert actual_error_message == expected_error_message, (
            f"Expected error message '{expected_error_message}', "
            f"but got '{actual_error_message}'"
        )

    @allure.step("Assert items quantity")
    def assert_items_quantity(self):
        expected_items_quantity = self.REQUEST_PARAMS["size"]
        actual_items_quantity = len(self.RESPONSE_DATA.items)

        assert actual_items_quantity == expected_items_quantity, (
            f"Expected  {expected_items_quantity} items quantity, "
            f"but actual items quantity is {actual_items_quantity}"
        )

    @allure.step("Assert response data matches the expected data")
    def assert_response_data(self, expected_data, ignore_missing_fields=False):
        actual_data = self.RESPONSE_DATA.model_dump(mode="python")
        for key, value in expected_data.items():
            if ignore_missing_fields and key not in actual_data:
                continue
            assert actual_data.get(key) == value, (
                f"Expected {key} to be {value}, " f"but got {actual_data.get(key)}"
            )
