'''
Caesar Chiper
'''

#import pyperclip

#THE STRING TO BE DECRYPTED AND ENCRYPTED! 

message = "This is my secret message"

#THE KEY!

key = 13

mode = "encrypt"

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_!?.&*()#þłßð"

translated = ""

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        if mode == "encrypt":
            translateIndex = symbolIndex + key
        elif mode == "decrypt":
            translateIndex = symbolIndex - key
            
        if translateIndex >= len(SYMBOLS):
            translateIndex = translateIndex - len(SYMBOLS)
        elif translateIndex < 0:
            translateIndex = translateIndex + len(SYMBOLS)
        translateIndex = translated + SYMBOLS[translateIndex]
    else:
        translated = translated + symbol

print(translated)
#pyperclip.copy(translated)