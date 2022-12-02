import datetime

vandaag_datum = datetime.date.today()

jaar = int(input("geef hier het jaar aan:\n"))
maand = int(input("geef hier de maand aan:\n"))
dag = int(input("geef hier de dag aan:\n"))

datum = datetime.date(jaar, maand, dag)
vandaag_datum = datetime.date.today()


delta = datum - vandaag_datum
print("dit is het verschil in dagen ", delta.days)