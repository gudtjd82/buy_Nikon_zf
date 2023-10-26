from PIL import ImageGrab
from functools import partial
import pyautogui as pg
import time
from get_location import *

time.sleep(3)

start = time.time()  # 시작 시간 저장

find_0((806, 475, 214, 111))
time.sleep(0.3)
find_3((806, 475, 214, 111))
time.sleep(0.3)
find_5((948, 477, 75, 107))
time.sleep(0.3)
find_0((806, 475, 214, 111))

print("코드 실행 시간 :", time.time() - start)  
