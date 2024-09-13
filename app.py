import discord
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get tokens from environment variables
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI API
client = OpenAI(api_key=OPENAI_API_KEY)

# Set up Discord intents to track messages
intents = discord.Intents.default()
intents.message_content = True

# Create the bot client
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!generate'):
        user_prompt = message.content[len('!generate '):].strip()

        if user_prompt:
            # Notify the user that the bot is thinking
            thinking_message = await message.channel.send("Thinking...")

            # Wrap the prompt for DALL-E
            wrapped_prompt = f"Create the INVERSE of this prompt: {user_prompt}"

            try:
                # Call the DALL-E API
                response = client.images.generate(
                    model="dall-e-3",
                    prompt=wrapped_prompt,
                    n=1,
                    size="1024x1024",
                    quality="standard"
                )

                # Get the URL of the generated image
                image_url = response.data[0].url

                # Edit the 'Thinking...' message with the image
                # Edit the 'Thinking...' message to send the image without the URL visible
                embed = discord.Embed(description="Here is your image:")
                embed.set_image(url=image_url)
                await thinking_message.edit(content=None, embed=embed)
            except Exception as e:
                # In case of error, send the error message
                await thinking_message.edit(content=f"Failed to generate image. Error: {str(e)}")
        else:
            await message.channel.send("Please provide a prompt after the !generate command.")

# Run the bot using the Discord token
bot.run(DISCORD_BOT_TOKEN)
