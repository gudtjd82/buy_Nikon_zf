def accept_alert(driver):
     while True:
        try:
            alert = driver.switch_to.alert
            alert.accept()
            break
        except:
            pass