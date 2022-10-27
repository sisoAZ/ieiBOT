import discord
import requests
import os
from PIL import Image, ImageDraw, ImageFont

DISCORD_BOT_TOKEN = "Token"
intents = discord.Intents.all()
intents.members=True
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print("Discord Logged in " + client.user.name)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if "-death" in message.content or "-iei" in message.content or "-kill" in message.content:
        args = sort_args(message.content)
        if len(args) < 1:
            await message.channel.send("Usage: `(-kill|-death|-iei) mention [text]`")
            return
        images = message.mentions[0].avatar.with_size(1024).url
        file_name = str(message.mentions[0].id)
        get_image = requests.get(images, timeout=5).content
        with open("./files" + '/' + file_name + ".png", 'wb') as img_file:
            img_file.write(get_image)
        image_path = os.path.abspath("./files" + '/' + file_name + ".png")
        if len(args) == 3:
            file_name = merge_iei(image_path, args[2])
        else:
            file_name = merge_iei(image_path)
        await message.channel.send(file=discord.File(file_name))
        os.remove(file_name)

def merge_iei(file, text = None):
    image = Image.open(file)
    bg_image = Image.open('./files/iei.png')

    base = Image.new('RGBA', bg_image.size, (255, 255, 255, 0))
    resize_image = image.resize(size=(428, 546))
    base.paste(resize_image.convert("L"), (142, 142))
    base.paste(bg_image, (0, 0), bg_image)
    resize_image.convert("L")
    if text != None:
        draw = ImageDraw.Draw(base)
        font = ImageFont.truetype("arial.ttf", size=70)
        draw.text((340, 400), text, fill=(255, 0, 0), font=font, anchor="mm")
    base.save(file, quality=100)
    return file
def sort_args(text) -> list:
    if " " in text:
        return text.split(" ")
    if "　" in text:
        return text.split("　")
    result = []
    return result

client.run(DISCORD_BOT_TOKEN)

