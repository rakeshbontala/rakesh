cost_price=int(input())

selling_price=int(input())

if cost_price<selling_price:
    print("Profit")

elif cost_price>selling_price:
    print("Loss")
    
else:
    print("No Profit - No Loss")