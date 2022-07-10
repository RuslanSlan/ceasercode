x = int(input())
b = input()
decryption = 0
for i in range(len(b)):
    decryption = ord(b[i]) - x      # Перетвореня символа в Unicode
    if decryption < 97:             # Коли виходить за межу алфавіту, тоді починається заново з букви а на z
        decryption += 26
    print(chr(decryption), end='')