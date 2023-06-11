#User Input On Food Charges
food_charge = float(input("Enter Food Charge:"))
tip_Amt= food_charge * 0.18
tax_Amt= food_charge * 0.0
#Total Charge Calculation
total_charge= food_charge + tip_Amt + tax_Amt

print ("Tip Amount: $ ", format(tip_Amt,".2f"))
print("Sales tax Amount: $ ", format(tax_Amt,".2f"))
print("float charge: $", format(total_charge,".2f"))