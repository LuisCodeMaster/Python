print("Welcome to conversion currency!!")
ch = (input("choose conversion:\n 1 - R$ -> USD\n 2 - USD -> R$\n 3 - USD -> EU"))
if ch == 1:
    real = (float(input("how much money do you have in your wallet?")))
    dollar = real/5.00
    print('With R${}, yoy can buy USD{}'.format(real, dollar))

    
elif ch == 2:

    dollar = (float(input("how much money do you have in your wallet?")))
    real = dollar*5.00
    print('With USD{}, you can buy R${}'.format(dollar, real))
    
else:
    dollar = (float(input("how much money do you have in your wallet?")))
    eu = dollar + 0.54
    print("With USD{}, you can buy EU{}".format(dollar, eu))

