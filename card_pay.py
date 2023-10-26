import pyautogui as pg
import time
from get_location import *

def card_pay():
    # 다른결제 선택
    pg.click(938, 354)
    time.sleep(1)

    # 일반 결제 선택
    pg.click(803, 513)
    time.sleep(2)

    # 카드번호 입력창 클릭
    pg.click(773, 420)
    time.sleep(0.3)

    # 카드번호 입력 0 2 3 4 5 6 7 8 9
    pg.typewrite('5')
    pg.typewrite('4')
    pg.typewrite('2')
    pg.typewrite('8')

    time.sleep(0.4)
    find_7((770, 400, 267, 225))
    time.sleep(0.3)
    find_9((770, 400, 267, 225))
    time.sleep(0.3)
    find_6((770, 400, 267, 225))
    time.sleep(0.3)
    find_7((770, 400, 267, 225))

    time.sleep(1)
    find_0((770, 400, 267, 225))
    time.sleep(0.3)
    find_3((770, 400, 267, 225))
    time.sleep(0.3)
    find_5((947, 419, 85, 181))
    time.sleep(0.3)
    find_0((770, 400, 267, 225))

    time.sleep(0.5)
    pg.typewrite('3')
    pg.typewrite('4')
    pg.typewrite('9')
    pg.typewrite('6')
    time.sleep(0.3)

    # cvc번호 입력창 클링
    pg.click(770, 468)
    time.sleep(0.2)

    # cvc번호 입력
    find_6((700, 400, 340, 300))
    time.sleep(0.3)
    find_4((700, 400, 340, 300))
    time.sleep(0.3)
    find_0((700, 400, 340, 300))
    time.sleep(0.3)

    # 입력완료 클릭
    pg.click(905, 611)

    # no 클릭
    pg.click(970, 523)

    # 다음 클릭
    pg.click(937, 661)
    time.sleep(2)

    # 확인 클릭 
    pg.click(947, 523)
    time.sleep(0.4)
    
    # 공동인증서 선택
    pg.click(970, 470)

    # 다음 클릭
    pg.click(945, 659)
    time.sleep(3.5)
    # 입력창 클릭
    pg.click(770, 731)

    # 비밀번호 입력
    time.sleep(0.3)
    pg.click(get_location('./images/password/d.png', confidence=0.99, region=(527, 838, 603, 200)))
    time.sleep(0.3)
    pg.click(get_location('./images/password/y.png', confidence=0.99, region=(527, 838, 603, 200)))
    time.sleep(0.3)
    pg.click(get_location('./images/password/d.png', confidence=0.99, region=(527, 838, 603, 200)))
    time.sleep(0.3)
    pg.click(get_location('./images/password/w.png', confidence=0.99, region=(527, 838, 603, 200)))
    time.sleep(0.3)
    pg.click(get_location('./images/password/n.png', confidence=0.99, region=(527, 838, 603, 200)))
    time.sleep(0.3)
    pg.click(get_location('./images/password/1.png', confidence=0.99, region=(527, 838, 603, 200)))
    time.sleep(0.3)
    pg.click(get_location('./images/password/1.png', confidence=0.99, region=(527, 838, 603, 200)))
    time.sleep(0.3)
    pg.click(get_location('./images/password/2.png', confidence=0.99, region=(527, 838, 603, 200)))
    time.sleep(0.3)
    pg.click(get_location('./images/password/4.png', confidence=0.99, region=(527, 838, 603, 200)))
    time.sleep(0.3)
    pg.click(get_location('./images/password/].png', confidence=0.99, region=(527, 838, 603, 200)))
    time.sleep(0.3)
    # enter 클릭
    pg.click(1089, 1022)

    # 결제요청 클릭
    time.sleep(2)
    # pg.click(1110, 742)

if __name__ == "__main__":
    time.sleep(3)
    card_pay()