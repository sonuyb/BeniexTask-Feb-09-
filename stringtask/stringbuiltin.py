#1.capitalize..
txt = "hello,  welcome all ."
x = txt.capitalize()
print (x)

#2.find..
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

#3strip..
txt = "apple"
x = txt.strip()
print("of all fruits", x, "is my favorite")

#4.format..
txt1 = "My name is {fname}, I'm {age}".format(fname = "Aswin", age = 29)
txt2 = "My name is {0}, I'm {1}".format("Aswin",29)
txt3 = "My name is {}, I'm {}".format("Aswin",29)
print(txt1)
print(txt2)
print(txt3)

#5.isalnum
txt = "Company53"
x = txt.isalnum()
print(x)

#6.isalpha
txt = "CompanyX"
x = txt.isalpha()
print(x)

#7.lower..
txt = "car"
x = txt.lower()
print(x)

#8.upper..
txt = "car"
x = txt.upper()
print(x)

#9.replace..
txt = "your company is good"
x = txt.replace('company','house')
print(x)

#10.split
txt = "your company is good"
x = txt.split()
print(x)

#11.count..
txt = "your car is porsche.car is in red color"
x = txt.count('car')
print(x)

#12.index..
txt = "Hello, welcome to my ownplace."
x = txt.index("welcome")
print(x)

# 13.isdigit..
txt = "49810"
x = txt.isdigit()
print(x)

#14. islower..
txt = "good morning!"
x = txt.islower()
print(x)

#15. isupper..
txt = "GOOD MORNING!"
x = txt.isupper()
print(x)