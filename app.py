from PIL import Image, ImageDraw, ImageFont
import os
import random
import requests
import json
import flask


def get_random_picture(path = './pictures'):
    pictures = os.listdir(path)
    picture = pictures[random.randint(0, len(pictures) - 1)]
    try:
        img = Image.open(path + '/' + picture)
        return img
    except:
        print('file not found')
        return False

def get_meme(path = './pictures', output_name = 'meme.png'):
    just_a_quote = requests.get('https://api.kanye.rest')
    just_a_quote = just_a_quote.json()['quote']

    img = get_random_picture()
    fnt = ImageFont.truetype("./arial/arial.ttf",45)
    d = ImageDraw.Draw(img)

    quote = ''
    width = img.size[0]
    height = img.size[1]
    text_line_width = int((45 * width)/1200)
    for char_index in range(len(just_a_quote)):
        quote += just_a_quote[char_index]
        if (char_index + 1) % text_line_width == 0:
            quote += '\n' 

    print('\nquote: ' + quote + '\n')
    d.text((int(width * 0.1),int(height * 0.6)), quote, font=fnt, fill=(200, 200, 0))
    img.save('memes/' + output_name)

file_name = input('give me name for your meme file/[nothing] or "NO" for exit\n')
while(file_name != 'NO'):
    if file_name != '':
        get_meme(output_name = file_name)
    else:
        get_meme()
    file_name = input('give me name for your meme file/[nothing] or "NO" for exit\n')