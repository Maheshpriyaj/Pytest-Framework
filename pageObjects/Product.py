from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Productpage:
    ScoreReprint_xpath = "//a[text()='NASBA Candidate Score Reprint']"
    SucessCandidate_xapth = "//a[text()='Successful Candidate Letter']"
    ScoreTransfer_xpath="//a[text()='NASBA Candidate Score Transfer']"
    Id_xpath = "//input[@id='attrib-15-0']"
    Name_xpath = "//input[@id='attrib-25-0']"
    JD_id = "attrib-20"
    can_JD_id = "attrib-57"
    Dob_xpath = "//input[@id='attrib-14-0']"
    AUD_xpath = "//input[@id='attrib-27-0']"
    BEC_xpath = "//input[@id='attrib-28-0']"
    FAR_xpath = "//input[@id='attrib-29-0']"
    REG_xpath = "//input[@id='attrib-30-0']"
    Quantity_xpath = "//div[@id='cartAdd']//following::input[@name='cart_quantity']"
    Addtocart_xpath = "//input[@title=' Add to Cart ']"
    title_xpath = "//h1[@id='checkoutSuccessHeading']"
    Checkout_xpath = "//img[@alt='Checkout']"
    continue_xpath = "//input[@title=' Continue ']"
    payment_continue_xpath = "//input[@title=' Continue ']"
    firstname_xpath = "//input[@id='firstName']"
    lastname_xpath = "//input[@id='lastName']"
    cardno_xpath = "//input[@id='cardNumber']"
    cvv_xapth = "//input[@id='cardCode']"
    dd_id = "expirationMonth"
    mm_id = "expirationYear"
    Submit_xpath = "//button[text()='Submit']"
    from_JD_id="attrib-fs-39"
    to_JD_id="attrib-40"

    def __init__(self, driver):
        self.driver = driver

    def clickscoreprint(self):
        Scoreprint = self.driver.find_element(By.XPATH, self.ScoreReprint_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Scoreprint)
        Scoreprint.click()

    def clicksucesscandidate(self):
        sucesscandidate = self.driver.find_element(By.XPATH, self.SucessCandidate_xapth)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", sucesscandidate)
        sucesscandidate.click()

    def clicksoretransfer(self):
        ScoreTransfer = self.driver.find_element(By.XPATH, self.ScoreTransfer_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ScoreTransfer)
        ScoreTransfer.click()


    def setId(self):
        self.driver.find_element(By.XPATH, self.Id_xpath).clear()
        self.driver.find_element(By.XPATH, self.Id_xpath).send_keys("678543")

    def setName(self):
        self.driver.find_element(By.XPATH, self.Name_xpath).clear()
        self.driver.find_element(By.XPATH, self.Name_xpath).send_keys("Automation")

    def setDOB(self):
        self.driver.find_element(By.XPATH, self.Dob_xpath).clear()
        self.driver.find_element(By.XPATH, self.Dob_xpath).send_keys("03/03/2002")

    def selectJD(self, JD_name):
        state_dropdown = Select(self.driver.find_element(By.ID, self.JD_id))
        state_dropdown.select_by_visible_text(JD_name)

    def selectcanJD(self, JD_name):
        state_dropdown = Select(self.driver.find_element(By.ID, self.can_JD_id))
        state_dropdown.select_by_visible_text(JD_name)

    def setAUD(self):
        self.driver.find_element(By.XPATH, self.AUD_xpath).clear()
        self.driver.find_element(By.XPATH, self.AUD_xpath).send_keys("03/03/1997")

    def setBEC(self):
        self.driver.find_element(By.XPATH, self.BEC_xpath).clear()
        self.driver.find_element(By.XPATH, self.BEC_xpath).send_keys("03/03/1997")

    def setFAR(self):
        self.driver.find_element(By.XPATH, self.FAR_xpath).clear()
        self.driver.find_element(By.XPATH, self.FAR_xpath).send_keys("03/03/1997")

    def setREG(self):
        self.driver.find_element(By.XPATH, self.REG_xpath).clear()
        self.driver.find_element(By.XPATH, self.REG_xpath).send_keys("03/03/1997")

    def setquantity(self):
        self.driver.find_element(By.XPATH, self.Quantity_xpath).clear()
        self.driver.find_element(By.XPATH, self.Quantity_xpath).send_keys("2")

    def clickaddtocart(self):
        Addtocart = self.driver.find_element(By.XPATH, self.Addtocart_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Addtocart)
        Addtocart.click()

    def gettexttitle(self):
        title = self.driver.find_element(By.XPATH, self.title_xpath)
        text = title.text
        return text

    def clickcheckout(self):
        Checkout = self.driver.find_element(By.XPATH, self.Checkout_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Checkout)
        Checkout.click()

    def clickcontinue(self):
        Continue = self.driver.find_element(By.XPATH, self.continue_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Continue)
        Continue.click()

    def clickpaymentcontinue(self):
        Payment_continue = self.driver.find_element(By.XPATH, self.payment_continue_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Payment_continue)
        Payment_continue.click()

    def setpaymentfn(self):
        self.driver.find_element(By.XPATH, self.firstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.firstname_xpath).send_keys("test")

    def setpaymentln(self):
        self.driver.find_element(By.XPATH, self.lastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.lastname_xpath).send_keys("test")

    def setpaymentcardno(self):
        self.driver.find_element(By.XPATH, self.cardno_xpath).clear()
        self.driver.find_element(By.XPATH, self.cardno_xpath).send_keys("4716957358235925")

    def setpaymentcvv(self):
        self.driver.find_element(By.XPATH, self.cvv_xapth).clear()
        self.driver.find_element(By.XPATH, self.cvv_xapth).send_keys("720")

    def selectJD(self, JD_name):
        state_dropdown = Select(self.driver.find_element(By.ID, self.JD_id))
        state_dropdown.select_by_visible_text(JD_name)

    def selectDD(self, DD):
        option = Select(self.driver.find_element(By.ID, self.dd_id))
        option.select_by_value(DD)

    def selectMM(self, MM):
        option1 = Select(self.driver.find_element(By.ID, self.mm_id))
        option1.select_by_value(MM)

    def clicksubmit(self):
        Submit = self.driver.find_element(By.XPATH, self.Submit_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Submit)
        Submit.click()

    def selectfromJD(self, JD):
        option = Select(self.driver.find_element(By.ID, self.from_JD_id))
        option.select_by_visible_text(JD)

    def selecttoJD(self, JD):
        option1 = Select(self.driver.find_element(By.ID, self.to_JD_id))
        option1.select_by_visible_text(JD)

