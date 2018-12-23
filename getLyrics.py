import requests
from bs4 import BeautifulSoup
import re


my_dir = "/Users/jimmylin/Desktop/期末專題/周杰倫/周杰倫-lyrics.txt"

def findsong(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    lyrics = soup.find(id="fsZx3").text

    pat = re.compile(r'\[.*\]')
    lyrics = re.sub(pat, "", lyrics)
    lyrics = lyrics.strip()
    lyrics = lyrics[18:]
    replaceList = ["更多更詳盡歌詞 在 ※ Mojim.com　魔鏡歌詞網", "(", ".", ")", ".", ",", "-", "~", "!", "#", "*", "「", "」", "作詞", "作曲", "方文山", "周杰倫", "提供動態歌詞", "感謝"]
    for i in replaceList:
        lyrics = lyrics.replace(i, "")

    with open(my_dir, "a", encoding='utf-8') as file:
        file.write(lyrics)


# https://mojim.com/twy100951x1x1.htm 周杰倫 1x(1-39)x(1-12?)
# the range of i, k depend on the singer and the album

for i in range(1, 40):
    for k in range(1, 13):
        url = "https://mojim.com/twy100951x" + str(i) + "x" + str(k) + ".htm"
        try:
            findsong(url)
        except:
            print("This url doesn't exist!: " + url)

