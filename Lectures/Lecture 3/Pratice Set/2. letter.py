letter = '''Dear <|name|>
you are selected
<|Dated|>'''
a = (input("Enter your name:"))
b = (a.capitalize())
c = (letter.replace("<|name|>",b))
d = (input("Enter the Date:"))  
e = (c.replace("<|Dated|>", d))

print (e)

# another way to that
print(letter.replace('<|name|>', a).replace('<|Dated|>', d))