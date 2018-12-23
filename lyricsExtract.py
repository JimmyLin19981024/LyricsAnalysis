import jieba
import jieba.posseg as pseg

file_dir = "/Users/jimmylin/Desktop/期末專題/周杰倫/七里香-lyrics.txt"
with open(file_dir , encoding="utf8") as f:
    text = f.read()
text_refined = text.replace("　", "").replace("\n", "")

from collections import Counter
wordCount = Counter()

stopWord = [' ', '_', '＃', '＊', '～', '歌詞', '修正', '一', ':', '/', 'Repeat', "'", "I", 'blank', '沒有', '不要', '不能', '想要', '不到', '不用', '不想', '只能', '知道', 'you', 'the', 'to', 'me', 'in', 'on', 'of', 'your', 'and', 'no', 'be', 'it', 'is', 'na', 'with', 'that', '所有', 'ba', 'oh', 'Oh', 'ko', 'so', 'up', 'ka', 'shi', 'ta', 're', 'go', 'mi', 'for', 'don', 'all', 'Ya', 'know', 'll', 'ku', '能夠', '是否', 'ni', 'are', 'What', 'Shorty', 'wo', 'te', 'got', 'can', 'It', 'this', 'And', 'not', 'gonna', 'have', 'ga', 'as', 'Woo', 'la', 'You', 'yo', 'wa', 'da', '可能', 'by', 'Was', 'de', 'ki', 'do', 'ru', 'out', 'get', 'was', 'No', 'ra', 'ri', 'am', 'will', 'JJ', 'ng', '不了', 'she', '披上', 'Dolin', '陳冬霖', 'ye', 've', '之外', '編曲', 'there', 'goes', 'ah', 'Just', 'Wu', '無法', 'yeah', 'Lupo', 'Groinig', 'about', 'My', 'Ha', 'One', '鄧紫棋', 'In', 'did', 'GEM', 'done', 'keep', 'wanna', 'You', 'where', 'GAME', 'IS', 'OVER', 'ai', 'Get', 'tell', 'But', 'tic', 'The', 'Within', 'DID', 'youI', 'DON', 'gave', 'my', 'we', 'DJ', 'like', 'just', 'THE', 'let', 'here', '蘇偉', '提供', 'TO', 'want', '跟著', 'Don', '羅百吉', '開始', 'GONNA', 'ON', 'IT', '看著', 'Where', 'YOUR', 'WANNA', 'YOU', 'come', 'way', 'new', 'LET', 'AND', 'IN', 'ate', 'Chiquita', '友站', 'var', 'funciton', 'Array', 'xx9a', 'http', 'https', 'xx9s', 'NO', 'Wan', 'Hi', 'blueI', 'groove', 'common', 'hoagei', 'weibo', 'Stand', 'PA', 'upGet', 'Evan', 'Avery', 'SIZE', '子安靜', '梁思樺','say','Ba','why','Try','ha','BAD','裡面','Tang','babybaby','tin','goodbyeTry','東想','Yes','張惠妹','Jae','徐光義','NoK','SO','FUN','hey','La','make','some','ayuan740622','senorita','find','from','蔡伯南','Repaet','玩遊','韋禮安','為了','outta','Luvin','就算','getting','what','heregetting','了你','留給','function','her','but','Cause','hereThis','ix1','jess','Shianlun','Cuz','mineMineMine','不鈴不鈴','or','杰倫','Gary','Na','徐若瑄','邁可林','妳在','tang891228','far','MV','cuz','beWanna','key','gotta','follow','beatNow','two','more','FaFa','AllenA','自動變','AGOGO','sa','ma','eop','kka','jeom','dae','lo']


for word, tag in pseg.cut(text_refined):
    if tag != "c" and tag != "r" and tag != "m" and tag != "df" and tag != "d" and word not in stopWord and len(word) > 1:
        wordCount[word] += 1

wordlist = []
for word, number in wordCount.most_common(200):
    print(word, number)

    for k in range(number):
        wordlist.append(word)

# https://wordcloud.timdream.org/
# join the words for creating word cloud
print(",".join(wordlist))


