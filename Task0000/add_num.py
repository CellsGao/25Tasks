from PIL import Image, ImageDraw, ImageFont



class Image_unread_messege:
    def __init__(self):
        self.fnt = None
        self.im = None

    def open(self, path):
        self.im = Image.open(path)
        return True

    def set_font(self, font_path, size):
        self.fnt = ImageFont.truetype(font_path, size)
        return True

    def draw_text(self, position, str, color, fnt):
        draw = ImageDraw.Draw(self.im)
        draw.text(position, str, fill=color, font=fnt)
        self.im.show()
        self.im.save(str + ' num' + '.jpg')
        return True


test = Image_unread_messege()
test.open("1.png")
test.set_font("Futura.ttf", 80)
test.draw_text((150, -10), '1', (255, 0, 0), test.fnt)
