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
    with codecs.open('quotes.txt', 'r', 'utf_8') as text_from_file_value:
        string_text = text_from_file_value.read()
        text_for_sending_array = string_text.split("{1}")
        text_to_send_random = random.choice(text_for_sending_array)
        text_from_file_value.close()
    return text_to_send_random


def name_for_account():
    name_for_account_array = None
    with codecs.open('name.txt', 'r', 'utf_8') as name_for_account_value:
        string_name = name_for_account_value.read()
        name_for_account_array = string_name.split("{1}")
        name_for_account_random = random.choice(name_for_account_array)
        name_for_account_value.close()
    return name_for_account_random


def random_bot_number():
    num_for_bot_array = ['79309206408', '79237958848']
    random_number = random.choice(num_for_bot_array)
    return random_number

print(text_to_send())
print(name_for_account())
print(random_bot_number())


