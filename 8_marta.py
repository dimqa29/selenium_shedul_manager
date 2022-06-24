import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains  # Модуль для двойного нажатия клавиш
from selenium.webdriver.common.keys import Keys  # Модуль для имитации работы клавиатуры
from selenium.common import exceptions
import parser

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
bsc_name_dict_cros4_1 = {}
bsc_name_dict_cros4_2 = {'BSCN-PZV098,BSCN-VOL093': 'Mar 5, 2022 01:40:00 AM', 'BSCN-VOL508': 'Mar 5, 2022 02:00:00 AM'}

bsc_name_dict_cros4_final = {**bsc_name_dict_cros4_1, **bsc_name_dict_cros4_2}


bsc_name_dict_cros4_final_bu = {'BSCN-KAM070': 'Mar 8, 2022 17:40:00 AM', 'BSCN-SAH068,BSCN-MGD069': 'Mar 8, 2022 18:30:00 AM', 'BSCN-BIR067': 'Mar 8, 2022 19:00:00 AM', 'BSCN-IRK148,BSCN-IRK169,BSCN-IRK135': 'Mar 8, 2022 19:20:00 AM', 'BSCN-IRK395,BSCN-IRK484': 'Mar 8, 2022 19:40:00 AM', 'BSCN-NSK095,BSCN-NSK115,BSCN-NSK042': 'Mar 8, 2022 20:00:00 AM', 'BSCN-KEM027,BSCN-KEM028': 'Mar 8, 2022 20:10:00 AM', 'BSCN-NSK502': 'Mar 8, 2022 20:20:00 AM', 'BSCN-KEM114,BSCN-KEM121,BSCN-KEM501': 'Mar 8, 2022 20:40:00 AM', 'BSCN-TOM506,BSCN-TOM104': 'Mar 8, 2022 21:00:00 AM', 'BSCN-OMS024,BSCN-OMS075': 'Mar 8, 2022 21:20:00 AM', 'BSCN-OMS103,BSCN-OMS133': 'Mar 8, 2022 21:40:00 AM', 'BSCN-ARH040,BSCN-ARH123': 'Mar 9, 2022 00:05:00 AM', 'BSCN-KOM109': 'Mar 9, 2022 00:20:00 AM', 'BSCN-MUR125,BSCN-NOV032': 'Mar 9, 2022 00:40:00 AM', 'BSCN-KLN077,BSCN-KLN503': 'Mar 9, 2022 01:00:00 AM', 'BSCN-NOV128,BSCN-PSK083': 'Mar 9, 2022 01:20:00 AM', 'BSCN-PZV098,BSCN-VOL093': 'Mar 9, 2022 01:40:00 AM', 'BSCN-VOL508': 'Mar 9, 2022 02:00:00 AM'}


dict_bsc_na3 = {'BSCN-VLA057,BSCN-VLA105': 'Mar 5, 2022 03:40:00 AM'}
dict_bsc_na3_bu = {'BSCN-IZH054,BSCN-IZH511': 'Mar 8, 2022 23:30:00 AM', 'BSCN-KAZ146,BSCN-KAZ495': 'Mar 9, 2022 00:05:00 AM', 'BSCN-KAZ509': 'Mar '
                                                                                                                                              '9, 2022 00:20:00 AM', 'BSCN-KIR056,BSCN-KIR106': 'Mar 9, 2022 00:40:00 AM', 'BSCN-KLG055,BSCN-KLG157': 'Mar 9, 2022 01:00:00 AM', 'BSCN-KOS107': 'Mar 9, 2022 01:10:00 AM', 'BSCN-NIN102,BSCN-NIN126': 'Mar 9, 2022 01:20:00 AM', 'BSCN-NIN129,BSCN-NIN496,BSCN-NIN510': 'Mar 9, 2022 01:40:00 AM', 'BSCN-RYZ078': 'Mar 9, 2022 02:00:00 AM', 'BSCN-RYZ152': 'Mar 9, 2022 02:20:00 AM', 'BSCN-SAM387,BSCN-SAM388': 'Mar 9, 2022 02:40:00 AM', 'BSCN-SMO033': 'Mar 9, 2022 02:50:00 AM', 'BSCN-SMO116': 'Mar 9, 2022 03:00:00 AM', 'BSCN-TUL092,BSCN-TUL507': 'Mar 9, 2022 03:20:00 AM', 'BSCN-TVE061,BSCN-TVE120': 'Mar 9, 2022 03:30:00 AM', 'BSCN-VLA057,BSCN-VLA105': 'Mar 9, 2022 03:40:00 AM'}

dict_bsc_na4 = {'BSCN-BEL101': 'Mar 5, 2022 03:50:00 AM', 'BSCN-VRN119': 'Mar 5, 2022 03:00:00 AM', 'BSCN-MRD147': 'Mar 5, 2022 03:10:00 AM'}

