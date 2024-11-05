#1)

ls =["someone", 110, 11.0, False, 11, "hello", "hi", 10, "good", True]


print(len(ls))

#2)

sl =["someone", 10, 1.0, True, 12, "why?", "gooddd", 11, "good", True]

for i in range(9):
    print(sl[1])
    #???
    
#3)

ls =["someone", 110, 11.0, False, 11, "hello", "hi", 10, "good", True]
ls.append(False)
# ეს ფუნქცია ამატებს ამ ლისტს რასაც შიგნით ფრჩხილებში ჩაწერ
print(ls)

#4)

for i in range (10):
    ls.append(i)
print(ls)