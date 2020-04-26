# import datetime
# print(datetime.datetime.now())
#
# student_grades={"jatin": 30,"ginni": 30}
# print(student_grades.values())
# print(student_grades.keys())
#
# def mean(mylist):
#     the_mean= sum(mylist)/len(mylist)
#     print(the_mean)
#     return the_mean
#
# print(mean([6,8,9]))

# def weather_check(temp):
#     if temp > 7:
#         return "Warm"
#     else:
#         return "Cold"
#
# user_input = float(input("Enter temp:"))
# print(weather_check(user_input))

# phpne_numbers={"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
# for value in phpne_numbers.values():
#     print(value.replace("++", "00"))

# temps = [222, 333, 333, 444]
# new_temp = [temp/10 for temp in temps if temp > 1]
# print(new_temp)

# def foo(my_list):
#     # my_list = [1, 2, 3, 'dd', 'fffff']
#     new_list = [m for m in my_list if not isinstance(m, str)]
#     print(new_list)
#     return new_list
#
# foo([1, 2, 3, 'dd', 'fffff'])

# def bar(mylist):
#     positive_list = [m for m in mylist if m > 0]
#     print(positive_list)
#     return positive_list
#
# bar([1, 2, 3, -1, -10])

# def fooo(my_list):
#     new_list = [m if not isinstance(m, str) else 0 for m in my_list]
#     print(new_list)
#     return new_list
#
# fooo([1, 2, 3, 'dd', 'fffff'])

# def foooo(my_list):
#     new_list = [m if not isinstance(m, str) else float(m) for m in my_list]
#     summ = sum(new_list)
#     print(summ)
#     return summ
#
# foooo(['1.1','2.2','3.2'])

import pandas

def con(first,second):
    print(first+second)
    return(first+second)

con('jatin','ginni')

def mean(*args):
    list=sum(args)/len(args)
    return list

print(mean(1,3,5))


def upp(*args):
    args=[n.upper() for n in args ]
    ln=sorted(args)
    return ln

print(upp("jatin","baby","ginni"))

with open("file.txt", "w") as file:
    file.write("snail")

with open("bear.txt") as file2:
    file3 = file2.read()

with open("first.txt","w") as f:
    f.write(file3[:9])

with open("bear1.txt") as b1:
    gg = b1.read()

with open("bear2.txt","a") as b2:
    b2.write(gg)

with open("file.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)