import discord
import requests
import os
from merge_iei import merge_iei

client = discord.Client()

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
        image_url = message.mentions[0].avatar_url_as(format="png", size=1024)
        file_name = str(message.mentions[0].id)
        get_image = requests.get(image_url, timeout=5).content
        with open("./files" + '/' + file_name + ".png", 'wb') as img_file:
            img_file.write(get_image)
        image_path = os.path.abspath("./files" + '/' + file_name + ".png")
        if len(args) == 3:
            file_name = merge_iei(image_path, args[2])
        else:
            file_name = merge_iei(image_path)
        await message.channel.send(file=discord.File(file_name))
        os.remove(file_name)

def sort_args(text) -> list:
    if " " in text:
        return text.split(" ")
    if "　" in text:
        return text.split("　")
    result = []
    return result

client.run("")