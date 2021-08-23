sentence,age = input("Enter Sentence and age : ").split(",")
print("Sentence enter {} and age {} and lenght {}: ".format(sentence.strip().upper(),age.strip(),len(sentence)))
char = input("Enter char want to count : ")
print("Char : \"{}\" in sentence is : \"{}\" times".format(char,sentence.strip().lower().count(char.strip().lower())))

findchar = input("Enter the char found in string : ")
print("Char found at {} position".format(sentence.lower().find(findchar.lower())))
print("Char found at {} position".format(sentence.lower().find(findchar.lower(),sentence.lower().find(findchar.lower())+1)))

  # to replace 2 
print("Sentence enter {}".format(sentence.replace("boy","girl",2)))

print("{}".format(sentence.center(len(sentence)+8,"*")))

sentence = "I am a good boy , I am a good girl    "
words = sentence.strip(" ").split(",")
print(words[0])
if "good" in words[0]:
    print("present")
else:
    print("not present")
print(sentence[::-1]) #reverse the string
print(sentence[::2]) #print second char in string

for i in words:
    print(i.strip(" "))