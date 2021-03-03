from test_selenium.addressPage.main_page import MainPage


class TestAddress:
    def test_addMember(self):
        MainPage().goto_address().addMember()
