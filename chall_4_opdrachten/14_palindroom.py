my_str = input("geef mij een woord: ")

my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
   print("dit woord is wel een palindroom")
else:
   print("dit woord is niet een palindroom")