
bill_ammount=int(input("enter bill ammount :"))
cust_id=int(input("enter cust id :"))
if cust_id>=101 and cust_id<=1000:
    if bill_ammount>0:
        if(bill_ammount>0) and (bill_ammount<500):
            discount=bill_ammount*0.99
            print("the ammount after discount :",discount)
        elif bill_ammount>=500 and bill_ammount<1000:
            discount=bill_ammount*0.97
            print("the ammount after discount :",discount)
        elif bill_ammount>=1000:
            discount=bill_ammount*0.05
            res=bill_ammount-discount
            print("the ammount after discount :",res)
    else:
         print("bill ammount should be greater than zero")
else:
    print("cust id should be between 101 and 1000")
