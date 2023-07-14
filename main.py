# import asyncio
import logging
import dotenv
import json
import random
import os 

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from decider import yes_or_no
from cat import get_cat
from dog import get_dog
from beers import get_beers

env_variables = dotenv.dotenv_values(".env")
TOKEN = env_variables["TELEGRAM_API_TOKEN"]

with open("clara.json", 'r') as json_file:
    clara_messages = json.load(json_file)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Soy Clarabot, KLK con KLK?"
    )


async def yesno(update: Update, context: ContextTypes.DEFAULT_TYPE):
    yesno_response = yes_or_no()
    await context.bot.send_animation(
        chat_id=update.effective_chat.id, animation=yesno_response
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    random_message = random.choice(clara_messages)
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=random_message
    )


async def get_a_cat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cat_response = get_cat()
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=cat_response)


async def get_a_dog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dog_response = get_dog()
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=dog_response)

async def get_a_beer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    beer = get_beers()

    beer_image = beer["image"]
    beer_message = f'Nombre: {beer["name"]}\nDescripción: {beer["description"]}\nCombina bien con: {beer["food_pairing"][0]}'

    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=beer_image)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=beer_message)


async def meaning_of_life(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "Error code: *42*"
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=message, parse_mode="Markdown"
    )


if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    yesno_handler = CommandHandler("yesno", yesno)
    application.add_handler(yesno_handler)

    random_handler = CommandHandler("clara_klk", status)
    application.add_handler(random_handler)

    cat_handler = CommandHandler("misu", get_a_cat)
    application.add_handler(cat_handler)
    
    dog_handler = CommandHandler("firulais", get_a_dog)
    application.add_handler(dog_handler)

    meaning_of_life_handler = CommandHandler("sentido_de_la_vida", meaning_of_life)
    application.add_handler(meaning_of_life_handler)

    beer_handler = CommandHandler("cerveza", get_a_beer)
    application.add_handler(beer_handler)

    application.run_polling()

    # asyncio.run(main())
