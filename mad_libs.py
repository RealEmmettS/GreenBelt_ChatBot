import math
import random
from replit.ai.modelfarm import ChatExample, ChatMessage, ChatModel, ChatSession

import prompts


# Mad Libs Game Functions
#
# This file contains functions that are part of a Mad Libs game.
#
# Functions:
#   get_user_inputs(): Prompts the user for adjectives and verbs, returns a string of comma-separated words.
#
#   process_story(inputs_string): Takes a string of comma-separated words and generates a story using those words.
#
#   startGame(): Initiates the game, gets user inputs, processes the story, and displays it.
#
# Usage:
#   To play the game, simply run the startGame() function. It will guide you through the process.



def get_user_inputs():
	# Prompt the user 7 times for an adjective or verb
	user_inputs = []
	for i in range(4):
			word_type = random.choice(["adjective", "verb"])
			user_input = input(f"Please enter an {word_type}: ")
			user_inputs.append(user_input)
	return ', '.join(user_inputs)




def process_story(inputs_string):
	model = ChatModel("chat-bison")
	response = model.chat([
			ChatSession(
					context=f"You are a mad-libs story generator. Generate a funny story using the provided adjectives and verbs. Make it as entertaining and as wild as possible (but keep it safe for work). When generating a story, try and use all provided words, and ONLY RETURN THE STORY AND NOTHING ELSE; No extra commentary on your part is required.",
					examples=[
							ChatExample(
									input=ChatMessage(content="super smash bros, booted, ghost, fought, ultimate"),
									output=ChatMessage(content=prompts.ML_Prompt)
							)
					],
					messages=[
							ChatMessage(author="USER", content=f"Make a story using these adjectives and verbs: {inputs_string}"),
					],
			)
	], temperature=0.2)

	return response.responses[0].candidates[0].message.content





def startGame():
	# Start the game
	print("Welcome to Mad Libs!")
	user_inputs = get_user_inputs()
	story = process_story(user_inputs)
	print("\n\n--- STORY TIME ---")
	print(story)
	print("--------\n\n")