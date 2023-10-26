from PIL import ImageGrab
from functools import partial
import pyautogui as pg
import time
from get_location import *

time.sleep(3)

start = time.time()  # 시작 시간 저장
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

print("코드 실행 시간 :", time.time() - start)  
