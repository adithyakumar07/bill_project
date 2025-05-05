iPHONE_16_mobile_cost =90000

SGST = 18 / 100
CGST = 18 / 100


print("------- We are selling iPhone mobiles --------\n")
print("-------Each mobile cost is 90000 INR ---------------\n")

required_items = int(input("No. of required items: "))
 
# Apply discount based on quantity
if 2 <= required_items <= 5:
    discount = 9 / 100
elif 6 <= required_items <= 10:
    discount = 19 / 100
elif 11 <= required_items <= 20:
    discount = 19 / 100
elif 21 <= required_items <= 40:
    discount = 24 / 100
elif required_items >= 41:
    discount = 29 / 100
else:
    discount =  2 / 100

iPhone_total_cost = required_items * iPHONE_16_mobile_cost
iPhone_SGST = iPHONE_16_mobile_cost * SGST
iPhone_CGST = iPHONE_16_mobile_cost * CGST
iPhone_discount_amount = iPHONE_16_mobile_cost * discount

#total_cost
total_cost = iPHONE_16_mobile_cost + iPhone_SGST + iPhone_CGST - iPhone_discount_amount

# Output
print("\n------------ Billing Summary --------------------")
print("     Total mobile Cost	: ₹",iPhone_total_cost)
print("     SGST (18%)		: ₹",iPhone_SGST)
print("     CGST (18%)		: ₹",iPhone_CGST)
print("     Discount ({}%)	:{}".format(int(discount*100),iPhone_discount_amount ))
print("-------------------------------------------------")
print("     Total Payable Amount     : ₹",total_cost)
print("-------------------------------------------------")
print(".<.<.<    THANK_YOU AND VISIT_AGAIN    >.>.>.")