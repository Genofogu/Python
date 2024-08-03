
mydict = {"precariously": "ख़तरनाक ढंग से",
          "rehabilitation":"पुनर्वास",
          "despite":"के बावजूद",
          "chaos":"घोर अव्‍यवस्‍था",
          "neat and tidy":"साफ सुथरा",
          "accumalated":"संचित",
          "unimaginable":"अकल्पनीय",
          "boastful":"घमंडी,शेख़ीबाज़",
          "willing":"इच्‍छुक; उत्‍साहित, तत्‍पर, राज़ी, तैयार",
          "setbacks":"आघात:a difficulty or problem that stops you progressing as fast as you would like",
          "conpelling":"बाध्यकर, प्रबल प्रेरक; विवश करने वाला"}

key = input("Enter a word:")
if(mydict.get(key))== None:
    print("Soory word is not listed")
else:
    print(key+":"+mydict.get(key))
    

        