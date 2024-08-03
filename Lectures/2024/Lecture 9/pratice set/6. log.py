#Write a pogram to mine a log file aand find out weather it contain "python"

word = "python"
with open("log.log","r") as l:
     py = l.read()
     if (word in py):
         print(f"{word} is present in file.")
     else:
         print(f"{word} is not present in file.")
         