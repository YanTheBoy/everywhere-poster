from dotenv import load_dotenv
import vk_api
from telegram import Bot
import os


def make_vk_post(session):
    upload = vk_api.VkUpload(session)
    print(vk.wall.post(owner_id='-195708808',message='Rick', attachments='photo-195708808_457239017'))
    photo = upload.photo(
        'morty-1.jpg',
        album_id=272483036,
        group_id=195708808)


def make_tg_post(tg_bot):
    tg_bot.send_message(chat_id='@chaname1', text="I'm sorry Dave I'm afraid I can't do that.")
    tg_bot.send_photo(chat_id='@chaname1',
                   photo='https://sun1-18.userapi.com/aK1pXgDxTDQM4p6zVtePKHWAk30et2aYlqGNBA/6BNY0enVoj8.jpg')


if __name__ == '__main__':
    load_dotenv()

    vk_login = os.getenv('VK-LOGIN')
    vk_pass = os.getenv('VK-PASS')
    vk_session = vk_api.VkApi(vk_login, vk_pass)
    vk_session.auth()
    vk = vk_session.get_api()
    make_vk_post(vk_session)

    tg_bot_token = os.getenv('TG-TOKEN')
    bot = Bot(token=tg_bot_token)
    make_tg_post(bot)
