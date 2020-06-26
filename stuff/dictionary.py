# Dictionary Practice

# Create dictionary
car = {
    "brand": "ford",
    "model": "figo",
    "year": 2016
}

print(car)

# Access item with key
print(car["model"])
print(car.get("model"))

# Change values
car["year"] = 2019
print(car)

# Looping and printing keys and values
for i in car:
    print(i)

for i in car:
    print(car[i])

# Value function
for x in car.values():
    print("aaa%%%"+str(x))

# Check key exists
if "model" in car:
    print("yes, model is a key in the dictionary  - car")

# Length
print(len(car))

# adding new key
car["color"] = "ruby red"
print(car)

# removing key

car.pop("model")
print(car)

# last inserted item
car.popitem()
print(car)

# del delete complete dictionary
# clear() empties the dictionary

# copy
car1 = car.copy()
print(car1)

# nested dictionary
ford = {
    "car1": {
        "name": "figo",
        "year": 2016
    },
    "car2": {
        "name": "aspire",
        "year": 2017
    },
    "car3":{
        "name": "endevour",
        "year": 2019
    }
}

print(ford)