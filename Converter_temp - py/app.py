
print("Welcome to your converter temp!!")
ch = int(input("Choose the conversion : \n 1 - F° -> C° \n 2 - C° -> F°\n           :"))
if ch == 1:
    c = float(input('Put the temperature on C°:'))
    f = int(((c * 9) /5) + 32)
    print('The temperature of {}°C is equals to {} F°'.format(c, f))
    print("Thank you for using our product!!")

else:
    f = float(input('Put the temperature on F°:'))
    c = ((f - 32)/9) * 5 
    print('The temperature of {}°F is equals to {} C°'.format(f, c))
    print("Thank you for using our product!!")

    
    
    
      