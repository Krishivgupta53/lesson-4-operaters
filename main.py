#-assignment operater(=)
#STORE THE HARVEST IN KG FROM EACH BAG FROM THE 5 FIELDS
field1=941
field2=26
field3=766
field4=663
field5=67

#---Arthimatic Operators (+,-,*,/)---
total = field1 + field2 + field3 + field4 + field5
average = total /5

print("total harvest         :",total, "kg")
print("average per field     :",average,  "kg")

#Price per kg is 20 rupees
#calculate total earnings
price_per_kg = 20
earnings = total*price_per_kg
print("total eaarnings    : Rs.",earnings)
#---Floor division (//) and modules (%)
#Compare this year's harvest with last year
bags=total//25
leftover =total%25
print("bags     :", bags)
print("leftover rgrains    :",leftover,  "kg")
#---Camperision operators (>,<,==,>=)
last_year=500
print("Better than last year?     ",total >  last_year)
print("same as last year ?  ",total==last_year)
print("as good  ",total>=last_year)

#-----Assignment operators
# a bonus field adds 30 kg to the total
total +=30
print("after bonus crop    ",total, "kg")

# subtract 15 kg seeds for next year
total-=15
print("the crop after seed saving  ",total,"kg")

#final bag count after all adjustments
bags=total//25
print("final bags packed   ",bags)