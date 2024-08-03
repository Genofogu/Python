#Write aprogram to make acopy of a text file "star.txt"


with open("star.txt","r")as f:
    a = f.read()
    for j in range(1,14):
        with open(f"Copying/{j}.txt","w") as f:
         f.write(a)








    
    
    
    
    
    
    
    
    
    
    
    
