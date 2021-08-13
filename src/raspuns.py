import pymysql
import time
import pyautogui
import os
import win32clipboard
import yaml
import sys
import re
import random
import uuid
import shutil
import glob
import random
import codecs


# ============CONFIG=============================================
def text_to_send():
    text_for_sending_array = None
    with codecs.open('raspuns.txt', 'r', 'utf_8') as text_from_file_value:
        string_text = text_from_file_value.read()
        text_for_sending_array = string_text.split("{1}")
        text_to_send_random = random.choice(text_for_sending_array)
        text_from_file_value.close()
    return text_to_send_random


def random_sleep():
    time_range = random.uniform(2.5, 3.5)
    return time_range


t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
script_path = os.getcwd()
receive_mess = "win_en_btn_receive_message.png"
rel_path = "static\\images\\viber"
# FULL - PATH FOR IMAGES FOR CLICKER
image_folder = os.path.join(script_path, rel_path)
receive_message = os.path.join(image_folder, receive_mess)
# ==========================END - FUNCTIONS===========================================

# ==============================CLICKER=================================================
# =============FUNC:FOR: LEFT CLICK==============


def click_by_image(image_name, lang, os, confidence=.9, grayscale=True):
    i = 1
    while True:
        file_name = f'{os}_{lang}_{image_name}.png'
        path = f'{image_folder}\\{file_name}'
        location = pyautogui.locateOnScreen(path, grayscale=grayscale, confidence=confidence)
        if location:
            pyautogui.click(location)
            return True
        else:
            time.sleep(0.1)
            if i == 50:
                return False
            i += 1


# ===========FUNC:FOR: RIGHT CLICK======


def right_click_by_image(image_name, lang, os, confidence=.9, grayscale=True):
    i = 1
    while True:
        file_name = f'{os}_{lang}_{image_name}.png'
        path = f'{image_folder}\\{file_name}'
        location = pyautogui.locateOnScreen(path, grayscale=grayscale, confidence=confidence)
        if location:
            pyautogui.click(location)
            pyautogui.click(button='right')
            return True

        else:
            time.sleep(0.1)
            if i == 50:
                return False
            i += 1


# =================MAIN CLICKER FUNCTIONALL=================================


def viber_user_checker(raspuns):
    rass = 'Message :' + raspuns + 'was not send'
    if pyautogui.locateOnScreen(receive_message, confidence=.9, grayscale=True):
        time.sleep(random_sleep())
        click_by_image("btn_receive_message", "en", "win")
        if click_by_image("btn_type_message", "en", "win"):
            pyautogui.write(raspuns, interval=0.2)
            time.sleep(random_sleep())
            click_by_image("btn_trow_message", "en", "win")
            rass = 'Message :' + raspuns + 'is send'
            click_by_image("btn_change_focus", "en", "win")

            return rass

# ==================================END==CLICKER====================================================
# ==================================B=R=A=I=N=======================================================

def main():
    while True:
        response = text_to_send()
        result = viber_user_checker(response)
        time.sleep(2)
        print(result)


if __name__ == '__main__':
    main()
