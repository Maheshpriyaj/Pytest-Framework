import time

import pytest

from pageObjects.Header_Footer import Header_Footerpage
from utilities.readProperties import ReadConfig


class Test_001_Headerfooter:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @pytest.mark.regression
    def test_Aboutus(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hf = Header_Footerpage(self.driver)
        self.driver.maximize_window()

        self.hf.clickaboutus()
        act_title = self.driver.title

        if act_title == "About Us : NASBAstore, NASBAstore":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(
                r"C:/Users/maheshpriya.j/PycharmProjects/Automation_NasbaStore/Screenshots/Aboutus.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_Faq(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hf = Header_Footerpage(self.driver)
        self.driver.maximize_window()

        self.hf.clickFaq()
        act_title = self.driver.title

        if act_title == "FAQ : NASBAstore, NASBAstore":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(
                r"C:/Users/maheshpriya.j/PycharmProjects/Automation_NasbaStore/Screenshots/Aboutus.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_Refundpolicy(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hf = Header_Footerpage(self.driver)
        self.driver.maximize_window()

        self.hf.clickRefundPolicy()
        act_title = self.driver.title

        if act_title == "Refund Policy : NASBAstore, NASBAstore":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(
                r"C:/Users/maheshpriya.j/PycharmProjects/Automation_NasbaStore/Screenshots/Aboutus.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_Privacypolicy(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hf = Header_Footerpage(self.driver)
        self.driver.maximize_window()

        self.hf.clickPrivacypolicy()
        self.driver.current_window_handle
        self.driver.window_handles[0]
        chld = self.driver.window_handles[1]
        self.driver.switch_to.window(chld)


        act_title = self.driver.title
        print("title", act_title)
        if act_title == "":
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(
                r"C:/Users/maheshpriya.j/PycharmProjects/Automation_NasbaStore/Screenshots/Aboutus.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_termsandcondition(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hf = Header_Footerpage(self.driver)
        self.driver.maximize_window()

        self.hf.clicktermsandcondition()
        self.driver.current_window_handle
        self.driver.window_handles[0]
        chld = self.driver.window_handles[1]
        self.driver.switch_to.window(chld)
        act_title = self.driver.title

        if act_title == "":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(
                r"C:/Users/maheshpriya.j/PycharmProjects/Automation_NasbaStore/Screenshots/Aboutus.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_contactus(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hf = Header_Footerpage(self.driver)
        self.driver.maximize_window()

        self.hf.clickContactus()
        act_title = self.driver.title

        if act_title == "Contact Us : NASBAstore, NASBAstore":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(
                r"C:/Users/maheshpriya.j/PycharmProjects/Automation_NasbaStore/Screenshots/Aboutus.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_Advancedsearch(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hf = Header_Footerpage(self.driver)
        self.driver.maximize_window()

        self.hf.clickadvancedsearch()
        act_title = self.driver.title

        if act_title == "Advanced Search : NASBAstore, NASBAstore":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(
                r"C:/Users/maheshpriya.j/PycharmProjects/Automation_NasbaStore/Screenshots/Aboutus.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_sitemap(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hf = Header_Footerpage(self.driver)
        self.driver.maximize_window()

        self.hf.clicksitemap()
        act_title = self.driver.title

        if act_title == "Site Map : NASBAstore, NASBAstore":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(
                r"C:/Users/maheshpriya.j/PycharmProjects/Automation_NasbaStore/Screenshots/Aboutus.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_newsletter(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hf = Header_Footerpage(self.driver)
        self.driver.maximize_window()

        self.hf.clickNewsletter()
        act_title = self.driver.title

        if act_title == "Unsubscribe : NASBAstore, NASBAstore":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(
                r"C:/Users/maheshpriya.j/PycharmProjects/Automation_NasbaStore/Screenshots/Aboutus.png")
            self.driver.close()
            assert False

    def testhomehaeder(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hf = Header_Footerpage(self.driver)
        self.driver.maximize_window()

        self.hf.clickHomeHeader()

        act_title = self.driver.title

        if act_title == "NASBAstore, NASBAstore":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(r"C:/Users/maheshpriya.j/PycharmProjects/Automation_NasbaStore/Screenshots/Aboutus.png")
            self.driver.close()
            assert False


