# everywhere-poster
SMMplanner analogue. The script make a post in VK and Facebook group, and send message in telegram bot
# How to install
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```bash
$ pip install -r requirements.txt
```
Create .env file in local folder and put there your instagram account login and password.
```text
VK-TOKEN=PUT_YOUR_VK_TOKEN
TG-TOKEN=PUT_YOUR_TG_BOT_TOKEN
VK-LOGIN=PUT_YOUR_VK_LOGIN
VK-PASS=PUT_YOUR_VK_PASSWORD
```
Run poster.py for making posts in your VK public, Facebook page and telegram chanel:
```bash
$ python3 poster.py
```
# Project Goals
The code is written for educational purposes on online-course for web-developers [DEVMAN.org](https://devman.org)
