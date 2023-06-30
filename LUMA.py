from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
from selenium.webdriver.common.by import By
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common import alert

@pytest.mark.usefixtures('setup')
class TestLUMA:
   browser = None

   @allure.feature('Тест магазина одежды')
   @allure.story('Возврат на главную страницу')
   @allure.description('')
   def test_store1(self):
       with allure.step('открыть ссылку'):
           self.browser.get('https://magento.softwaretestingboard.com/')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Whats New'):
           self.browser.find_element(By.XPATH, '//*[@id="ui-id-3"]/span').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать на логотип LUMA'):
           self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/a/img').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

   @allure.feature('Тест магазина одежды')
   @allure.story('Добавление в корзину')
   @allure.description('')
   def test_store2(self):
       with allure.step('открыть ссылку'):
           self.browser.get('https://magento.softwaretestingboard.com/')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Woman'):
           self.browser.find_element(By.XPATH, '//*[@id="ui-id-4"]/span[2]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Hoodies & Sweatshirts'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul[1]/li[1]/a').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать флис Circe Hooded Ice Fleece'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/strong/a').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать размер XS'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-size-143-item-166"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать цвет серый'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-color-93-item-52"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('добавить в корзину нажав кнопку Add to Cart'):
           self.browser.find_element(By.XPATH, '//*[@id="product-addtocart-button"]/span').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

   @allure.feature('Тест магазина одежды')
   @allure.story('Регистрация')
   @allure.description('')
   def test_store3(self):
       Alert(self.driver).accert()
       with allure.step('открыть ссылку'):
           self.browser.get('https://magento.softwaretestingboard.com/')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку на главной странице Create an Account'):
           self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[3]/a').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('печатать имя'):
           element = driver.find_element(By.XPATH, '//*[@id="firstname"]').send_keys('dinur')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('печатать фамилию'):
           element = driver.find_element(By.XPATH, '//*[@id="lastname"]').send_keys('sabitov')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('печатать почту'):
           element = driver.find_element(By.XPATH, '//*[@id="email_address"]').send_keys('dinur12@mail.ru')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('печатать пароль'):
           element = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('5SwAN8f@348b9Gj')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('печатать повторный пароль'):
           element = driver.find_element(By.XPATH, '//*[@id="password-confirmation"]').send_keys('5SwAN8f@348b9Gj')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Create an Account'):
           self.browser.find_element(By.XPATH, '//*[@id="form-validate"]/div/div[1]/button/span').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

   @allure.feature('Тест магазина одежды')
   @allure.story('Добавление в корзину')
   @allure.description('')
   def test_store4(self):
       with allure.step('открыть ссылку'):
           self.browser.get('https://magento.softwaretestingboard.com/')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Whats New'):
           self.browser.find_element(By.XPATH, '//*[@id="ui-id-3"]/span').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Hoodies & Sweatshirts'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div/div/ul[1]/li[1]/a').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать Circe Hooded Ice Fleece'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/strong/a').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать размер XS'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-size-143-item-166"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать цвет серый'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-color-93-item-52"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Add to cart'):
           self.browser.find_element(By.XPATH, '//*[@id="product-addtocart-button"]/span').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       assert element == True

   @allure.feature('Тест магазина одежды')
   @allure.story('Покупка Men')
   @allure.description('')
   def test_store5(self):
       with allure.step('открыть ссылку'):
           self.browser.get('https://magento.softwaretestingboard.com/')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Men'):
           self.browser.find_element(By.XPATH, '//*[@id="ui-id-5"]/span[2]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Jackets'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul[1]/li[2]/a').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать Proteus Fitness Jackshirt'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/strong/a').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать размер XS'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-size-143-item-166"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать цвет черный'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-color-93-item-49"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Add to cart'):
           self.browser.find_element(By.XPATH, '//*[@id="product-addtocart-button"]/span').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       assert element == True

   @allure.feature('Тест магазина одежды')
   @allure.story('Возврат на главную страницу')
   @allure.description('')
   def test_store6(self):
       with allure.step('открыть ссылку'):
           self.browser.get('https://magento.softwaretestingboard.com/')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Whats New'):
           self.browser.find_element(By.XPATH, '//*[@id="ui-id-3"]/span').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать на логотип LUMA'):
           self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/a/img').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

   @allure.feature('Тест магазина одежды')
   @allure.story('Покупка Gear')
   @allure.description('')
   def test_store7(self):
       with allure.step('открыть ссылку'):
           self.browser.get('https://magento.softwaretestingboard.com/')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Gear'):
           self.browser.find_element(By.XPATH, '//*[@id="ui-id-6"]/span[2]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Bags'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul/li[1]/a').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать Push It Messenger Bag'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/strong/a').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Add to cart'):
           self.browser.find_element(By.XPATH, '//*[@id="product-addtocart-button"]/span').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       assert element == True

   @allure.feature('Тест магазина одежды')
   @allure.story('Покупка Sale')
   @allure.description('')
   def test_store8(self):
       with allure.step('открыть ссылку'):
           self.browser.get('https://magento.softwaretestingboard.com/')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Sale'):
           self.browser.find_element(By.XPATH, '//*[@id="ui-id-8"]/span').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Tees'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div/div/ul[1]/li[3]/a').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать Desiree Fitness Tee'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/strong/a').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать размер XS'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-size-143-item-166"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать цвет черный'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-color-93-item-49"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Add to cart'):
           self.browser.find_element(By.XPATH, '//*[@id="product-addtocart-button"]/span').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       assert element == True

   @allure.feature('Тест магазина одежды')
   @allure.story('Покупка Йога')
   @allure.description('')
   def test_store9(self):
       with allure.step('открыть ссылку'):
           self.browser.get('https://magento.softwaretestingboard.com/')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Shop New Yoga'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[2]/div[1]/a/span/span[2]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать Echo Fit Compression Short'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/strong/a').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать размер 28'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-size-143-item-171"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать цвет черный'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-color-93-item-49"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Add to cart'):
           self.browser.find_element(By.XPATH, '//*[@id="product-addtocart-button"]/span').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       assert element == True

   @allure.feature('Тест магазина одежды')
   @allure.story('Войти в аккаунт')
   @allure.description('')
   def test_store10(self):
       with allure.step('открыть ссылку'):
           self.browser.get('https://magento.softwaretestingboard.com/')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Welcome, dinur sabitov! My account'):
           self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[1]/comment()[2]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       assert element == True

   @allure.feature('Тест магазина одежды')
   @allure.story('Покупка из рекламы Shop Tees')
   @allure.description('')
   def test_store11(self):
       with allure.step('открыть ссылку'):
           self.browser.get('https://magento.softwaretestingboard.com/')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Shop Tees'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[2]/div[1]/div/a[2]/span[2]/span[2]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать Desiree Fitness Tee'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/strong/a').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать размер XS'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-size-143-item-166"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать цвет черный'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-color-93-item-49"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Add to Cart'):
           self.browser.find_element(By.XPATH, '//*[@id="product-addtocart-button"]/span').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       assert element == True

   @allure.feature('Тест магазина одежды')
   @allure.story('Покупка из рекламы Shop Perfomance')
   @allure.description('')
   def test_store12(self):
       with allure.step('открыть ссылку'):
           self.browser.get('https://magento.softwaretestingboard.com/')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Shop Perfomance'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[2]/div[1]/div/a[4]/span/span[2]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать Sybil Running Short'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/strong/a').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать размер 28'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-size-143-item-171"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать цвет purple'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-color-93-item-57"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Add to Cart'):
           self.browser.find_element(By.XPATH, '//*[@id="product-addtocart-button"]/span').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       assert element == True

   @allure.feature('Тест магазина одежды')
   @allure.story('Покупка из рекламы Shop Pants')
   @allure.description('')
   def test_store13(self):
       with allure.step('открыть ссылку'):
           self.browser.get('https://magento.softwaretestingboard.com/')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Shop Pants'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[2]/div[1]/div/a[1]/span/span[2]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать Portia Capri'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/strong/a').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать размер 28'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-size-143-item-171"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать цвет blue'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-color-93-item-50"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Add to Cart'):
           self.browser.find_element(By.XPATH, '//*[@id="product-addtocart-button"]/span').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       assert element == True

   @allure.feature('Тест магазина одежды')
   @allure.story('Изменение размера в корзине Echo Fit Compression Short')
   @allure.description('')
   def test_store14(self):
       Alert(self.driver).accert()
       with allure.step('открыть ссылку'):
           self.browser.get('https://magento.softwaretestingboard.com/')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать на иконку корзина'):
           self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div[1]/a/span[2]/span[1]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать Echo Fit Compression Short'):
           self.browser.find_element(By.XPATH, '//*[@id="mini-cart"]/li[1]/div/div/strong/a').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать размер 29'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-size-143-item-172"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать цвет blue'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-color-93-item-49"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Add to Cart'):
           self.browser.find_element(By.XPATH, '//*[@id="product-addtocart-button"]/span').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

   @allure.feature('Тест магазина одежды')
   @allure.story('Покупка из рекламы Shop Eco-Friendly')
   @allure.description('')
   def test_store15(self):
       with allure.step('открыть ссылку'):
           self.browser.get('https://magento.softwaretestingboard.com/')
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Shop Eco-Friendly'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[2]/div[1]/div/a[5]/span/span[2]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать Ana Running Short'):
           self.browser.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/strong/a').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать размер 28'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-size-143-item-171"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('выбрать цвет black'):
           self.browser.find_element(By.XPATH, '//*[@id="option-label-color-93-item-49"]').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       with allure.step('нажать кнопку Add to Cart'):
           self.browser.find_element(By.XPATH, '//*[@id="product-addtocart-button"]/span').click()
           allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       assert element == True








