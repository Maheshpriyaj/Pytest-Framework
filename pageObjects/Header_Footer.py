from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Header_Footerpage:
    About_Us_xpath ="//a[text()='About Us']"
    FAQ_xpath="//a[text()='FAQ']"
    Refund_Policy_xpath = "//a[text()='Refund Policy']"
    Privacy_Policy_xpath="//a[text()='Privacy Policy']"
    Terms_Conditions_xpath ="//a[text()='Terms and Conditions']"
    Contact_Us_xpath="//a[text()='Contact Us']"
    Advanced_Search_xpath="//a[text()='Advanced Search']"
    Site_Map_xpath ="//a[text()='Site Map']"
    Newsletter_Unsubscribe_xpath="//a[text()='Newsletter Unsubscribe']"
    Feature_Product_xpath="//img[@title=' Ad1 ']"
    CPA_Merchandise_xpath="//h1[@id='productListHeading']"
    Nasba_store_header_xpath="//div[@id='logo']//following::img[@title=' NASBA Store ']"
    Nasba_store_footer_xpath="//div[text()='Copyright © 2007 - 2023 ']//following::a[text()='NASBAstore']"
    home_header_xpath="//div[@id='navMain']/a[1]"
    home_footer_xpath="//div[@id='navSupp']//following::a[text()='Home']"
    nasba_xpath="//a[text()='NASBA']"



    def __init__(self, driver):
        self.driver = driver

    def clickaboutus(self):
        Aboutus = self.driver.find_element(By.XPATH, self.About_Us_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Aboutus)
        Aboutus.click()

    def clickFaq(self):
        FAQ = self.driver.find_element(By.XPATH, self.FAQ_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", FAQ)
        FAQ.click()

    def clickRefundPolicy(self):
        RefundPolicy = self.driver.find_element(By.XPATH, self.Refund_Policy_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", RefundPolicy)
        RefundPolicy.click()

    def clickPrivacypolicy(self):
        Privacypolicy = self.driver.find_element(By.XPATH, self.Privacy_Policy_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Privacypolicy)
        Privacypolicy.click()

    def clicktermsandcondition(self):
        Terms_Conditions = self.driver.find_element(By.XPATH, self.Terms_Conditions_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Terms_Conditions)
        Terms_Conditions.click()

    def clickContactus(self):
        Contact_us = self.driver.find_element(By.XPATH, self.Contact_Us_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Contact_us)
        Contact_us.click()

    def clickadvancedsearch(self):
        Advancedsearch = self.driver.find_element(By.XPATH, self.Advanced_Search_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Advancedsearch)
        Advancedsearch.click()

    def clicksitemap(self):
        Sitemap = self.driver.find_element(By.XPATH, self.Site_Map_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Sitemap)
        Sitemap.click()

    def clickNewsletter(self):
        Newsletter = self.driver.find_element(By.XPATH, self.Newsletter_Unsubscribe_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Newsletter)
        Newsletter.click()

    def clickFeatureproduct(self):
        Feature = self.driver.find_element(By.XPATH, self.Feature_Product_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Feature)
        Feature.click()

    def gettextfeature(self):
        feature=self.driver.find_element(By.XPATH,self.CPA_Merchandise_xpath)
        text = feature.text
        return text

    def clicknasbastoreheader(self):
        Header = self.driver.find_element(By.XPATH, self.Nasba_store_header_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Header)
        Header.click()

    def clicknasbastorefooter(self):
        Footer = self.driver.find_element(By.XPATH, self.Nasba_store_footer_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Footer)
        Footer.click()

    def clickHomeHeader(self):
        Header = self.driver.find_element(By.XPATH, self.home_header_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Header)
        Header.click()

    def clickHomeFooter(self):
        Footer = self.driver.find_element(By.XPATH, self.home_footer_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Footer)
        Footer.click()

    def clickNasba(self):
        Nasba = self.driver.find_element(By.XPATH, self.nasba_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", Nasba)
        Nasba.click()





