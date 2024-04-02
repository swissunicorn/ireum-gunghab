from flask import Flask
import math

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulations, it's a web app!"

SBase = 0xAC00
LBase = 0x1100
VBase = 0x1161
TBase = 0x11A7
LCount = 19
VCount = 21
TCount = 28
NCount = 588
SCount = 11172

strokeCount = {
    'ㅂ': 4,
    'ㅈ': 3,
    'ㄷ': 3,
    'ㄱ': 2,
    'ㅅ': 2,
    'ㅛ': 3,
    'ㅕ': 3,
    'ㅑ': 3,
    'ㅐ': 3,
    'ㅒ': 4,
    'ㅖ': 4,
    'ㅔ': 3,
    'ㅁ': 4,
    'ㄴ': 2,
    'ㅇ': 1,
    'ㄹ': 5,
    'ㅎ': 3,
    'ㅗ': 2,
    'ㅓ': 2,
    'ㅏ': 2,
    'ㅣ': 1,
    'ㅋ': 3,
    'ㅌ': 4,
    'ㅊ': 4,
    'ㅍ': 4,
    'ㅠ': 3,
    'ㅜ': 2,
    'ㅡ': 1,
    'ㅚ': 3,
    'ㅢ': 2,
    'ㅟ': 3,
    'ㅘ': 4,
    'ㅝ': 4,
    'ㅞ': 5,
    'ㅙ': 5,
    '': 0
}

def syllableDecomp(s):
    SIndex = s - SBase #4340 
    LIndex = math.floor(SIndex / NCount) #7
    VIndex = math.floor((SIndex % NCount) / TCount) #8
    TIndex = SIndex % TCount # 0
    LPart = LBase + LIndex #4359
    VPart = VBase + VIndex #4457
    TPart = 0
    l = chr(LPart)
    v = chr(TPart)
    t = ''
    if TIndex > 0:  
        TPart = TBase + TIndex # batchim 
        t = chr(TPart)
    numStrokes = strokeCount[l] + strokeCount[v] + strokeCount[t]
    return numStrokes


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

test1 = "한"
print(syllableDecomp(test1))