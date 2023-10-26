import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def find_matchOP(driver, target_option_colors, target_option_kit):
    matching_option = list()
    nonMatching_option = list()

    nonMatching_a = list()
    nonMatching_b = list()
    matching_color = dict()
    matching_kit = dict()


    sel_elem = driver.find_element(By.ID, 'relation_sel')
    option_elems = sel_elem.find_elements(By.TAG_NAME, 'option')
    i = 0
    for option in option_elems:
        if i == 0:
            i += 1
            continue
        if target_option_colors[1] in option.text.lower():
            if target_option_kit in option.text.lower():
                matching_kit[target_option_colors[1]] = option
                continue
            matching_color[target_option_colors[1]] = option

        elif target_option_colors[2] in option.text.lower():
            if target_option_kit in option.text.lower():
                matching_kit[target_option_colors[2]] = option
                continue
            matching_color[target_option_colors[2]] = option
            
        elif target_option_colors[3] in option.text.lower():
            if target_option_kit in option.text.lower():
                matching_kit[target_option_colors[3]] = option
                continue
            matching_color[target_option_colors[3]] = option

        elif target_option_kit in option.text.lower():
            nonMatching_a.append(option)

        else:
            nonMatching_b.append(option)

    nonMatching_option = nonMatching_a + nonMatching_b

    if target_option_colors[1] in matching_kit:
        matching_option.append(matching_kit[target_option_colors[1]])       # (black, O)
    if target_option_colors[1] in matching_color:
        matching_option.append(matching_color[target_option_colors[1]])     # (black, X)
    if target_option_colors[2] in matching_kit:
        matching_option.append(matching_kit[target_option_colors[2]])       # (brown, O)
    if target_option_colors[3] in matching_kit:
        matching_option.append(matching_kit[target_option_colors[3]])       # (green, O)
    if target_option_colors[2] in matching_color:
        matching_option.append(matching_color[target_option_colors[2]])     # (brown, X)
    if target_option_colors[3] in matching_color:
        matching_option.append(matching_color[target_option_colors[3]])     # (green, X)
    
    return matching_option, nonMatching_option