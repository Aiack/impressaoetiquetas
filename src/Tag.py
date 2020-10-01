from PIL import Image, ImageDraw, ImageFont
import math

def cmToPixel(cms):
    return int(cms * 370.7952755906)


class Tag():    
    def __init__(self, name, value, code):
        self.TAGWIDHT = cmToPixel(6.35)
        self.TAGHEIGHT = cmToPixel(3.1)
        
        self.img = None
        
        self.name = name
        self.value = value
        self.code = code
        
        self.buildImg()
        self.addLogoText()
        self.addProductText()
        
    def buildImg(self):
        self.img = Image.new('RGBA', (self.TAGWIDHT, self.TAGHEIGHT), 'yellow')
        self.idraw = ImageDraw.Draw(self.img)
        
    def addLogoText(self):
        font = ImageFont.truetype("arialbi.ttf", size=150)
        center_text = int(math.floor((self.TAGWIDHT / 2) - (font.getsize("O TIJOLÂO")[0] / 2)))
        self.idraw.text((center_text, 60), "O TIJOLÂO", 'black', font)
        
    def addProductText(self):
        lines = []
        # lastIndex = 0
        # while lastIndex < len(self.name):
        #     lastSpaceIndex = lastIndex
        #     for index, char in enumerate(list(self.name[lastIndex: (len(lines) + 1) * 23])):
        #         if char == " ":
        #             lastSpaceIndex = index
            
        #     if lastSpaceIndex != lastIndex:
        #         lines.append(self.name[lastIndex: lastSpaceIndex])
        #         lastIndex = lastSpaceIndex
        #         print(lastIndex)
        #     else:
        #         lines.append(self.name[lastIndex: (len(lines) + 1) * 23])
        #         lastIndex = (len(lines) + 1) * 23
        #         print("else")
        
        words = self.name.split()
        line = ''
        for index, word in enumerate(words):
            if len(line + ' ' + word) <= 23:
                if line == '':
                    line = word
                else:
                    line = line + ' ' + word
            else:
                lines.append(line)
                line = ''
                
        print(lines)
                            
        # product = "CHAV. TIPO BIELA FURO PASS. 12X12MM 40X135 UNIFORT"
        # font = ImageFont.truetype("arial.ttf", size=175)
        
        # numLines = math.ceil(len(product) / 23)
        
        # lines = []
        # if numLines == 3:
        #     substringIndex = 0
        #     for index, char in enumerate(list(product[:23])):
        
                
        # print(len(product))
        
        # if len(product) > 23:
        #     substringIndex = 0
        #     for index, char in enumerate(list(product[:23])):
        #         if char == " ":
        #             substringIndex = index

        #     texts = None        
        #     if substringIndex:
        #         texts = [product[:substringIndex], product[substringIndex:]]
        #     else:
        #         print('here')
        #         texts = [product[:23], product[23:]]
            
        #     for index, text in enumerate(texts):
        #         center_text = int(math.floor((ETIWIDHT / 2) - (font.getsize(text)[0] / 2)))
        #         textHeight = 60 + 150 + index * 200
        #         idraw.text((center_text, textHeight), text, 'black', font)
    
        
    