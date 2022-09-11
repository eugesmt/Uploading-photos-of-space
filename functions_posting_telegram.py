import telegram


def send_photo_to_channel(image_path, image_name, chat_id, telegram_token):
    bot = telegram.Bot(telegram_token)
    bot.send_photo(
        chat_id=chat_id,
        photo=open(f'{image_path}/{image_name}', 'rb')
    )
