from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
import time
import secrets
import json
import string
import os

PATH = "questions.json"


def abagpt(question):
    for sy in string.punctuation:
        question = question.replace(sy, "")

    options = []

    f = dict(json.loads(open(PATH, "r").read()))

    for bruh in f.keys():
        options.append(bruh)

    possible = []
    for op in options:
        Sop = op.split("-")

        for x in Sop:
            if x in question:
                if op not in possible:
                    possible.append(op)

    if (len(possible) > 0):
        x = f[secrets.choice(possible)]

        if len(x) > 1 and str(type(x)) == "<class 'list'>":
            return secrets.choice(x)

        else:
            return x

    else:
        return secrets.choice(f["default_message"])


def start(update, context):
    update.message.reply_text(
        "AbaGPT\n\n[+] Manager di Astri\n[+] Abati Coin CEO\n[+] Abati Security Inc\n[+] Valdelsa Allarmi CTO\n[+] Clash Royale EG PLAYER\n[+] Horses Better\n[+] Freelancer\n[+] Chicken Seller w/ Fabio Abati")


def answer(update, context):
    msg = update.message.reply_text("🧠 AbaGPT is braining 🧠")

    time.sleep(round(random.uniform(0.2, 0.9), 2))

    if random.randint(0, 100) >= 90:
        for x in range(5+1):
            msg.edit_text(f"🧠 AbaGPT is braining {'.'*x} 🧠")
            time.sleep(0.01)

    msg.edit_text(abagpt(update.message.text.lower()))


updater = Updater(os.getenv("TOKEN"))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, answer))
print("AbaGPT is listening.....")
updater.start_polling()
