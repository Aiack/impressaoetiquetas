from PIL import Image, ImageDraw, ImageFont
import math

def cmToPixel(cms):
    return int(cms * 370.7952755906)

ETIWIDHT = cmToPixel(6.35)
ETIHEIGHT = cmToPixel(3.1)

PAPERWIDHT = cmToPixel(21)
PAPERHEIGHT = cmToPixel(29.7)

class etiqueta():
    def __init__(self):
        self.paper = None
        
        self.buildPaper()
        
        
    def buildEtiqueta(self):
        img = Image.new('RGBA', (ETIWIDHT, ETIHEIGHT), 'yellow')
        
        idraw = ImageDraw.Draw(img)
        
        #O Tijolão
        font = ImageFont.truetype("arialbi.ttf", size=150)
        center_text = int(math.floor((ETIWIDHT / 2) - (font.getsize("O TIJOLÂO")[0] / 2)))
        idraw.text((center_text, 60), "O TIJOLÂO", 'black', font)
        
        #Nome do Produto
        product = "CHAV. TIPO BIELA FURO PASS. 12X12MM 40X135 UNIFORT"
        font = ImageFont.truetype("arial.ttf", size=175)
        
        numLines = math.ceil(len(product) / 23)
        
        lines = []
        if numLines == 3:
            for index, char in enumerate(list(product[:23])):
            lines.append(product[:23])
            lines.append(product[23:46])
        
                
        print(len(product))
        
        if len(product) > 23:
            substringIndex = 0
            for index, char in enumerate(list(product[:23])):
                if char == " ":
                    substringIndex = index

            texts = None        
            if substringIndex:
                texts = [product[:substringIndex], product[substringIndex:]]
            else:
                print('here')
                texts = [product[:23], product[23:]]
            
            for index, text in enumerate(texts):
                center_text = int(math.floor((ETIWIDHT / 2) - (font.getsize(text)[0] / 2)))
                textHeight = 60 + 150 + index * 200
                idraw.text((center_text, textHeight), text, 'black', font)
        
        return img
        
    def buildPaper(self):
        self.paper = Image.new('RGBA', (PAPERWIDHT, PAPERHEIGHT), 'white')
        
        
        self.paper.paste(self.buildEtiqueta(), (int((PAPERWIDHT / 2) - ETIWIDHT / 2), int((PAPERHEIGHT / 2) - ETIHEIGHT / 2)))
        
        self.paper.save('img.png')
        
        