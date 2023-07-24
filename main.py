import openai
import telebot

openai.api_key = "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"
key = "6549329577:AAEoeoqiBRjZiAITdDVn1342BLq02u0_MxA"

bot = telebot.TeleBot(key)


@bot.message_handler(commands=["start"])
def start(message):
    return bot.send_message(message.chat.id, "Привет")


@bot.message_handler(content_types=['text'])
def main(message):
    response = openai.Completion.create(
        prompt=message.text,
        engine='text-davinci-003',
        max_tokens=1000,
        temperature=0.6,
        n=1,
        stop=None,
        timeout=15
    )
    if response and response.choices:
        reply = response.choices[0].text.strip()
    else:
        reply = "Uknowned error"

    bot.send_message(message.chat.id, reply)


bot.infinity_polling()