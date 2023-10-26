from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re

def time_check(driver_time, hour, minute, sec):
        

    time_txt = driver_time.find_element(By.ID, 'time_area').text
    time = re.findall("[0-9]+", time_txt)
    prev_hour = time[3]
    while True:
        try:
            time_txt = driver_time.find_element(By.ID, 'time_area').text
            # msec_txt = driver_time.find_element(By.ID, 'msec_area').text
        except:
            driver_time.refresh()
            print("time_txt: ", time_txt)
        time = re.findall("[0-9]+", time_txt)
        # time[0]: 년 / time[1]: 월 / time[2]: 일 / time[3] 시 / time[4] 분 / time[5] 초
        if time[3]==hour and time[4]==minute and time[5]==sec:
            # msec = re.findall('[0-9]+', msec_txt)
            # if(int(msec[0]) >=0):
            print("On Time!")
            return
        if prev_hour != time[3]:
            driver_time.find_element(By.ID, 'buttonFight').click()
            prev_hour = time[3]
