def check_baggage(baggage_weight):
    if baggage_weight>=0 and  baggage_weight<=40:
        return "TRUE"
    else:
        return "FALSE"

def check_immigration(expiry_year):
    if expiry_year>=2001 and expiry_year<=2025:
        return "TRUE"
    else:
        return "FALSE"

def check_security(noc_status):
    if noc_status=='valid' or noc_status=='VALID':
       return "TRUE"
    else:
        return "FALSE"

def traveler():
    traveler_id=int(input("enter traveler id :"))
    traveler_name=input("enter traveler name :")
    x=int(input("enter baggage weight :"))
    y=int(input("enter immigration expiry year :"))
    z=input("enter noc status :")
    check_baggage(x)
    check_immigration(y)  
    check_security(z)
    if check_baggage == "TRUE" and check_immigration == "TRUE" and check_security == "TRUE":
        print(traveler_id)
        print(traveler_name)
        print("Allow Traveler to fly")
        return
    else:
        print(traveler_id)
        print(traveler_name)
        print("Detain Traveler to recheck")



traveler()
        
    