dict_bsc_na4_bu = {'BSCN-BRY053,BSCN-BRY099,BSCN-BRY154': 'Mar 9, 2022 00:10:00 AM', 'BSCN-KRA026,BSCN-KRA038': 'Mar 9, 2022 00:30:00 AM', 'BSCN-KRA090,BSCN-KRA113': 'Mar 9, 2022 00:50:00 AM', 'BSCN-ADY081': 'Mar 9, 2022 01:10:00 AM', 'BSCN-ROS021,BSCN-ROS085': 'Mar 9, 2022 02:00:00 AM', 'BSCN-ROS086,BSCN-ROS127,BSCN-ROS117': 'Mar 9, 2022 02:20:00 AM', 'BSCN-ORL076': 'Mar 9, 2022 01:30:00 AM', 'BSCN-TAM058,BSCN-TAM505': 'Mar 9, 2022 01:40:00 AM', 'BSCN-KUR031,BSCN-KUR084': 'Mar 9, 2022 01:50:00 AM', 'BSCN-LIP072,BSCN-LIP504': 'Mar 9, 2022 02:10:00 AM', 'BSCN-VRN036,BSCN-VRN096': 'Mar 9, 2022 02:30:00 AM', 'BSCN-BEL062': 'Mar 9, 2022 02:50:00 AM', 'BSCN-BEL101': 'Mar 9, 2022 03:50:00 AM', 'BSCN-VRN119': 'Mar 9, 2022 03:00:00 AM', 'BSCN-MRD147': 'Mar 9, 2022 03:10:00 AM'}


url_cros1 = "https://*************"  # MOS
url_cros2 = 'https://*************'  # CHE PRM ORB
url_cros3 = 'https://*************'  # EKT
url_cros4 = 'https://*************'  # KEM NSK
url_cros5 = 'https://*************'
url_cros6 = 'https://*************'
url_sonLab = 'https://*************'
url = url_cros1
print('a')
s = Service(r'G:\chromedriver\chromedriver.exe')
print(s)
driver = webdriver.Chrome(service=s)
print(driver)

driver.get(url)
login_sonlab = 'testerTele2'
pass_sonlab = '*****'
login_dnikit = 'dnikitin'
pass_dnikit = '******'

driver.maximize_window()

log = login_dnikit
pas = pass_dnikit
yaer = '2022'
month = 'Mar'
day = '6'
day2 = '7'
day3 = '8'
# day4 = '3'
# day5 = '4'
day_3 = "//td[@ class='dateChooserWeekday' or @ class='dateChooserWeekend' or @ class='dateChooserWeekdaySelected']/div[contains(text(), '" + day + "')]"

spisok_dat = [[yaer,month,day], [yaer,month,day2], [yaer,month,day3]]
# name_modules = ['PCE', 'PCI', 'PRACH', 'SCReuse', 'CA_IFLB']
module_name = 'PCEmodule_TEST'
bsc_name = 'AND071'


def login_vhod (log, pas):

    login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-Gui-login-userNameTextBox')))
    # ввод логина
    login.send_keys(log)

    # ввод пароля
    password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-Gui-login-passwordTextBox')))
    password.send_keys(pas)
    time.sleep(1)

    # вход
    vhod = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-logInButton')))
    vhod.click()
    time.sleep(5)

def vibor_dati(yaer, month, day):
    # выбор даты
    vibor = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#isc_5M > img')))
    vibor.click()
    time.sleep(2)

    yaer_selection = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//td[@ class='dateChooserNavButton']/div[contains(text(), '2022')]")))
    yaer_selection.click()
    time.sleep(2)

    yaer_selection2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//td[@eventpart='showYear' and contains(text(), '"+yaer+"')]")))
    yaer_selection2.click()
    time.sleep(2)

    month_selection = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@ onfocus='isc.EH.focusInCanvas(isc_Calendar_0_dateChooser_monthChooserButton,true);']")))
    month_selection.click()
    time.sleep(2)

    month_selection2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//td[@eventpart='showMonth' and contains(text(), '"+month+"')]")))
    month_selection2.click()
    time.sleep(2)


    day_selection = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        [By.XPATH, "//td[@ class='dateChooserWeekday' or @ class='dateChooserWeekend' or @ class='dateChooserWeekdaySelected']/div[contains(text(), '" + day + "')]"]))
    day_selection.click()
    time.sleep(2)



# вкладка Configure
def selection_module(module_name):
    Configure = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-GUI-Tab-Configure')))
    Configure.click()
    time.sleep(5)

    module_selection = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-templateList-filterField')))
    # ввод имени модуля
    module_selection.send_keys(module_name)
    time.sleep(5)
    # выбор модуля
    module_selection_2 = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[1]/td/div/div/div[1]/label/b")))
    module_selection_2.click()
    time.sleep(5)

    return print("modul vibran")

