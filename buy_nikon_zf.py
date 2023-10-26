import pyperclip
import pyautogui as pg
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from get_location import *
from accept_alert import *
from card_pay import *
from find_matchOP import *

def buy_nikon_zf(device_check):

    finish = False

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    # 니콘 e샵 접속
    driver.get('https://eshop.nikon-image.co.kr/mirrorless')
    driver.maximize_window()

    # 로그인
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/a[2]/img').click()
    user_id = 'gudtjd82'
    user_pw = 'tjdgus02@@'
    elem_id = driver.find_element(By.ID, 'userid')
    pyperclip.copy(user_id)
    time.sleep(0.3)
    elem_id.click()
    time.sleep(0.2)
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

    elem_pw = driver.find_element(By.ID, 'pwd')
    pyperclip.copy(user_pw)
    elem_pw.click()
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[4]/div/form/div/div[3]').click()

    # 구매 페이지 접속
    # zf
    url = 'https://eshop.nikon-image.co.kr/product/NK0003142'
    # z6
    # url = 'https://eshop.nikon-image.co.kr/product/NK0002937'
    # z5
    # url = 'https://eshop.nikon-image.co.kr/product/NK0003111'
    # zfc
    # url = 'https://eshop.nikon-image.co.kr/product/NK0002988'

    driver.get(url)

    # 옵션 선택
    target_option_colors = list([1, 2, 3, 4])
    # 임시
    # target_option_colors[1] = '24-200'
    # target_option_colors[2] = 'body'
    # target_option_colors[3] = '24-70'
    # target_option_kit = 'kit'
    # 실제 사용
    target_option_colors[1] = 'black'
    target_option_colors[2] = 'brown'
    target_option_colors[3] = 'green'
    target_option_kit = 'se'
    matching_option = list()
    nonMatching_option = list()

    # 우선 순위(color, kit): (black, O) > (black, X) > (brown, O) > (green, O) > (brown, X) > (green, X)
    matching_option, nonMatching_option = find_matchOP(driver, target_option_colors, target_option_kit)
    
    print("-------Matching Option---------")
    for option in matching_option:
        print(option.text)
    print()
    print("-------NonMatching Option---------")
    for option in nonMatching_option:
        print(option.text)
    print()
    
    buy_click = False
    buy_button = None
    # matching_option 클릭
    i = 0
    if len(matching_option) > 0:
        for i in range(0, len(matching_option)):
            if len(matching_option) > 0:
                option = matching_option[i]
                option.click()
                driver.implicitly_wait(5)
                buy_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div[3]/div[2]/div[3]/div[3]')
                if buy_button.text == '일시품절':
                    matching_option, nonMatching_option = find_matchOP(driver, target_option_colors, target_option_kit)
                    buy_button = None
                    continue
                elif buy_button.text == '구매하기':
                    print("구매하기 클릭")
                    buy_button.click()
                    accept_alert(driver)
                    buy_click = True
                    break
                else:
                    try:
                        buy_button.click()
                        accept_alert(driver)
                        break
                    except:
                        buy_button = None
                        matching_option, nonMatching_option = find_matchOP(driver, target_option_colors, target_option_kit)
                        continue
    
    # nonMatching_option 클릭
    j = 0
    if not buy_click or len(matching_option) <= 0:
        if len(nonMatching_option) > 0:
            for j in range(0, len(nonMatching_option)):
                if len(nonMatching_option) > 0:
                    option = nonMatching_option[j]
                    option.click()
                    driver.implicitly_wait(5)
                    buy_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div[3]/div[2]/div[3]/div[3]')
                    if buy_button.text == '일시품절':
                        matching_option, nonMatching_option = find_matchOP(driver, target_option_colors, target_option_kit)
                        buy_button = None
                        continue
                    elif buy_button.text == '구매하기':
                        print("구매하기 클릭")
                        buy_button.click()
                        accept_alert(driver)
                        buy_click = True
                        break
                    else:
                        try:
                            buy_button.click()
                            accept_alert(driver)
                            break
                        except:
                            buy_button = None
                            matching_option, nonMatching_option = find_matchOP(driver, target_option_colors, target_option_kit)
                            continue
    if not buy_click:
        print("구매 가능한 option이 없습니다.")
        buy_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div[3]/div[2]/div[3]/div[3]')
        try:
            buy_button.click()
            print("구매하기 클릭")
            accept_alert(driver)
        except:
            buy_button = None
            exit("구매 가능한 option이 없습니다.")

    driver.implicitly_wait(5)
    
    # 기존 배송지 클릭
    driver.find_element(By.CSS_SELECTOR, '#cartOrderPayForm > div.order_page > div > div.pay_page > div.pay_left > div:nth-child(2) > ul:nth-child(2) > li.home_check > p:nth-child(1) > label').click()
    # 신용카드 선택
    driver.find_element(By.CSS_SELECTOR, '#cartOrderPayForm > div.order_page > div > div.pay_page > div.pay_left > div.pay_box.last_pay_box > ul > li.card > p:nth-child(1) > label').click()
    # 결제하기
    driver.find_element(By.CSS_SELECTOR, '#goSettle').click()

    # 결제창
    
    if device_check == '1': 
        ## 전체동의 -> 신한카드 선택 -> 할부선택 -> 24개월 -> 다음 1 -> 다른 결제 -> 일반결제
        time(0.3)
        pg.click(pg.locateCenterOnScreen('./images/전체동의.png', confidence=0.9, region=(915, 340, 755, 310)))
        pg.click(pg.locateCenterOnScreen('./images/신한카드.png', confidence=0.9, region=(915, 340, 755, 310)))
        pg.click(pg.locateCenterOnScreen('./images/할부선택.png', confidence=0.9, region=(915, 340, 755, 310)))
        time(0.3)
        pg.click(pg.locateCenterOnScreen('./images/24개월.png', confidence=0.9, region=(917, 1101, 103, 20)))
        pg.click(pg.locateCenterOnScreen('./images/다음_1.png', confidence=0.9, region=(1470, 714, 170, 40)))
        time(0.3)
        pg.click(pg.locateCenterOnScreen('./images/다른결제.png', confidence=0.9, region=(1080, 270, 400, 435)))
        time(0.3)
        pg.click(pg.locateCenterOnScreen('./images/일반결제.png', confidence=0.9, region=(1080, 270, 400, 435)))

        ## 카드번호 입력
        pg.click(1214, 446)
        pg.typewrite('5')
        pg.typewrite('4')
        pg.typewrite('2')
        pg.typewrite('8')

        pg.click(pg.locateCenterOnScreen('./images/number/7.png', confidence=0.9, region=(1237, 464, 128, 50)))
        time.sleep(0.3)
        pg.click(pg.locateCenterOnScreen('./images/number/9.png', confidence=0.9, region=(1237, 464, 128, 50)))
        time.sleep(0.3)
        pg.click(pg.locateCenterOnScreen('./images/number/6.png', confidence=0.9, region=(1237, 464, 128, 50)))
        time.sleep(0.3)
        pg.click(pg.locateCenterOnScreen('./images/number/7.png', confidence=0.9, region=(1237, 464, 128, 50)))
        time.sleep(0.3)

        pg.click(pg.locateCenterOnScreen('./images/number/0.png', confidence=0.9, region=(1242, 492, 222, 121)))
        time.sleep(0.3)
        pg.click(pg.locateCenterOnScreen('./images/number/3.png', confidence=0.9, region=(1242, 492, 222, 121)))
        time.sleep(0.3)
        pg.click(pg.locateCenterOnScreen('./images/number/5.png', confidence=0.9, region=(1242, 492, 222, 121)))
        time.sleep(0.3)
        pg.click(pg.locateCenterOnScreen('./images/number/0.png', confidence=0.9, region=(1242, 492, 222, 121)))
        time.sleep(0.3)

        pg.typewrite('3')
        pg.typewrite('4')
        pg.typewrite('9')
        pg.typewrite('6')

        pg.click(pg.locateCenterOnScreen('./images/number/6.png', confidence=0.9, region=(1200, 545, 223, 115)))
        pg.click(pg.locateCenterOnScreen('./images/number/4.png', confidence=0.9, region=(1200, 545, 223, 115)))
        pg.click(pg.locateCenterOnScreen('./images/number/0.png', confidence=0.9, region=(1200, 545, 223, 115)))

        # no 클릭
        pg.click(1414, 550)
        # 다음 클릭
        pg.click(1400, 677)
        # 확인 클릭 
        pg.click(1385, 537)
        # 입력창 클릭
        pg.click(1200, 542)

        # 비밀번호 입력
        pg.click(pg.locateCenterOnScreen('./images/password/d.png', confidence=0.9, region=(1080, 370, 396, 161)))
        pg.click(pg.locateCenterOnScreen('./images/password/y.png', confidence=0.9, region=(1080, 370, 396, 161)))
        pg.click(pg.locateCenterOnScreen('./images/password/d.png', confidence=0.9, region=(1080, 370, 396, 161)))
        pg.click(pg.locateCenterOnScreen('./images/password/w.png', confidence=0.9, region=(1080, 370, 396, 161)))
        pg.click(pg.locateCenterOnScreen('./images/password/n.png', confidence=0.9, region=(1080, 370, 396, 161)))
        pg.click(pg.locateCenterOnScreen('./images/password/1.png', confidence=0.9, region=(1080, 370, 396, 161)))
        pg.click(pg.locateCenterOnScreen('./images/password/1.png', confidence=0.9, region=(1080, 370, 396, 161)))
        pg.click(pg.locateCenterOnScreen('./images/password/2.png', confidence=0.9, region=(1080, 370, 396, 161)))
        pg.click(pg.locateCenterOnScreen('./images/password/4.png', confidence=0.9, region=(1080, 370, 396, 161)))
        pg.click(pg.locateCenterOnScreen('./images/password/특수문자.png', confidence=0.9, region=(1080, 370, 396, 161)))
        pg.click(pg.locateCenterOnScreen('./images/password/dollar.png', confidence=0.9, region=(1080, 370, 396, 161)))
        pg.click(pg.locateCenterOnScreen('./images/password/입력완료.png', confidence=0.9, region=(1080, 370, 396, 161)))

        # pg.click(1400, 677)
        pg.moveTo(1400, 677)

    elif device_check == '2':
        ## 전체동의 -> 신한카드 선택 -> 할부선택 -> 24개월 -> 다음 1 -> 다른 결제 -> 일반결제
        time.sleep(1)
        # 전체동의
        pg.click(880, 353)
        # 신한카드 선택
        pg.click(624, 450)
        # 할부선택 클릭
        pg.moveTo(523, 572)
        pg.leftClick()
        time.sleep(0.5)
        # 스크롤 내리기
        pg.moveTo(552, 1048)
        time.sleep(1.5)
        # 24개월 선택
        pg.click(507, 1005)
        time.sleep(0.3)
        # 다음 선택
        pg.click(1111, 727)
        time.sleep(1)

        card_pay(finish)

if __name__ == "__main__":
    device_check = input("Desktop(1) or Laptop(2)? : ")
    buy_nikon_zf(device_check)

