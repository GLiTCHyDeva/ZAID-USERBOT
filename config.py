import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5825240844").split()))
OWNER_ID = int(getenv("OWNER_ID", "5825240844"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Zaid:qwer@cluster0.6qsekr5.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5891865426:AAGxPL-uU8gVtyg-zp0THyEmXLc3MXNh8ug")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "AQBiMZkAcmQT5djdHC5yyP124cxx4Y9hvjReBn80krvxrup8Q8VPgMvzKQMHfXSEgrxmTXHaDBH4w2j4gRzDzhk1r1ksIhiynL4UU4rhE3jXlMWK8LyqGbt_Vc1JDtkC--P33jU9EpoD2diZl_PH0oqWvzBq_WZTfKeYPieY_iuWLk9Xtd_p6I35PoBpkCDpe7ea-CKmpny4aeDQmHkXii0w5vKVhra51EeoQ_RTPDU1y0ZLJn6NhJIvrPY1Ar67zUHsztIidQgzmHCz8S_GPFxrREQ_zvG2M_8CuKFeh2PUXYeAhNonig61TyscRc9mMvYwubT6ELWiqZHV0FbBMpVDBubruAAAAAFbNh8MAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
