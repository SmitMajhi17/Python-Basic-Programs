print("=== EXPENSE TRACKER ===")
budget=int(input("Enter your budget :"))
n=int(input("How many expenses ? :"))
amount=[]
for i in range(n):
    exp=str(input(f"Expense {i+1}:"))
    amt=int(input("Amount :"))
    amount.append(amt)
s=sum(amount)
m1=max(amount)
m2=min(amount)
avg=s/n
print("===SUMMARY===")
print("Total spent :",s)
print("Highest expense :",m1)
print("Lowest expense :",m2)
print("Average expense :",avg)
if s>budget :
    print("Budget exceeded by :", s-budget)
else :
    print("Remaining Budget :", budget-s)
per=(s/budget)*100
print("Budget % Used :" ,per)
