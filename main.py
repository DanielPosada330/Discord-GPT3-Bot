# Import os in order to utilize discord and openai APIs

import os
import discord
import openai
from keep_alive import keep_alive

#This calls discord bot secret token.
my_secret = os.environ['DISCORD_BOT_SECRET']

#Put in your personal OpenAI API key here.
OPENAI_KEY = os.environ["OPEN_AI_SECRET"]
openai.api_key = OPENAI_KEY
openai.Model.list()

#Set up object Client to send commands to Discord's Servers.
intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents=intents)


#To ensure that the bot is online, print a message to the console.
@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')


#This is the main function that will be called when the bot is online.
@client.event
async def on_message(message):
  #This is to make sure the bot doesn't respond to itself.
  if message.author == client.user:
    return

  #This is to make sure the bot only responds to messages when it is mentioned in Discord.
  if client.user in message.mentions:

    #Use the OPENAI API to generate a response to the user's message.
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=f"{message.content}",
      max_tokens=2048,
      temperature=0.5,
    )
  #Send the response to the user.
  await message.channel.send(response.choices[0].text)

#To keep the bot alive using Flask
keep_alive()
#This starts the bot.
client.run(my_secret)
