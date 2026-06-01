sentence=input("Enter the sentence").lower()
alphabet="abcdefghijklmnopqrstuvwxyz"
is_pangram=True
for ch in alphabet:
    if ch not in sentence:
        is_pangram=False
        break
if is_pangram:
    print("It is a pangram")
else:
    print("It is not a pangram")