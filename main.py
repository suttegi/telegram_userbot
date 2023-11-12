import openai
# from openai import OpenAI
import os
from pyrogram import Client, filters

with open("config.txt", "r") as file:
    config = file.read()

exec(config)

app = Client("my_bot", api_id=api_id, api_hash=api_hash)

# client = OpenAI(api_key=openai.api_key)




@app.on_message(filters.private)
def handle_message(client, message):

    user_input = message.text
    prompt = f'я буду ввести с тобой диалог, пиши неформально как в переписке, с маленькой буквы, пиши очень коротко. я твой собеседник, сообщение которое будет написано после точки, мое тебе сообщение которое пришло тебе в соц. сети, будь заинтересован в разговоре со мной.' + user_input
    response = openai.ChatCompletion.create(
        model=os.environ.get('OPENAI_MODEL', 'gpt-3.5-turbo'),
        messages=[{"role": "user", "content": prompt}],
        temperature=1.0,
        max_tokens=50,  
    )
    bot_reply = response["choices"][0]["message"]["content"]
    message.reply(bot_reply)

# @app.on_message(filters.command("image"))
# def handle_image_generation(client, message):
#     # Получаем текст после команды "/image"
#     user_input = " ".join(message.command[1:])

#     # Генерируем изображение только при наличии текста
#     if user_input:
#         prompt = f'{user_input}'
#         image_response = openai.Image.create(
#             model=os.environ.get('OPENAI_MODEL', 'image-alpha-001'),
#             prompt=prompt,
#             max_tokens=50,
#             temperature=1.0
#         )
#         image_url = response.data[0].url
#         # Отправляем изображение пользователю
#         app.send_photo(message.chat.id, photo=image_url)
#     else:
#         app.send_message(message.chat.id, "Пожалуйста, укажите текст после команды /image.")


if __name__ == "__main__":
    app.run()
