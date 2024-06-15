import pyrogram
from pyrogram import filters, Client
import nltk
from nltk.corpus import words
import re
import random

# Initialize the bot
bot = Client("my_bot", session_string="BQDCoasAuI0F_3jR2plLj34jzkk2RBBiufgwacvXCN6GeRDkXq2Ug3BWuFEMDZ1EDxeNIrnJSzRWqYhCuMvpaHB_RNkojRHr1kdTzmEf9wGoSluwFK6kV69n5OLGOmhNIMybSjg4lj4BDci3_iFGhYS3Bn6LtKIwCoR_OlLRIhhpRREpkZrnIQSkGbEqv4zThK40MN2AKPPy5_l8TUItRM670cleGt_dAFIfBkwGiXuvRHCcGF-APOrb0vKiR4-hf1EX0ZTv07UQfG2vxsOHfrYgBRn97si9QuLVjdSRCmmr1uOt7OzJNERmzio3LFAAdHAEJ2nprBqOexpznkJTodAJWEDLVgAAAAGmo4A-AA", workers=1, sleep_threshold=0, ipv6=True, max_concurrent_transmissions=5)

# Load the English words corpus
nltk.download('words')
english_words = set(words.words())

# Keep track of used words
used_words = set()

@bot.on_message(filters.regex("Turn: Yun Che \(Next: .*?\)\nYour word must start with (\w) and include at least (\d+) letters\.\nYou have (\d+)s to answer\.\nPlayers remaining: (\d+)/(\d+)\nTotal words: (\d+)"))
def respond_to_turn(client, message):
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
        message.reply_text(f"Sorry, no English word found with length {exact_length}!")
        return

    # Choose a random suitable word
    response_word = random.choice(suitable_words)

    # Send the response
    message.reply_text(response_word)

    # Add the word to the used words set
    used_words.add(response_word)

bot.run()
