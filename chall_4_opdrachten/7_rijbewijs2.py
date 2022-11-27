
# import datetime


# def geboortedatum():
#     datum = input('wat is uw geboortedatum? (YYYY-MM-DD): ')
#     try:
#         Juiste_datum = datetime.datetime.strptime(datum, "%Y-%m-%d")
#         if datum < ("2005-01-01"):
#             print("volgens de wet mag jij voor een motor rijbewijs gaan!")
#         elif datum > ("2005-01-01"):
#             print("volgens de wet mag jij niet voor een motor rijbewijs gaan!")        
#     except ValueError:
#         print("Sorry, dat is niet juist. Probeer het opnieuw!")
#         return geboortedatum()

# print(geboortedatum())
# exit()


import datetime

birthday = (input('Enter your birthday in dd/mm/yyyy format: '))
day, month, year = list(map(int, birthday.split('/')))
birthdate = datetime.date(year, month, day)
today = datetime.date.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
print (age)

if age >= 18:
    print("u mag als u een WA bij u hebt en een motorhelm op hebt, gaan motorrijden")
if age <= 17:
    print("je mag niet motorrijden")