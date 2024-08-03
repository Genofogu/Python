dis = {"this is some" : "ohh relly",
       34: 43,
       "sdfs": "sdfsf",
       "list": [2,54,65,"dfsf"],
       }

print(dis)
print(dis["sdfs"])
print(type(dis))  

# distnary methords

# 1.items methods
for item in dis.items():
       print(item)

# 2. key method
for key in dis.keys():
       print(key)
       
# 3. update method
dis.update({"this is some" : "sdfdfsfsdfs",})
print("thid is an updated dict",dis)

#4. get method
print("thid is not given an error",dis.get("sdff"))