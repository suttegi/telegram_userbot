import openai
# from openai import OpenAI
import os
from pyrogram import Client, filters

with open("config.txt", "r") as file:
    config = file.read()

exec(config)

app = Client("my_bot", api_id=api_id, api_hash=api_hash)






@app.on_message(filters.private)
def handle_message(client, message):

    user_input = message.text
    prompt =  user_input
    response = openai.ChatCompletion.create(
        model=os.environ.get('OPENAI_MODEL', 'gpt-3.5-turbo'),
        messages=[{"role": "user", "content": prompt}],
        temperature=1.0,
        max_tokens=50,  
    )
    bot_reply = response["choices"][0]["message"]["content"]
    message.reply(bot_reply)



if __name__ == "__main__":
    app.run()
