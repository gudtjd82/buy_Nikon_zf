import pyautogui as pg

def get_location(path, **kwargs):
    if 'region' in kwargs:
        new_region = tuple(i * 2 for i in kwargs['region'])
        location = pg.locateCenterOnScreen(path, confidence=kwargs['confidence'], region=new_region)
    else:
        location = pg.locateCenterOnScreen(path, confidence=kwargs['confidence'])
    if location is not None:
        x, y = location
        return (x//2, y//2)
    else:
        print("찾을 수 없음")
        return None

def find_0(num_region):
    # pg.click(get_location('./images/number/0.png', confidence=0.7, region=(943, 636, 100, 100)))
    pg.click(get_location('./images/number/0.png', confidence=0.99, region=num_region))

def find_2(num_region):
    pg.click(get_location('./images/number/2.png', confidence=0.99, region=num_region))

def find_3(num_region):
    pg.click(get_location('./images/number/3.png', confidence=0.99, region=num_region))
    
def find_4(num_region):
    pg.click(get_location('./images/number/4.png', confidence=0.99, region=num_region))

def find_5(num_region):
    pg.click(get_location('./images/number/5.png', confidence=0.8, region=num_region))

def find_6(num_region):
    pg.click(get_location('./images/number/6.png', confidence=0.99, region=num_region))

def find_7(num_region):
    pg.click(get_location('./images/number/7.png', confidence=0.99, region=num_region))

def find_8(num_region):
    pg.click(get_location('./images/number/8.png', confidence=0.99, region=num_region))

def find_9(num_region):
    pg.click(get_location('./images/number/9.png', confidence=0.99, region=num_region))

