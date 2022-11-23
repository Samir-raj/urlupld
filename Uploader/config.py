# MIT License

# Copyright (c) 2022 Hash Minner

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    WEBHOOK = os.environ.get("BOT_TOKEN", False)
    # get a token from @BotFather
    BOT_TOKEN = "5830014306:AAGEy_sxm8fpZ_tzvEzn96tsaaY58xgJau8"
    # The Telegram API things
    API_ID = 25117040
    API_HASH = "d1cfa64ebbb012620a69b133a2428c25"
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot

    # file /video dpwnload location
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    MEGA_EMAIL = os.environ.get("MEGA_EMAIL", "None")
    # If deploying on vps edit the above value as example := Mega_email = "Your-Mega_email-inside-inverted-commas."

    # This is not necessary! Enter your mega password only if you have a mega.nz account with pro/business features.
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD", "None")
    # If deploying on vps edit the above value as example := Mega_password = "Your-Mega_password-inside-inverted-commas."
    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 4194304000

    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    # set timeout for subprcess
    PROCESS_MAX_TIMEOUT = 3700

    LOG_CHANNEL = -1001825669290
    OWNER_ID = 5470140997
    BOT_USERNAME = "urlnupldbot"
    ADL_BOT_RQ = {}
    AUTH_USERS = 5470140997
    

