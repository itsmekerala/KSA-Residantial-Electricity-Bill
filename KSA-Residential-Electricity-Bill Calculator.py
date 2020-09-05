print("SAUDI ELECTRICITY Residantical Bill Calculator")
print("-----------------------------------------------")
 #old bill
#new bill
#new - old = current reading
#add tax amount to taxrate (taxamount / 100 )
taxrate=0.15
olre=int(input("Old Bill Reading(KWH): "))
nere=int(input("New Bill Reading(KWH): "))
currre=nere-olre
print("Current Usage(KWH):",currre),
tariff=currre*0.18
print("Amount Of Usage as per residential Tariff (0.18): ",tariff,"SAR"),
rent=tariff+10
print("Meter Rent(10SAR) ",rent,"SAR"),
tax=rent*taxrate
totaltax=rent+tax
print("Total Invoice amount",totaltax,"SAR"),

input()
