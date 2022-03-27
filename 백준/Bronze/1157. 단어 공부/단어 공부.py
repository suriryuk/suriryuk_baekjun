string = input()
big_count = []
many = {"alphabet" : "A", "count" : 0}

string = string.upper()

for i in range(65, 91):
    count = string.count(chr(i))
    if count != 0:
        big_count.append(count)
        if count > many["count"]:
            many["alphabet"] = chr(i)
            many["count"] = count
            
if big_count.count(many["count"]) > 1:
    print("?")
else:
    print(many["alphabet"])
