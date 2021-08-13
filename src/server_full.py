import pymysql
import time
import pyautogui
import os
import yaml
import sys
import re
import uuid
import shutil
import glob
import random
import codecs


# ============CONFIG=============================================
def random_bot_number():
    num_for_bot_array = ['79309206408', '79237958848', '37369309940']
    random_number = random.choice(num_for_bot_array)
    return random_number


def has_russian(text):
    return bool(re.search('[\u0400-\u04FF]', text))


def text_to_send():
    text_for_sending_array = None
    with codecs.open('quotes.txt', 'r', 'utf_8') as text_from_file_value:
        string_text = text_from_file_value.read()
        text_for_sending_array = string_text.split("{1}")
        text_to_send_random = random.choice(text_for_sending_array)
        text_from_file_value.close()
    return text_to_send_random


def text_to_send_ru():
    ext_for_sending_array = None
    with codecs.open('name_ru.txt', 'r', 'utf_8') as text_from_file_value:
        string_text = text_from_file_value.read()
        text_for_sending_array = string_text.split("{1}")
        text_to_send_random = random.choice(text_for_sending_array)
        text_from_file_value.close()
    return text_to_send_random


def text_to_send_bot():
    text_for_sending_bot_array = None
    with codecs.open('raspuns.txt', 'r', 'utf_8') as text_from_bot_file_value:
        string_text_bot = text_from_bot_file_value.read()
        text_for_sending_bot_array = string_text_bot.split("{1}")
        text_to_bot_send_random = random.choice(text_for_sending_bot_array)
        text_from_bot_file_value.close()
    return text_to_bot_send_random


def name_for_account():
    name_for_account_array = None
    with codecs.open('name.txt', 'r', 'utf_8') as name_for_account_value:
        string_name = name_for_account_value.read()
        name_for_account_array = string_name.split("{1}")
        name_for_account_random = random.choice(name_for_account_array)
        name_for_account_value.close()
    return name_for_account_random

# RANDOM TIME RANGE FOR SEND MESSAGE


def random_sleep():
    time_range = random.uniform(0.5, 2.5)
    return time_range


t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
# CURRENT SCRIPT PATH
script_path = os.getcwd()
# REL - PATH FOR IMAGES FOR CLICKER
rel_path = "static\\images\\viber"
# FULL - PATH FOR IMAGES FOR CLICKER
image_folder = os.path.join(script_path, rel_path)
# REL-CONFIG PATH
config_file = "config\\param.yml"
# FULL CONFIG PATH
config_dir = os.path.join(script_path, config_file)
# REL - PATH FOR IMAGE FOR CHECK IF USER EXIST
image_for_user_exists_trigger = "win_en_user_exists.png"
# REL - PATH FOR IMAGE FOR CHECK IF USER HAVEN'T VIBER
image_for_trigger1 = "win_en_btn_no_viber.png"
# REL - PATH FOR CLOSE EXTRA WINDOW
image_for_trigger2 = "win_en_btn_insta_call.png"
# REL - PATH FOR CLOSE EXTRA WINDOW
image_for_trigger3 = "win_en_btn_ERR_ group info.png"
# REL - PATH FOR CLOSE  EXTRA WINDOW
image_for_connect_trigger = "win_en_btn_no_connection.png"
image_for_change_language_trigger = "win_en_btn_check_language.png"
language_trigger = os.path.join(image_folder, image_for_change_language_trigger)
image_for_trigger_close_settings = "win_en_btn_settings.png"
trigger_close_settings = os.path.join(image_folder, image_for_trigger_close_settings)
image_for_trigger_no_micro = "win_en_btn_micro_not_found.png"
trigger_for_no_micro = os.path.join(image_folder, image_for_trigger_no_micro)
image_for_close_received_message = "win_en_btn_trigger_for_close _received_message.png"
close_received_message = os.path.join(image_folder, image_for_close_received_message)
# FULL - PATH FOR IMAGE FOR CHECK IF USER HAVEN'T VIBER
except_trigger = os.path.join(image_folder, image_for_trigger1)
# FULL - PATH FOR EXTRA WINDOW
except_trigger_call = os.path.join(image_folder, image_for_trigger2)
# FULL - PATH FOR EXTRA WINDOW
except_trigger_group_info_bug = os.path.join(image_folder, image_for_trigger3)
# FULL - PATH FOR FOR CHECK IF USER EXIST
trigger_for_user_exists = os.path.join(image_folder, image_for_user_exists_trigger)
# FULL - PATH FOR EXTRA WINDOW
restore_connection_trigger = os.path.join(image_folder, image_for_connect_trigger)

