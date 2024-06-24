p1_name, p1_price = "Wheat", 20.05
p2_name, p2_price = "pan cake", 15.00
p3_name, p3_price = "dairy milk", 5.00
company_name = "D mart"
company_adress = "humnabad ring road"
company_city = "kalaburagi"
Message = "Thank you for shopping with us,visit again"
print("*"*50)
print("\t Product Name \t Product Price")
print("\t{}\t\t${}".format(p1_name.title(),p1_price))
print("\t{}\t\t${}".format(p2_name.title(),p2_price))
print("\t{}\t\t${}".format(p3_name.title(),p3_price))
print("="*50)
print("\t\t\t Total")
total = p1_price + p2_price + p3_price
print("\t\t\t${}".format(total))
print("="*50)
print("\n\t{}\n".format(Message))
print("*"*50)
