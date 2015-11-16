from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("https://app.mysms.com")
time.sleep(2)
driver.find_element_by_class_name('styledButton').click()
time.sleep(2)
driver.find_element_by_css_selector('tr>td>a').click()
number=driver.find_element_by_class_name('msisdn')
number.send_keys('9790468990')
passwd=driver.find_element_by_class_name('html5TextBox')
passwd.send_keys('pash1397')
driver.find_element_by_css_selector('div>table>tbody>tr>td>button[class="styledButton login"]').click()
time.sleep(2)
driver.get("https://app.mysms.com/#messages:BW-IRCTCi")
html=driver.page_source()

driver.find_element_by_css_selector('div>div[_key="BW-IRCTCi"]').click()
print driver.find_element_by_css_selector('div>div>div>span>span[key="91"]').text()
