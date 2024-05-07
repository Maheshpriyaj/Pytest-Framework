import random
import string
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Registerpage:
    Loginlink_xpath = "//*[text()='Log In']"
    First_name_xpath = "//input[@id='firstname']"
    Last_name_xpath = "//input[@id='lastname']"
    Street_Address_xpath = "//input[@id='street-address']"
    city_xpath = "//input[@id='city']"
    State_id = "stateZone"
    post_xpath = "//input[@id='postcode']"
    Telephone_xpath = "//input[@id='telephone']"
    Email_xpath = "//input[@id='email-address']"
    Password_xpath = "//input[@id='password-new']"
    Confirm_Pass_xpath = "//input[@id='password-confirm']"
    submit_button_xpath = "//*[@id='createAccountForm']/div/input"
    myAccount_xpath = "//a[text()='My Account']"
    LoginEmail_xpath="//input[@id='login-email-address']"
    LoginPassword_xpath="//input[@id='login-password']"
    signin_xpath="//*[@id='loginForm']/div[1]/input"
    Changepassword_xpath="//a[text()='Change my account password.']"
    curr_password="//input[@id='password-current']"
    new_password="//input[@id='password-new']"
    conf_password="//input[@id='password-confirm']"
    submit_chgpassword_xpath="//*[@id='accountPassword']/form/div[1]/input"
    Chgpasswordpopup_xpath="//*[text()='  Your password has been successfully updated.']"
    forgot_password_xpath="//a[text()='Forgot your password?']"
    Forgot_submit_xpath="//*[@id='passwordForgotten']/form/div[1]/input"
    new_password_xpath="//td[text()='NASBAstore - New Password']"
    Password_mail_xpath="/html/body/div[1]/div[2]/div[3]/text()"



    def __init__(self, driver):
        self.driver = driver

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.Loginlink_xpath).click()

    def setFirstname(self):
        self.driver.find_element(By.XPATH,self.First_name_xpath).clear()
        self.driver.find_element(By.XPATH,self.First_name_xpath).send_keys("test")

    def setLastname(self):
        self.driver.find_element(By.XPATH,self.Last_name_xpath).clear()
        self.driver.find_element(By.XPATH,self.Last_name_xpath).send_keys("Automation")

    def setStreetAddress(self):
        self.driver.find_element(By.XPATH,self.Street_Address_xpath).clear()
        self.driver.find_element(By.XPATH,self.Street_Address_xpath).send_keys("70 Stevens St")
    def setcity(self):
        self.driver.find_element(By.XPATH,self.city_xpath).clear()
        self.driver.find_element(By.XPATH,self.city_xpath).send_keys("Cordova")

    def selectstate(self, state_name):
        state_dropdown = Select(self.driver.find_element(By.ID, self.State_id))
        state_dropdown.select_by_visible_text(state_name)

    def setpost(self):
        self.driver.find_element(By.XPATH,self.post_xpath).clear()
        self.driver.find_element(By.XPATH,self.post_xpath).send_keys("35550")

    def settelephone(self):
        self.driver.find_element(By.XPATH,self.Telephone_xpath).clear()
        self.driver.find_element(By.XPATH,self.Telephone_xpath).send_keys("9789754400")

    def generate_random_email(self):
        domain = "@example.com"
        username_length = random.randint(5, 10)
        username = ''.join(random.choice(string.ascii_lowercase) for _ in range(username_length))
        random_email=username + domain
        return random_email

    def setEmail(self, email):
        self.driver.find_element(By.XPATH,self.Email_xpath).clear()
        self.driver.find_element(By.XPATH,self.Email_xpath).send_keys(email)

    def setpassword(self):
        self.driver.find_element(By.XPATH,self.Password_xpath).clear()
        self.driver.find_element(By.XPATH,self.Password_xpath).send_keys("Password1!")

    def setconfirmpassword(self):
        self.driver.find_element(By.XPATH,self.Confirm_Pass_xpath).clear()
        self.driver.find_element(By.XPATH,self.Confirm_Pass_xpath).send_keys("Password1!")

    def clicksubmit(self):
        Submit= self.driver.find_element(By.XPATH,self.submit_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Submit)
        Submit.click()

    def gettextMyaccount(self):
        myaccount=self.driver.find_element(By.XPATH,self.myAccount_xpath)
        text = myaccount.text
        return text

    def setLoginEmail(self,username):
        self.driver.find_element(By.XPATH,self.LoginEmail_xpath).clear()
        self.driver.find_element(By.XPATH,self.LoginEmail_xpath).send_keys(username)

    def setLoginpassword(self,password):
        self.driver.find_element(By.XPATH,self.LoginPassword_xpath).clear()
        self.driver.find_element(By.XPATH,self.LoginPassword_xpath).send_keys(password)

    def clicksignin(self):
        signin = self.driver.find_element(By.XPATH, self.signin_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", signin)
        signin.click()

    def clickmyaccount(self):
        Myaccount= self.driver.find_element(By.XPATH,self.myAccount_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Myaccount)
        Myaccount.click()

    def clickchgpassword(self):
        Changepassword= self.driver.find_element(By.XPATH,self.Changepassword_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Changepassword)
        Changepassword.click()

    def setCurrpassword(self,password):
        self.driver.find_element(By.XPATH,self.curr_password).clear()
        self.driver.find_element(By.XPATH,self.curr_password).send_keys(password)

    def setnewpassword(self):
        self.driver.find_element(By.XPATH,self.new_password).clear()
        self.driver.find_element(By.XPATH,self.new_password).send_keys("Password1!")

    def setconfirmpassword(self):
        self.driver.find_element(By.XPATH,self.conf_password).clear()
        self.driver.find_element(By.XPATH,self.conf_password).send_keys("Password1!")

    def clicksubmitChngpassword(self):
        Submit= self.driver.find_element(By.XPATH,self.submit_chgpassword_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Submit)
        Submit.click()

    def gettextChangepassword(self):
        Changepassword=self.driver.find_element(By.XPATH,self.Chgpasswordpopup_xpath)
        text = Changepassword.text
        return text

    def clickforgotpassword(self):
        self.driver.find_element(By.XPATH, self.forgot_password_xpath).click()

    def clicksubmitforgot(self):
        Submit= self.driver.find_element(By.XPATH,self.Forgot_submit_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Submit)
        Submit.click()

    def mailpassword(self):
        self.driver.execute_script("window.open('', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://mailcatcher.nasba-dev.org/")
        time.sleep(10)
        self.driver.find_element("xpath", "//td[text()='NASBAstore - New Password']").click()
        time.sleep(10)
        iframe = self.driver.find_element("xpath", "//iframe[@class='body']")
        self.driver.switch_to.frame(iframe)
        l = self.driver.find_element("xpath", "//div[contains(text(),'A new password')]")
        string = l.text
        a, b = string.split(":", 1)
        word = b.split(" ", 2)
        print(word[1])
        self.driver.switch_to.window(self.driver.window_handles[0])
        return(word[1])

