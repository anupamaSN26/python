
#Count the occurrences of each word in a line of text. 
Text=input("Enter the text:")
words= {}
for word in Text.split(' '):
    if word in words.keys():
        words[word]+=1
    else:
        words[word]=1
        
print(words)