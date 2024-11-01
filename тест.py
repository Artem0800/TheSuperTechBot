s = "asus huy pizda 16gb"
p = "asus 24gb".split()
if all(word in s for word in p):
    print(True)
else:
    print(False)
