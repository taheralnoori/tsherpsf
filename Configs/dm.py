# fileName: Configs/dm.py
# copyright ©️ 2021 nabilanavab




import os




#------------------------------------------- Config Variables -------------------------------------------

class Config(object):
    
    
    # get API_ID, API_HASH values from my.telegram.org (Mandatory)
    API_ID = os.environ.get("18563373")
    API_HASH = os.environ.get("5020a93006b07645b5ce3d8ad5a0cea5")
    
    
    # add API_TOKEN from @botfather (Mandatory)
    API_TOKEN = os.environ.get("5142088093:AAHfKa0oK9LBUhttdB0AGKP-_iwF202Yow8")
    
    
    # channel id for forced Subscription with -100 (Optional)
    UPDATE_CHANNEL = os.environ.get("https://t.me/engineering_electrical9")
    
    
    # get convertAPI secret (Optional)
    CONVERT_API = os.environ.get("Lr6Xjzmwb9QyqAYe")
    
    
    # set maximum file size for preventing overload (Optional)
    MAX_FILE_SIZE = os.environ.get("12")
    
    
    # add admins Id list by space seperated (Optional)
    ADMINS = list(set(int(x) for x in os.environ.get("ADMINS", "0").split()))
    if ADMINS:
        # Bot only for admins [True/False] (Optional)
        ADMIN_ONLY = os.environ.get("mn_ja", False)
    
    
    # banned Users cant use this bot (Optional)
    BANNED_USERS = list(set(int(x) for x in os.environ.get("BANNED_USERS", "0").split()))
    if not BANNED_USERS:
        BANNED_USERS = []
    
    # thumbnail
    PDF_THUMBNAIL = "./thumbnail.jpeg"
