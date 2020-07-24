def check(choice,key):
    if choice=="decrypt":
        key=-key
        return key
    else:
        return key
print("Do you wish to encrypt or decrypt a message?")
choice=str(input())
print("Enter your message:")
message=str(input())
print("Enter a key number (1-26)")
key=int(input())
key=check(choice,key)
translated_msg=''
for i in message:
    if i.isalpha():
        num=ord(i)
        num+=key
        if i.isupper():
            if num > ord('Z'):
                num -= 26
            elif num < ord('A'):
                num += 26
        elif i.islower():
            if num > ord('z'):
                 num -= 26
            elif num < ord('a'):
                num += 26
        translated_msg+=chr(num)
    else:
        translated_msg+=i
print("Translated message is:")
print(translated_msg)