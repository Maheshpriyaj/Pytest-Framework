import time
import pytest

from pageObjects.Product import Productpage
from pageObjects.Register import Registerpage
from utilities.readProperties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()


    @pytest.mark.regression
    def test_ScorePrint(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.rp = Registerpage(self.driver)
        self.rp.clickLogin()
        self.rp.setLoginEmail(self.username)
        self.rp.setLoginpassword(self.password)
        self.rp.clicksignin()

        self.pro = Productpage(self.driver)
        self.driver.maximize_window()
        self.pro.clickscoreprint()
        self.pro.setId()
        self.pro.setName()
        self.pro.selectJD("Colorado")
        self.pro.setAUD()
        self.pro.setBEC()
        self.pro.setFAR()
        self.pro.setREG()
        self.pro.setquantity()
        self.pro.clickaddtocart()
        self.pro.clickcheckout()
        self.pro.clickcontinue()
        self.pro.clickpaymentcontinue()
        self.pro.setpaymentfn()
        self.pro.setpaymentln()
        self.pro.setpaymentcardno()
        self.pro.selectDD("06")
        self.pro.selectMM("2027")
        self.pro.setpaymentcvv()
        self.pro.clicksubmit()
        time.sleep(35)

        act_title = self.pro.gettexttitle()
        print(act_title)

        if act_title == "Thank You! We Appreciate your Business!":
            self.driver.close()
            assert True
        else:

            self.driver.save_screenshot(r"C:/Users/maheshpriya.j/PycharmProjects/Automation_NasbaStore/Screenshots/register.png")
            self.driver.close()
            assert False



    @pytest.mark.regression
    def test_ScoreTransfer(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.rp = Registerpage(self.driver)
        self.rp.clickLogin()
        self.rp.setLoginEmail(self.username)
        self.rp.setLoginpassword(self.password)
        self.rp.clicksignin()

        self.pro = Productpage(self.driver)
        self.driver.maximize_window()
        self.pro.clicksoretransfer()
        self.pro.setName()
        self.pro.setDOB()

        self.pro.selectfromJD("Connecticut")
        time.sleep(5)
        self.pro.selecttoJD("Alabama")
        self.pro.setAUD()
        self.pro.setBEC()
        self.pro.setFAR()
        self.pro.setREG()
        self.pro.setquantity()
        self.pro.clickaddtocart()
        self.pro.clickcheckout()
        self.pro.clickcontinue()
        self.pro.clickpaymentcontinue()
        self.pro.setpaymentfn()
        self.pro.setpaymentln()
        self.pro.setpaymentcardno()
        self.pro.selectDD("05")
        self.pro.selectMM("2026")
        self.pro.setpaymentcvv()
        self.pro.clicksubmit()
        time.sleep(35)
        act_title = self.pro.gettexttitle()
        print(act_title)

        if act_title == "Thank You! We Appreciate your Business!":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(r"C:/Users/maheshpriya.j/PycharmProjects/Automation_NasbaStore/Screenshots/register.png")
            self.driver.close()
            assert False


    @pytest.mark.regression
    def test_Successcandidate(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.rp = Registerpage(self.driver)
        self.rp.clickLogin()
        self.rp.setLoginEmail(self.username)
        self.rp.setLoginpassword(self.password)
        self.rp.clicksignin()

        self.pro = Productpage(self.driver)
        self.driver.maximize_window()
        self.pro.clicksucesscandidate()
        self.pro.setId()
        self.pro.setName()
        self.pro.selectcanJD("Connecticut")
        self.pro.setDOB()
        self.pro.setAUD()
        self.pro.setBEC()
        self.pro.setFAR()
        self.pro.setREG()
        self.pro.setquantity()
        self.pro.clickaddtocart()
        self.pro.clickcheckout()
        self.pro.clickcontinue()
        self.pro.clickpaymentcontinue()
        self.pro.setpaymentfn()
        self.pro.setpaymentln()
        self.pro.setpaymentcardno()
        self.pro.selectDD("09")
        self.pro.selectMM("2029")
        self.pro.setpaymentcvv()
        self.pro.clicksubmit()
        time.sleep(35)
        act_title = self.pro.gettexttitle()
        print(act_title)

        if act_title == "Thank You! We Appreciate your Business!":
            self.driver.close()
            assert True
        else:

            self.driver.save_screenshot(r"C:/Users/maheshpriya.j/PycharmProjects/Automation_NasbaStore/Screenshots/register.png")
            self.driver.close()
            assert False




