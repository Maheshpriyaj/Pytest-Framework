import time
import pytest

from pageObjects.Register import Registerpage
from utilities.readProperties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @pytest.mark.regression
    def test_register(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.rp=Registerpage(self.driver)
        self.rp.clickLogin()
        self.rp.setFirstname()
        self.rp.setLastname()
        self.rp.setStreetAddress()
        self.rp.setcity()
        self.rp.selectstate("Alabama")
        self.rp.setpost()
        self.rp.settelephone()
        email = self.rp.generate_random_email()
        print("register",email)
        self.rp.setEmail(email)
        self.rp.setpassword()
        self.rp.setconfirmpassword()
        self.rp.clicksubmit()
        time.sleep(15)
        act_title = self.rp.gettextMyaccount()
        print(act_title)

        if act_title == "My Account":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(r"C:/Users/maheshpriya.j/PycharmProjects/Automation_NasbaStore/Screenshots/register.png")
            self.driver.close()
            assert False


    @pytest.mark.regression
    def test_Login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.rp = Registerpage(self.driver)
        self.rp.clickLogin()
        self.rp.setLoginEmail(self.username)
        self.rp.setLoginpassword(self.password)
        self.rp.clicksignin()

        act_title = self.rp.gettextMyaccount()
        print(act_title)

        if act_title == "My Account":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(r"C:/Users/maheshpriya.j/PycharmProjects/Automation_NasbaStore/Screenshots/register.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_forgotpassword(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.rp = Registerpage(self.driver)
        self.rp.clickLogin()
        self.rp.clickforgotpassword()
        self.rp.setEmail(self.username)
        self.rp.clicksubmitforgot()
        self.rp.setLoginEmail(self.username)
        password = self.rp.mailpassword()
        self.rp.setLoginpassword(password)
        self.rp.clicksignin()

        act_title = self.rp.gettextMyaccount()
        print(act_title)

        if act_title == "My Account":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(r"C:/Users/maheshpriya.j/PycharmProjects/Automation_NasbaStore/Screenshots/register.png")
            self.driver.close()
            assert False


    @pytest.mark.regression
    def test_Changepassword(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.rp = Registerpage(self.driver)
        self.rp.clickLogin()
        self.rp.setLoginEmail(self.username)
        password = self.rp.mailpassword()
        self.rp.setLoginpassword(password)
        self.rp.clicksignin()
        self.rp.clickmyaccount()
        self.rp.clickchgpassword()
        self.rp.setCurrpassword(password)
        self.rp.setnewpassword()
        self.rp.setconfirmpassword()
        self.rp.clicksubmitChngpassword()

        act_title = self.rp.gettextChangepassword()
        print(act_title)

        if act_title == "Your password has been successfully updated.":  # Update the expected title to match the actual title
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(r"C:/Users/maheshpriya.j/PycharmProjects/Automation_NasbaStore/Screenshots/Login.png")
            self.driver.close()
            assert False






