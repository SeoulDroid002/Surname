import pyrogram
from pyrogram import filters, Client
import nltk
from nltk.corpus import words
import re
import random
import asyncio 

# Initialize the bot
bot = Client("my_bot", session_string="BQDCoasAwZbZxkMkf7sxyaijJC9Zx0JKhY6LN_i8h8sydq6Ehmr5WyFgI5nKV5zNY4bvHu35qBUg78k5xxxJ2iftH3EFc7uXKP79-V7PCtxEPaG8GRa51FBKtsdVFnVHfqJV9ykNAqkr9oK_FdcKT_Vtci2dKo5jB_V9JXZ0Uh6QOfDH4f8Gdzf9enc2IbGnikWeoSp2TixpKNQeBFv30YXr4iQeKSQqMrzYGl7YEl_cSe00w-zP4iA9_wsqDxbYW0cCdn4G782Z6iT38KKokfolNqToBH63jVbKf1y_mEO5XWlVf_0A8TPij47TvO4csm59c_O0vogSMXFBiL25B8PmjnX6BQAAAAGUTcYsAA", workers=100, sleep_threshold=0, ipv6=True, max_concurrent_transmissions=5)

# Load the English words corpus
nltk.download('words')
english_words = set(words.words())

# Keep track of used words
used_words = set()

async def respond_to_turn(client, message):
    # Extract the starting letter, the exact length, the time limit, the number of players remaining, and the total words
    match = message.matches[0].groups()
    starting_letter = match[0]
    exact_length = int(match[1])
    time_limit = int(match[2])
    players_remaining = match[3]
    total_words = int(match[5])

    # Find a suitable English word that starts with the given letter and has exactly the exact length
    suitable_words = [word for word in english_words if word.startswith(starting_letter) and len(word) == exact_length and word not in used_words]

    # If there are no suitable words, send a message saying so
    if not suitable_words:
        await message.reply_text(f"Sorry, no English word found with length {exact_length}!")
        return

    # Choose a random suitable word
    response_word = random.choice(suitable_words)

    # Send the response
    await message.reply_text(response_word)

    # Add the word to the used words set
    used_words.add(response_word)

@bot.on_message(filters.regex("Turn: Yun Che \\(Next: .*?\\)\\nYour word must start with (\\w) and include at least (\\d+) letters\\.\\nYou have (\\d+)s to answer\\.\\nPlayers remaining: (\\d+)/(\\d+)\\nTotal words: (\\d+)"))
async def handle_message(client, message):
    await respond_to_turn(client, message)

bot.run()
