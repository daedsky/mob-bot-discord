import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np


class Utility:
    @staticmethod
    def get_text_size(text, font: ImageFont.FreeTypeFont):
        img = Image.new('L', (1, 1))
        draw = ImageDraw.Draw(img)
        w, h = draw.textsize(text, font=font)
        return w, h

    @staticmethod
    def refine_text(text, lpl):
        """lpl: letters per line"""

        if len(text) <= lpl:
            refined_text = text
        else:
            c = lpl
            refined_text = f'{text[0:lpl]}\n' if text[lpl] == ' ' else f'{text[0:lpl]}-\n'
            while c <= len(text):
                try:
                    ltr = text[c + lpl]
                except IndexError:
                    ltr = ' '

                if ltr == ' ':
                    line = f'{text[c:c + lpl]} \n'.removeprefix(' ')
                    refined_text += line
                else:
                    line = f'{text[c:c + lpl]}-\n'.removeprefix(' ')
                    refined_text += line

                c = c + lpl

        return refined_text


class ImageFunctions:
    @staticmethod
    async def grave(image, save_to):
        with Image.open('./meme_templates/gravestone.jpg') as img:
            with Image.open(image) as avatar:
                avatar = avatar.resize((310, 310))
                img.paste(avatar, (183, 400))
                img.save(save_to)

    @staticmethod
    async def joke_over_head(image, save_to):
        with Image.open('./meme_templates/joke_over_head_transparent.png') as img:
            with Image.open(image) as avatar:
                avatar = avatar.resize((200, 200))
                img2 = Image.new('RGBA', img.size)
                print(img.mode)
                img2.paste(avatar, (180, 175))
                img2.paste(img, mask=img)
                img2.save(save_to)

    @staticmethod
    async def water_meme(text, save_to):
        with Image.open('./meme_templates/water_meme.jpg') as img:
            font = ImageFont.truetype('./fonts/Roboto-Regular.ttf', 38)
            draw = ImageDraw.Draw(img)
            refined_text = Utility.refine_text(text, 20)
            lines = refined_text.count('\n')
            y = 270 // (lines * 1.5) + 68 if lines > 0 else 240
            draw.multiline_text((304, y), refined_text, fill='#000000', font=font)
            img.save(save_to)

    @staticmethod
    async def supreme(text, save_to):
        font = ImageFont.truetype('./fonts/Futura Bold Italic font.ttf', size=68)
        w, h = Utility.get_text_size(text, font)
        img = Image.new('RGB', size=(w + 15, h + 15), color='#ff0100')
        draw = ImageDraw.Draw(img)
        draw.text((10, 0), text, fill='#ffffff', font=font)
        img.save(save_to)

    @staticmethod
    async def phub(text1, text2, save_to):
        font = ImageFont.truetype('./fonts/Roboto-Regular.ttf', 56)
        height = 64

        w1, h1 = Utility.get_text_size(text1, font)
        w1 = w1 + 10
        img1 = Image.new('RGB', size=(w1, height), color='#000000')
        draw1 = ImageDraw.Draw(img1)
        draw1.text((w1 - 5, 0), text1, fill='#ffffff', font=font, anchor='ra')

        w2, h2 = Utility.get_text_size(text2, font)
        w2 = w2 + 10
        img2 = Image.new('RGB', size=(w2, height), color='#000000')
        draw2 = ImageDraw.Draw(img2)
        draw2.rounded_rectangle((0, 0, w2, height), radius=5, fill='#f8981f')
        draw2.text((5, 0), text2, fill='#000000', font=font)

        w3 = w1 + w2 + 40
        img3 = Image.new('RGB', size=(w3, height + 40), color='#000000')
        img3.paste(img1, (20, 20))
        img3.paste(img2, (w1 + 20, 20))
        img3.save(save_to)

    @staticmethod
    async def communist(image, save_to):
        with Image.open(image) as img:
            with Image.open('meme_templates/communist.png') as communist_flag:
                img = img.convert(mode='RGBA')
                communist_flag = communist_flag.convert(mode='RGBA')

                resized_communist_flag = communist_flag.resize((img.width, img.height))

                alpha_blend = Image.blend(img, resized_communist_flag, 0.4)
                alpha_blend.save(save_to)

    @staticmethod
    async def gay(image, save_to):
        with Image.open(image) as img:
            with Image.open('./meme_templates/gay_flag.png') as gay_flag:
                img = img.convert(mode='RGBA')
                gay_flag = gay_flag.convert(mode='RGBA')

                resized_gay_flag = gay_flag.resize(img.size)

                alpha_blend = Image.blend(img, resized_gay_flag, 0.4)
                alpha_blend.save(save_to)

    @staticmethod
    async def captcha(text, save_to):
        with Image.open('./meme_templates/captcha_template.png') as img:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/Roboto-Regular.ttf', 18)
            draw.text((100, 74), text, fill=(0, 0, 0), font=font)
            img.save(save_to)

    @staticmethod
    async def fact(text, save_to):
        with Image.open('./meme_templates/facts.png') as img:
            font = ImageFont.truetype('./fonts/Roboto-Regular.ttf', 16)

            text_img = Image.new('RGBA', (262, 170), color=(0, 0, 0, 0))
            draw = ImageDraw.Draw(text_img)

            draw.multiline_text((0, 0), Utility.refine_text(text, 34), fill='#000000', font=font)
            rotated_img = text_img.rotate(343, expand=True, resample=Image.Resampling.BICUBIC)

            img.paste(rotated_img, (0, 430), rotated_img)
            img.save(save_to)

    @staticmethod
    async def did_you_mean(search_text, suggestion_text, save_to):
        with Image.open('./meme_templates/did_you_mean_template.png') as img:
            search_font = ImageFont.truetype('./fonts/Roboto-Regular.ttf', 16)
            suggestion_font = ImageFont.truetype('./fonts/Roboto-MediumItalic.ttf', 18)
            draw = ImageDraw.Draw(img)
            draw.text(xy=(178, 94), text=search_text, fill='#000000', font=search_font)
            draw.text(xy=(317, 243), text=suggestion_text, fill='#1a0dab', font=suggestion_font)
            img.save(save_to)

    @staticmethod
    async def pencil(fp, save_to):
        img = cv2.imread(fp)
        pencil, coloured = cv2.pencilSketch(img, sigma_s=3, sigma_r=0.07, shade_factor=0.07)
        cv2.imwrite(save_to, pencil)

    @staticmethod
    async def colored_ketch(fp, save_to):
        img = cv2.imread(fp)
        pencil, coloured = cv2.pencilSketch(img, sigma_s=3, sigma_r=0.07, shade_factor=0.07)
        cv2.imwrite(save_to, coloured)

    @staticmethod
    async def canny(fp, save_to):
        img = cv2.imread(fp)
        canny_img = cv2.Canny(img, threshold1=100, threshold2=250)
        cv2.imwrite(save_to, canny_img)

    @staticmethod
    async def brazzers(fp, save_to):
        with Image.open("./meme_templates/brazzers.png") as bzpic:
            with Image.open(fp) as img:
                resizedbz = bzpic.resize(
                    (int(bzpic.width * (img.width / 1400)), int(bzpic.height * (img.height / 1000))))
                img.paste(resizedbz, (img.width - resizedbz.width, img.height - resizedbz.height))
                img.save(save_to)

    @staticmethod
    async def ship(avatar1, avatar2, save_to):
        img = cv2.imread("./meme_templates/heart.png")
        img_width = 225
        img_height = 225

        avatar1 = cv2.imread(avatar1)
        resizedav1 = cv2.resize(avatar1, (img_width, img_height))

        avatar2 = cv2.imread(avatar2)
        resizedav2 = cv2.resize(avatar2, (img_width, img_height))

        out = np.hstack((resizedav1, img, resizedav2))

        cv2.imwrite(save_to, out)

    @staticmethod
    async def drake(text1, text2, save_to):
        with Image.open("meme_templates/drake.jpg") as img:
            font = ImageFont.truetype("./fonts/Itim.ttf", 22)
            draw = ImageDraw.Draw(img)

            if len(text1) < 29:
                draw.multiline_text((int(img.width / 2 + 10), int(img.height / 4.5)), text=text1, fill=(0, 0, 0),
                                    font=font)
            else:
                upper_text = Utility.refine_text(text1, 29)
                draw.multiline_text((int(img.width / 2 + 10), 30), text=upper_text, fill=(0, 0, 0), font=font)

            if len(text2) < 29:
                draw.multiline_text((int(img.width / 2 + 10), 380), text=text2, fill=(0, 0, 0), font=font)

            else:
                lower_text = Utility.refine_text(text2, 29)
                draw.multiline_text((int(img.width / 2 + 10), 320), text=lower_text, fill=(0, 0, 0), font=font)

            img.save(save_to)

    @staticmethod
    async def write_motivation(text, save_to):
        with Image.open("./meme_templates/motivation.jpg") as img:
            draw = ImageDraw.Draw(img)
            motivation = Utility.refine_text(text, 33)
            font = ImageFont.truetype("./fonts/yrsa.ttf", 80)

            if len(text) < 28:  # len(text) < 33:
                draw.text((170, 400), text=text, fill=(0, 0, 0), font=font)

            elif 28 <= len(text) <= 186:
                draw.text((100, 250), text=motivation, fill=(0, 0, 0), font=font)

            else:
                draw.text((100, 100), text=motivation, fill=(0, 0, 0), font=font)

            img.save(save_to)

    @staticmethod
    async def whathow(image, save_to):
        with Image.open("./meme_templates/whathow.jpg") as img:
            with Image.open(image) as avatar:
                resized_avatar = avatar.resize((110, 110))
                img.paste(resized_avatar, (133, 55))
                img.save(save_to)

    @staticmethod
    async def detailscard(avatar, name, email, pswd, phno, virginstatus, networth, profession, save_to):
        with Image.open("./meme_templates/details.png") as img:
            font = ImageFont.truetype("./fonts/opensans.ttf", 28)
            draw = ImageDraw.Draw(img)
            draw.text((402, 91), text=name, fill=(0, 0, 0), font=font)
            draw.text((402, 124), text=email, fill=(0, 0, 0), font=font)
            draw.text((445, 157), text=pswd, fill=(0, 0, 0), font=font)
            draw.text((440, 192), text=phno, fill=(0, 0, 0), font=font)
            draw.text((408, 224), text=virginstatus, fill=(0, 0, 0), font=font)
            draw.text((455, 258), text=networth, fill=(0, 0, 0), font=font)
            draw.text((457, 291), text=profession, fill=(0, 0, 0), font=font)

            with Image.open(avatar) as av:
                res = av.resize((218, 218))
                img.paste(res, (59, 116))

                img.save(save_to)

    @staticmethod
    async def paise_barbad_bc(text, save_to):
        with Image.open("./meme_templates/paisabarbad.jpg") as img:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("./fonts/yrsa.ttf", 45)
            thetext = Utility.refine_text(text, 34)

            if len(text) < 34:
                draw.multiline_text((40, 200), text=text, fill=(255, 0, 0), font=font)
                img = img.crop((0, 160, img.width, img.height))

            elif 34 <= len(text) <= 67:
                draw.multiline_text((40, 160), text=thetext, fill=(255, 0, 0), font=font)
                img = img.crop((0, 120, img.width, img.height))

            elif 68 <= len(text) <= 100:
                draw.multiline_text((40, 115), text=thetext, fill=(255, 0, 0), font=font)
                img = img.crop((0, 65, img.width, img.height))

            else:
                draw.multiline_text((40, 80), text=thetext, fill=(255, 0, 0), font=font)
                img = img.crop((0, 40, img.width, img.height))

            img.save(save_to)

    @staticmethod
    async def trump(text, save_to):
        with Image.open("./meme_templates/trump.jpg") as img:
            the_text = Utility.refine_text(text, 48)

            font = ImageFont.truetype("./fonts/opensans.ttf", 18)
            draw = ImageDraw.Draw(img)
            draw.multiline_text((15, 55), text=the_text, fill=(0, 0, 0), font=font)

            img.save(save_to)




if __name__ == '__main__':
    import asyncio

    # asyncio.run(ImageFunctions.drake('Almost before we knew it, we had left the ground. The quck brown fox jumped over the lazy dog. A peep at some distant orb has power to raise and purify our thoughts like a strain of sacred music, or a noble picture, or a passage from the grander poets. It always does one good.'))
    asyncio.run(ImageFunctions.grave('./meme_templates/communist.png', 'lamd'))
