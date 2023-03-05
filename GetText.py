import pyautogui
import pynput
import time
import pytesseract
from PIL import ImageGrab
from PIL import Image
import random

prompt = ["Give me a funny paragraph to say in video format on the internet that is not offensive",
          "Give me a funny paragraph to say in a video format on the internet about tech that is not offensive",
          "Give me a funny event in paragraph form to say on TikTok that is not offensive",
          "Give me a funny paragraph to say in video format on the internet about anime that is not offensive",
          "Give me a funny paragraph to say in video format on the internet about cooking that is not offensive",
          "Give me a funny paragraph to say in video format on the internet that is not offensive about gaming",
          "Give me a funny paragraph to say about youtube in a video format on the internet that is not offensive",
          "Give me a funny paragraph to say in video format on the internet that is not offensive about Twitch",
          "Give me a funny paragraph to say in video format on the internet about TikTok that is not offensive",
          "Give me a funny paragraph to say in a video format on the internet about AI that is not offensive"]

mouseCon = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

file = open("Responses3.txt", "w")

#initialSetup
time.sleep(15)

def PointAndClick(xTo, yTo, click):
    pyautogui.moveTo(xTo, yTo)
    time.sleep(1)
    if click:
        pyautogui.leftClick()
    time.sleep(1)
    
PointAndClick(704, 921, True)
keyboard.type(random.choice(prompt))
PointAndClick(1606, 927, True)

for i in range(90):
    print(f"checking | {i +1}")
    offset = random.randrange(13, 751)
    time.sleep(180 + offset)
    
    im = ImageGrab.grab(bbox=(717, 244, 1544, 786))
    im.save(f"./Photos/Photo#{i+1}.png")
    time.sleep(1)
    imIm = Image.open(f"./Photos/Photo#{i+1}.png")
    
    response = pytesseract.image_to_string(imIm)
    print("Actual | ")
    print(response)
    
    response = response.replace("“", '"')
    response = response.replace("”", '"')
    response = response.split('"')
    
    res = max(response, key=len)
    res = res.replace("\n", " ")
    res = res.replace("|", "I")
    print("Modified | ")
    print(res)
    
    file.write(res)
    file.write("\n")
    file.write("\n")
    
    if i % 2 == 0:
        PointAndClick(244, 171, True)
        time.sleep(2)
        PointAndClick(704, 921, True)
        keyboard.type(random.choice(prompt))
        PointAndClick(1606, 927, True)
        continue
    
    PointAndClick(1165, 870, True)