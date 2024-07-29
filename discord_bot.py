import discord
from discord.ext import commands
import requests
from config import DISCORD_BOT_TOKEN 

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

url = "http://localhost:11434/api/chat"

def llama3(prompt):
    data = {
        "model": "llama3",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False,
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=data)
    
    return response.json()["message"]["content"]

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='ask')
async def ask(ctx, *, question):
    print(f"Received question: {question}")
    try:
        response = llama3(question)
        print(f"Llama3 response: {response}")
        await ctx.send(response)
    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("Sorry, I encountered an error while processing your request.")

bot.run(DISCORD_BOT_TOKEN)