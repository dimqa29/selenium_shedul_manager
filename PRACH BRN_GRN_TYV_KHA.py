import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains  # Модуль для двойного нажатия клавиш
from selenium.webdriver.common.keys import Keys  # Модуль для имитации работы клавиатуры

region_brn = '/html/body/div[2]/div[2]/div/div[4]/div/div[3]/div/div[3]/div/div[2]/div/div[3]/div/div[4]/table/tbody/tr/td[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div/div[6]/div/div[3]/div/div[3]/div/div/table[10]/tbody/tr/td[1]/span/input'
region_grn = '/html/body/div[2]/div[2]/div/div[4]/div/div[3]/div/div[3]/div/div[2]/div/div[3]/div/div[4]/table/tbody/tr/td[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div/div[6]/div/div[3]/div/div[3]/div/div/table[15]/tbody/tr/td[1]/span/input'
region_kha = '/html/body/div[2]/div[2]/div/div[4]/div/div[3]/div/div[3]/div/div[2]/div/div[3]/div/div[4]/table/tbody/tr/td[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div/div[6]/div/div[3]/div/div[3]/div/div/table[16]/tbody/tr/td[1]/span/input'
region_tyv = '/html/body/div[2]/div[2]/div/div[4]/div/div[3]/div/div[3]/div/div[2]/div/div[3]/div/div[4]/table/tbody/tr/td[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div/div[6]/div/div[3]/div/div[3]/div/div/table[25]/tbody/tr/td[1]/span/input'
name = 'PRACH GRN_TYV_KHA_BRN'
mail = '****'
mw_start_schedul = '20'
mw_end_schedul = '1'
time_task_schedul = 'Jan 16, 2022 20:00:00 AM'
every_schedul = '2'
repeat_end_schedul = 'Dec 28, 2022 12:00:00 AM'
url = '********'

print('a')
s = Service(r'G:\chromedriver\chromedriver.exe')
print(s)
driver = webdriver.Chrome(service=s)
print(driver)
driver.get(url)
driver.maximize_window()

# ввод логина
login = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-Gui-login-userNameTextBox')))
login.send_keys('dnikitin')

# ввод пароля
password = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-Gui-login-passwordTextBox')))
password.send_keys('****')
time.sleep(1)

# вход
vhod = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-logInButton')))
vhod.click()
time.sleep(5)

# вкладка Configure
Configure = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-GUI-Tab-Configure')))
Configure.click()
time.sleep(5)

# выбор модуля
prach = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-templateList > div:nth-child(4) > div > div:nth-child(3) > div > div > div > table:nth-child(1) > tbody > tr:nth-child(2) > td > div > div > div:nth-child(1) > div:nth-child(32)')))
prach.click()
time.sleep(5)

# открыть поле кластеров
Cluster = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-GUI-SONModulesPanel-ConfigurePanel-ConfigureWizard-topologyWidget-mapConfigPanel-stackPanel-stack-child-2-headerPanel > div.GO3SYWINO.pinHeaderContent')))
Cluster.click()
time.sleep(5)

# Выбор региона
reg = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, region_brn)))
reg.click()
time.sleep(1)
reg = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, region_grn)))
reg.click()
time.sleep(1)
reg = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, region_kha)))
reg.click()
time.sleep(1)
reg = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, region_tyv)))
reg.click()
time.sleep(1)

# next
next = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-GUI-SONModulesPanel-ConfigurePanel-ConfigureWizard-nextButton')))
next.click()
time.sleep(5)

# ввод mw_start
mw_start = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-ConfigureInputsPanel-VariablesTable-row0-class\ com\.google\.gwt\.user\.client\.ui\.ListBox')))
mw_start.send_keys(mw_start_schedul)

# ввод mw_end
mw_end = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-ConfigureInputsPanel-VariablesTable-row1-class\ com\.google\.gwt\.user\.client\.ui\.ListBox')))
mw_end.send_keys(mw_end_schedul)


# ввод emeil
email = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-ConfigureInputsPanel-VariablesTable-row2-class\ com\.google\.gwt\.user\.client\.ui\.TextBox')))
email.send_keys(mail)
time.sleep(5)

# next
next = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-GUI-SONModulesPanel-ConfigurePanel-ConfigureWizard-nextButton')))
next.click()
time.sleep(1)

# next
next = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-GUI-SONModulesPanel-ConfigurePanel-ConfigureWizard-nextButton')))
next.click()
time.sleep(1)

# schedule execution
schedule_execution = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-GUI-SONModulesPanel-ConfigurePanel-ConfigureWizard-selectExecutionPanel-scheduleScript-button-input')))
schedule_execution.click()
time.sleep(2)

# next
next = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-GUI-SONModulesPanel-ConfigurePanel-ConfigureWizard-nextButton')))
next.click()
time.sleep(5)

# schedule a module
schedule_a_module = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#isc_58table > tbody > tr:nth-child(9) > td:nth-child(1) > div')))
schedule_a_module.click()
time.sleep(5)

# ввод названия таска
name_task = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-Calendar-eventDetailsPanel-eventNameTextBox')))
name_task.send_keys(name)


# ввод времени таска
time_task = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-Calendar-eventDetailsPanel-eventStartDateBox')))
time_task.clear()
time_task.send_keys(time_task_schedul)

# убрать галочку end time
end_time_click = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-Calendar-eventDetailsPanel-eventEndDateCheckBox-input')))
end_time_click.click()

# поставить галочку Repeat
end_time_click = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-Calendar-eventDetailsPanel-repeatCheckBox-input')))
end_time_click.click()

# ввод в поле Every
every = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-Calendar-eventDetailsPanel-repeatingEventPanel-periodTextBox')))
every.clear()
every.send_keys(every_schedul)

# клиск на поле Weeks
end_time_click = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-Calendar-eventDetailsPanel-repeatingEventPanel-weeksButton > div')))
end_time_click.click()

# ввод Until
repeat_end = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-Calendar-eventDetailsPanel-repeatingEventPanel-repeatEndDateBox')))
repeat_end.send_keys(repeat_end_schedul)