mashineIP = "192.168.55.254"
with open(config_dir) as stream:
    config = yaml.safe_load(stream)
SERVER_PORT = config['SERVER_PORT']
# end-config=============================================
# ==========================START - FUNCTIONS===========================================
# FUNC:FOR:Database Connection


def connect_db():
    connection = pymysql.connect(host="192.168.1.238", port=3306, user="spamm", passwd="123qwer456!123Qwer456!",
                                 db="spamm_db", charset="utf8")
    return connection


# FUNC:FOR:Update Database
def update_field(number, field, value):
    try:
        connection = connect_db()
        with connection:
            with connection.cursor() as cursor:
                sql = "UPDATE unifun_base SET " + str(field) + " = '" + str(value) + "' WHERE mobile_number = '" + str(
                    number) + "';"
                cursor.execute(sql)
            connection.commit()
    finally:
        pass


# FUNC:FOR:Get Number From DB for checking
def get_number():
    try:
        connection = connect_db()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT mobile_number FROM unifun_base WHERE check_full IS NULL  and result_full_spamm IS NULL LIMIT 1;"
                cursor.execute(sql)
                number = cursor.fetchone()
                return number

    finally:
        pass

# =========FUNC:FOR:CHANGE PHOTO NAME FOR SENDING======================================


def change_photo_name():
    filename = time.strftime("%H_M_%S", t)
    rel_path_src = "static\\images\\viber.png"
    rel_path_dst = "static\\images\\temp\\viber.png"
    rel_path_renamed = "static\\images\\temp\\img-" + filename + ".png"
    shutil.copyfile(rel_path_src, rel_path_dst)
    os.rename(rel_path_dst, rel_path_renamed)

# ===========FUNC:FOR:CLEAN - FOLDER - AFTER - SENDING FOR CLEAN SPACE============


def clean_temp_folder():
    rel_path_dst = "static\\images\\temp\\*.png"
    image_folder_dst = os.path.join(script_path, rel_path_dst)
    files = glob.glob(image_folder_dst)
    for file in files:
        os.remove(file)

# =============  FUNC:FOR:VERIFY ANSWER FROM CLICKER AND UPDATE INFO IN DB==================


def check_number(number, name):
    if name == "Dont have viber":
        update_field(number, 'result_full_spamm', str(name))
        update_field(number, 'check_full', "number_is_processed")
    else:

        update_field(number, 'result_full_spamm', str(remove_special_chars(name)))
        update_field(number, 'check_full', "number_is_processed")

#  =====================FUNC:FOR:WRITE TO FILE ANSWER FROM CLICKER=====================


def write_to_file(number, name):
    with open('target.txt', 'w', encoding='utf-8') as f_out:
        f_out.write(str(number) + " ; " + str(name))


def remove_special_chars(name):
    name = name.encode('ascii', 'ignore').decode('ascii')
    name = re.sub('[^A-Za-z0-9]+', '', name)
    return name
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


def trigger_events():
    if pyautogui.locateOnScreen(trigger_close_settings, confidence=.9, grayscale=True):
        click_by_image("btn_close_settings", "en", "win")
    if pyautogui.locateOnScreen(trigger_for_no_micro, confidence=.9, grayscale=True):
        click_by_image("btn_close_call", "en", "win")
    if pyautogui.locateOnScreen(except_trigger_group_info_bug, confidence=.9, grayscale=True):
        click_by_image("btn_close_media", "en", "win")
        time.sleep(random_sleep())
    if pyautogui.locateOnScreen(except_trigger_call, confidence=.9, grayscale=True):
        click_by_image("btn_close_call", "en", "win")
        time.sleep(random_sleep())
        click_by_image("btn_close_buy_credit", "en", "win")
        time.sleep(random_sleep())
    if pyautogui.locateOnScreen(restore_connection_trigger, confidence=.9, grayscale=True):
        click_by_image("btn_restore_connection", "en", "win")
    if pyautogui.locateOnScreen(language_trigger, confidence=.9, grayscale=True):
        pyautogui.hotkey('shiftleft', 'altleft')

# =================MAIN CLICKER FUNCTIONALL=================================


