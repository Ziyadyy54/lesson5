marketcost =float(input("what price did you buy it "))
sellingat =float(input("what price did you sell it "))
if marketcost<sellingat:
    profit=sellingat-marketcost
    print("you got a profit of",profit)
else:
    loss=sellingat-marketcost
    print("you got a loss",loss)