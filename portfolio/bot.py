# import requests
# from environs import Env
# env = Env()
# env.read_env()
# def send_message(text):
#     BOT_TOKEN=env.str("BOT_TOKEN")
#     CHAT_ID=env.str("CHAT_ID")
#     PHOTO="https://www.thoughtco.com/thmb/w9h2eusNboflTm20DRXO1NL7Sbw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/a-right-hand-of-asian-skin-is-sending-letter-to-post-box-974020720-5c5f239646e0fb0001ca87ba.jpg"
#     TEXT=text
#     url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendphoto?chat_id={CHAT_ID}&photo={PHOTO}&caption={TEXT}"
#     response = requests.get(url)
# #   print(response.status_code)




import requests
from environs import Env

env = Env()
env.read_env()

def get_random_cat_image():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    if response.status_code == 200:
        cat_data = response.json()
        if len(cat_data) > 0:
            return cat_data[0]['url']
    return None

def send_message(text):
    BOT_TOKEN = env.str("BOT_TOKEN")
    CHAT_ID = env.str("CHAT_ID")
    PHOTO = get_random_cat_image()
    
    if PHOTO:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto?chat_id={CHAT_ID}&photo={PHOTO}&caption={text}"
        response = requests.get(url)
        print(response.status_code)
    else:
        print("Mushuk rasmni olishda xatolik yuz berdi")

# # Masalan, xabarni jo'natish
# send_message("Mana mushuk rasmi!")
