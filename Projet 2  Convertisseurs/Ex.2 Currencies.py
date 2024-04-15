
print("CURRENCY CONVERTER")
print("")


currencies = ["EUR to US", "US to EUR"]
currencies[0] = "1 (EUR to US)"
currencies[1] = "2 (US to EUR)"

print(currencies[0])
print(currencies[1])


print("")


exchange_rate1 = 1.0733333
exchange_rate2 = 0.9345794

     
answer=input("Enter the number corresponding to the desired conversion: ")

print("") 

n=input("Enter the amount to convert: ")

if answer == "1":
    print(str(round((float(n)*exchange_rate1),2))+"$")
    
else:
    print(str(round((float(n)*exchange_rate2),2))+"€")

    


            