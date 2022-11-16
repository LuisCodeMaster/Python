print("Welcome to our  hire car service!!")
km = int(input('how many km did you run?'))
days = float(input('how many days it was hired?'))
paid = (days * 60) + (km * 0.15)
print('The total to pay is R${:.2f}'.format(paid))
    