def select_bsc(bsc_name):

    # выбор региона
    bsc_select = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@ class='gwt-Label GMTD3BJDBP' and contains(text(), '"+bsc_name+"')]")))
    bsc_select.click()
    time.sleep(3)
    galochka = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-GUI-SONModulesPanel-ConfigurePanel-ConfigureWizard-topologyWidget-mapConfigPanel-stackPanel-stack-child-0-button')))
    galochka.click()

    return print("bsc_vibran")

def cheduling_task(reg, times):
    # schedule a module
    time.sleep(5)
    schedule_a_module = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div[4]/div/div[3]/div/div[3]/div/div[2]/div/div[3]/div/div["
                                          "4]/table/tbody/tr/td[2]/div/div/div[2]/div[5]/div/div/div/div/div[1]/div/div/div[3]/div[1]/div[2]/div/div[2]/div[1]/table/tbody/tr[3]/td[5]/div")))
    schedule_a_module.click()
    time.sleep(5)
    # ввод названия таска
    name_task = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-Calendar-eventDetailsPanel-eventNameTextBox')))
    name_task.send_keys('8_marta_' + nazvanie_taska(reg))
    # ввод времени таска
    time_task = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-Calendar-eventDetailsPanel-eventStartDateBox')))
    time_task.clear()
    time_task.send_keys(times)
    # убрать галочку end time
    end_time_click = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#gwt-debug-Calendar-eventDetailsPanel-eventEndDateCheckBox-input')))
    end_time_click.click()
    time.sleep(2)
    # клик Schedule
    Schedule_click = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.XPATH, "// button[ @ type = 'button' and contains(text(), 'Schedule')]")))
    Schedule_click.click()
    return print("task zaveden", reg)


def nazvanie_taska(reg):
    if len(reg) > 11:
        reg = reg.replace('BSCN-', '')
        reg = reg.replace(',', '_')
    else:
        reg = reg.replace('BSCN-', '')

    return reg


login_vhod(log, pas)
selection_module(module_name)

filter = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,
                                '#gwt-debug-GUI-SONModulesPanel-ConfigurePanel-ConfigureWizard-topologyWidget-mapConfigPanel-stackPanel-stack-child-0-headerPanel > div.GMTD3BJDNO.pinHeaderContent')))
filter.click()

plusik = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,
                                '#gwt-debug-GUI-SONModulesPanel-ConfigurePanel-ConfigureWizard-topologyWidget-mapFilterPanel > div > div > div:nth-child(3) > div:nth-child(2) > table > tbody > tr > td:nth-child(1) > img')))
plusik.click()

plusik2 = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.XPATH,
                                "/html/body/div[2]/div[2]/div/div[4]/div/div[3]/div/div[3]/div/div[2]/div/div[3]/div/div[4]/table/tbody/tr/td[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div/div[2]/div/div/div/div[3]/div[2]/div/div[2]/table/tbody/tr/td[1]/img")))
plusik2.click()

plusik3 = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div[4]/div/div[3]/div/div[3]/div/div[2]/div/div[3]/div/div["
                                                 "4]/table/tbody/tr/td[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div/div[2]/div/div/div/div[3]/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[1]/img")))
plusik3.click()
time.sleep(3)


for reg, times in dict_bsc_na4.items():
    if ',' in reg:
        for k in reg.split(','):
            print(k)
            select_bsc(k)
    else:
        select_bsc(reg)
    time.sleep(5)
    next = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                      '#gwt-debug-GUI-SONModulesPanel-ConfigurePanel-ConfigureWizard-nextButton')))
    next.click()

    report_prefix = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                               '#gwt-debug-ConfigureInputsPanel-VariablesTable-row9-class\ com\.google\.gwt\.user\.client\.ui\.TextBox')))
    report_prefix.send_keys(nazvanie_taska(reg))
    next.click()
    time.sleep(2)
    next.click()
    time.sleep(2)
    schedule_execution = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#gwt-debug-GUI-SONModulesPanel-ConfigurePanel-ConfigureWizard-selectExecutionPanel-scheduleScript-button-input')))
    schedule_execution.click()
    time.sleep(2)
    next.click()
    time.sleep(5)
    cheduling_task(reg, times)
    time.sleep(10)
    cheduling_task(reg, dict_bsc_na4_bu.get(reg))
    time.sleep(10)
    finish_click = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "// button[ @ type = 'button' and contains(text(), 'Finish')]")))
    finish_click.click()
    time.sleep(5)
    click_nokia = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//div[@ class='gwt-Label GMTD3BJDBP' and contains(text(), 'Nokia')]")))
    click_nokia.click()
    click_nokia.click()

    time.sleep(3)



print("ok")
print("ok")