# person= input("Who is your favorite person?")
# cause= input("Why do yo like this person")
# name= input("her name is")
# age= input("her age")

# print(f"My favorite person is {person},Because she {cause}, Her name is {name},and her age {age} years old")


# person= input("Who is your favorite person? ")
# cause= input("Why do yo like this person")
# name= input("her name is ")
# age= str(int(input("her age")))

# print("My favorite person is" + person + "she" + cause + "her name is" + name + "and her age" + age + "years old")




# print("My favorite person is",person,"she/he",cause, "her name is",name,"and her",age,"years old" )

name = "Anvar"
age = 18
print(name)
print(age)

talabalar = ["Avnar","Dilshod","Malika"]
print(talabalar)

talabalar = ["Anvar","Dilshod","Malika"]
talabalar.append("Sardor")
print(talabalar)

talabalar = ["Anvar","Dilshod","Malika","Sardor"]
talabalar.insert(1,"Otabek")
print(talabalar)

talabalar = ["Anvar","Otabek","Dilshod","Malika","Sardor"]
talabalar1 = ["Gulnoza","Islom"]
talabalar.extend(talabalar1)
print(talabalar)

talabalar = ["Anvar","Otabek","Dilshod","Malika","Sardor","Gulnoza","Islom"]
talabalar.remove("Dilshod")
print(talabalar)

talabalar = ["Anvar","Otabek","Malika","Sardor","Gulnoza","Islom"]
talabalar.pop()
print(talabalar)

talabalar = ["Anvar","Otabek","Malika","Sardor","Gulnoza",]
del talabalar[0]
print(talabalar)

talabalar = ["Otabek","Malika","Sardor","Gulnoza"]
talabalar.sort()
print(talabalar)

talabalar = ["Otabek","Malika","Sardor","Gulnoza"]
talabalar.sort(reverse=True)
print(talabalar)

talabalar = ["Otabek","Malika","Sardor","Gulnoza"]
talabalar.clear()
print(talabalar)

talabalar = ["Otabek","Malika","Sardor","Gulnoza"]
print(len(talabalar))

numbers = [5,10,15,20,25]
numbers.pop(0)
numbers.pop()
print(numbers)

fruits = ["apple","banana","cherry","date","elderberry"]
fruits.remove("apple")
fruits.remove("cherry")
fruits.remove("date")
fruits.remove("elderberry")
print(fruits)

items = [1,2,3,4,5]
items.clear()
print(items)

cars = ["Toyota","Ford","Bmw","Audi"]
cars.remove("Ford")
cars.append("Ford")
print(cars)

numbers = ("10","20","30","40","50",)
numbers = list(numbers)
numbers.append("60")
tuple(numbers)
print(numbers)

tuple1 =(1,2,3)
tuple2=(4,5,6)
print(tuple1 + tuple2)

listnumbers = [10,20,30,40,50]
listnumbers.remove(10)
listnumbers [0]=100
listnumbers.append(60)
print(listnumbers)

fruits = ["apple","banana","cherry"]
fruits.append("orange")
fruits.append("kiwi")
fruits [2] = "mango"
print(fruits)


students = ["Ali","Olim","Zarina","Jasur","Sabina"]
print(students.index("Zarina"))
students.remove("Ali")
students.pop(3)
print(students)

my_tuple = (5,10,15,20,25) 
print(my_tuple[2])
print(len(my_tuple))

my_tuple = (1,2,3)
my_list = [1,2,3]
my_list.append(4)
print(my_list)

colors = ("red","green","blue")
list_colors = list(colors)
list_colors.append("yellow")
print(list_colors)

numbers = [5,10,15,20,25]
numbers.append(30)
numbers.sort(reverse=True)
print(numbers)