def viber_user_checker(mobile_number):
    message = "Don't have viber"
    if len(mobile_number) == 11:
        trigger_events()
        if click_by_image("btn_tree_points", "en", "win"):
            change_account_name = name_for_account()
            print(change_account_name)
            verify_received_text = has_russian(change_account_name)
            if verify_received_text == True:
                pyautogui.hotkey('shiftleft', 'altleft')
                change_account_name = text_to_send_ru()
            click_by_image("btn_edit_name", "en", "win")
            time.sleep(random_sleep())
            pyautogui.press('backspace')
            pyautogui.write(change_account_name, interval=0.05)
            time.sleep(random_sleep())
            click_by_image("btn_edit_name_done", "en", "win")
            time.sleep(random_sleep())
            click_by_image("btn_dialpad", "en", "win")
            time.sleep(random_sleep())
            if click_by_image("btn_phone_dialer", "en", "win"):
                if pyautogui.locateOnScreen(language_trigger, confidence=.9, grayscale=True):
                    pyautogui.hotkey('shiftleft', 'altleft')
                time.sleep(random_sleep())
                pyautogui.typewrite(mobile_number)
                click_by_image("btn_initiate_send_message", "en", "win")
                time.sleep(random_sleep())
                # exec if number haven't viber
            if pyautogui.locateOnScreen(except_trigger, confidence=.9, grayscale=True):
                time.sleep(random_sleep())
                return message
            if pyautogui.locateOnScreen(close_received_message, confidence=.9, grayscale=True):
                click_by_image("btn_trigger_lose _received_message", "en", "win")
            # trigger for user info # exec if number have viber
            if pyautogui.locateOnScreen(trigger_for_user_exists, confidence=.9, grayscale=True):
                text_for_send = text_to_send()
                if click_by_image("btn_type_message", "en", "win"):
                    pyautogui.write(text_for_send, interval=0.1)
                    click_by_image("btn_trow_message", "en", "win")
                    message = "Message_is_Send"
            if pyautogui.locateOnScreen(trigger_for_no_micro, confidence=.9, grayscale=True):
                click_by_image("btn_close_call", "en", "win")

                # click_by_image("btn_add_img", "en", "win")
                # time.sleep(0.5)
                # if click_by_image("btn_img_for_sending", "en", "win"):
                #     time.sleep(0.5)
                #     click_by_image("btn_send_img", "en", "win")



    return message


def send_message_to_bot(bot_mobile_number):
    if len(bot_mobile_number) == 11:
        trigger_events()
        if click_by_image("btn_tree_points", "en", "win"):
            change_account_name = name_for_account()
            print(change_account_name)
            verify_received_text = has_russian(change_account_name)
            if verify_received_text == True:
                pyautogui.hotkey('shiftleft', 'altleft')
                change_account_name = text_to_send_ru()
            click_by_image("btn_edit_name", "en", "win")
            pyautogui.press('backspace')
            pyautogui.typewrite(change_account_name)
            time.sleep(random_sleep())
            click_by_image("btn_edit_name_done", "en", "win")
            click_by_image("btn_dialpad", "en", "win")
            if click_by_image("btn_phone_dialer", "en", "win"):
                if pyautogui.locateOnScreen(language_trigger, confidence=.9, grayscale=True):
                    pyautogui.hotkey('shiftleft', 'altleft')
                pyautogui.typewrite(bot_mobile_number)
                click_by_image("btn_initiate_send_message", "en", "win")
                # exec if number haven't viber
            if pyautogui.locateOnScreen(except_trigger, confidence=.9, grayscale=True):
                time.sleep(0.1)
            if pyautogui.locateOnScreen(close_received_message, confidence=.9, grayscale=True):
                click_by_image("btn_trigger_lose _received_message", "en", "win")
            # trigger for user info # exec if number have viber
            if pyautogui.locateOnScreen(trigger_for_user_exists, confidence=.9, grayscale=True):
                text_for_send_bot1 = text_to_send_bot()
                if click_by_image("btn_type_message", "en", "win"):
                    pyautogui.write(text_for_send_bot1, interval=0.1)
                    click_by_image("btn_trow_message", "en", "win")
                if pyautogui.locateOnScreen(trigger_for_no_micro, confidence=.9, grayscale=True):
                    click_by_image("btn_close_call", "en", "win")

                # click_by_image("btn_add_img", "en", "win")
                # time.sleep(0.5)
                # if click_by_image("btn_img_for_sending", "en", "win"):
                #     time.sleep(0.5)
                #     click_by_image("btn_send_img", "en", "win")
                message = bot_mobile_number

                return message


# ==================================END==CLICKER====================================================
# ==================================B=R=A=I=N=======================================================

def main():
    while True:
        nr = get_number()
        if nr == None:
            print("No More Numbers By Criteria")
            exit()
        number = "".join(nr).strip()
        print(current_time + ": " + number)
        update_field(number, 'check_full', "number_is_selected")
        response = viber_user_checker(number)
        check_number(number, response)
        print(current_time + ": " + number + " >> " + response)
        time.sleep(3)
        send_message_to_bot(random_bot_number())
        trigger_events()



        

if __name__ == '__main__':
    main()
