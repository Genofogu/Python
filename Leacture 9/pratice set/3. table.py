#Write a program to gentate a multiplation tables of 2 to 20 and write it to the different file.Plase these files in a floder for a 13 year old.

for i in range (2,21):
    table = ''
    for j in range(1,11):
       table += f"{i} x {j} = {i*j}\n"
    with open(f"tables/{i}.txt","w") as f:
        f.write(table)
        
     