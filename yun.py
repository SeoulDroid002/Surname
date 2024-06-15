import pyrogram
from pyrogram import filters, Client
import nltk
from nltk.corpus import words
import re
import random

# Initialize the bot
bot = Client("my_bot", session_string="BQDCoasAPcy9B0mJjUNLhMFPxKmTDqtnuu9qLKrDYbPDZFSn9NKjKs9ifOUObKPqFlUcucDwjSEa-eH68wKAmrcAKROmCMNRI-N-J2zz3B7QjqMbwZP994GSKDLHcDNFVCTQItdT0tDS3Kd5su2jVv5ffWU4nVGbOUmUIRL73TBGuMUbLV532DUpYqG28Y72edRiq_FLZ7X9RkHKDZFqrP3Ar5fTLgvrWmAlTHJTZ1plhgbcsXIB4H7pTRJY7Oie3apBvddla2y3r5I-PPeW-inWwOQns6YYhpq-PbcD9YC7gOjoKBRSxASD0chtGulNnVuMsjBvtLwbP_aM5KptDm2UOFyrngAAAAGmo4A-AA", workers=1, sleep_threshold=0, ipv6=True, max_concurrent_transmissions=1)

# Load the English words corpus
nltk.download('words')
english_words = set(words.words())

# Keep track of used words
used_words = set()
@bot.on_message(filters.text)
def respond_to_turn(client, message):
    text = message.text
    lines = text.split('\n')
    if len(lines) != 5:
        return

    if not lines[0].startswith('Turn: Yun Che (Next: '):
        return

    parts = lines[1].split(' and include at least ')
    if len(parts) != 2:
        return

    starting_letter = parts[0][-1]
    exact_length = int(parts[1].split(' letters.')[0])

    parts = lines[2].split(' to answer.')
    if len(parts) != 2:
        return

    time_limit = int(parts[0].split('You have ')[1][:-1])

    parts = lines[3].split(' / ')
    if len(parts) != 2:
        return

    players_remaining = parts[0]
    total_players = parts[1]

    total_words = int(lines[4].split('Total words: ')[1])

    # Find a suitable English word that starts with the given letter and has exactly the exact length
    suitable_words = [word for word in english_words if word.startswith(starting_letter) and len(word) == exact_length and word not in used_words]

    # If there are no suitable words, send a message saying so
    if not suitable_words:
        message.reply_text(f"Sorry, no English word found with length {exact_length}!")
        return

    # Choose a random suitable word
    response_word = random.choice(suitable_words)

    # Send the response
    message.reply_text(response_word)

    # Add the word to the used words set
    used_words.add(response_word)

bot.run()
