# A file contaion a word "donkey" multiple times you need to write a program to replace this word with ####### by updating in the same file


#-----------------for full file--------------
# word = "donkey"
# newword  = "######"
# new = word.replace(word,newword)
# with open("donkey.txt","r") as a:
    
#     if(word in a.read()):
#         with open("donkey.txt","w") as a:
#             a.write(new)
#             print(f"We update {word} to {newword}")
#     else:
#         print(f"{word} is not present in this file")



#-----------------for a seprate text--------------
with open("donkey.txt","r") as a:
    text = a.read()
    
text = text.replace('donkey',"######")

with open("donkey.txt","w") as a:
    a.write(text)
        
        


        

        
       
       
        
