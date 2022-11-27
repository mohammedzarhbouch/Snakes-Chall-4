

# light_is_on = True
# if light_is_on:
#     print("hello")
#     print("the light is on poggers!")


# bottle_is_open = False

# if bottle_is_open:
#     print("the bottle is open!")
# else:
#     print("the bottle is closed")


# weight = 48.7

# if weight > 50:
#     print("you're overweight:)")
# else:
#     print("eat something fat ass")
    
# age = 17

# if age == 18:
#     print("that's the right age there pal")
# else:
#     print("wrong age buddy")


# import random

# print(random.randint(1,3))


# answer = random.randint(1,3)

# if answer == 1:
#     print("yes")

# if answer == 2:
#     print("no")

# if answer == 3:
#     print("maybe")


# print(random.var())

# import random

# lucky_number = random.randint(1,100)

# print(f"you will have a great day! your lucky number is: {lucky_number}" )
# if lucky_number < 50:
#     print(f"you will have a bad day! your unlucky number is: {lucky_number}")
# else:
#     print(f"you will have a great day! your lucky number is: {lucky_number}")

# fortune_number = random.randint(1,3)




# fav_movies = ["Avengers","Black adam","Starwars"]

# print(fav_movies[2])

# fav_numbers = [2,7,9]

# print(fav_numbers[0])


# print(len(fav_movies))
# fav_movies.append("Iron man")

# print(len(fav_movies))
# print(fav_movies)

# fav_movies.insert(1,"Batman")
# print(fav_movies)

# del(fav_movies[2])
# print(fav_movies)

# del(fav_movies[1])
# del(fav_movies[1])
# del(fav_movies[1])
# print(fav_movies)


# for number in range(100):
#     print(number)
    
# fav_movies = ["Avengers","Black adam","Starwars"]

# for movie in fav_movies:
#     print(movie)


# for number in range(40):
#     print((number + 1) * 2)

# cats = {"kismo":1, "Jane":6, "Tom":14}

# cats["wilson"] = 2

# del (cats["Tom"])
# len(cats)

# print(cats)

# people = {1:True, 2:False, 3:False}

# print(people)


# text = " Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

# # print(text.split())

# word_count ={}

# for word in text.lower().split():
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# print(word_count)





# def bark():
#     print("Woof woof!")
#     print("I'm a dog")

# for x in range(100):
#     bark()


# def hello(name):
#     print(f"Hello {name}!")

# hello("nick")

# def add_numbers (num1,num2):
#     print(num1 + num2)

# add_numbers(4,8)


# def dog_info(name,age):
#     print(f"this dog's name is {name} and it's {age} years old.")

# dog_info("kismo", 5)


def uppercase(text):
    return text.upper()

    
print(uppercase("caps plz"))

names = ["nick","jane","sarah"]

for name in names:
    print(uppercase(name))
