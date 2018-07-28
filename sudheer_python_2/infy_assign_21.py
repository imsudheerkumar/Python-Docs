furniture=['sofa set','dining table','tv stand','cupboard']
cost=['20000','8500','4599','13920']
user_furniture=input("enter furniture you want :")
quantity=int(input("enter quantity :"))
if user_furniture in furniture:
    x=furniture.count(user_furniture)
    print(x)
    bill_ammount=cost*quantity
    print(bill_ammount)
else:
    print("enter correct quantity and furniture")
