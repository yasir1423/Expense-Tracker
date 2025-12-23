import csv
import os
filename="expenses.csv"
#function to add an expense
def add_expense():
    amount=float(input("Enter amount:"))
    category=input("Enter category(Food,travel,bill,etc):")
    #saving in csv
    with open(filename,"a") as f:
        writer=csv.writer(f)
        writer.writerow([amount,category])
    print("Expense added successfully! ")
#function to load all expenses
def load_expenses():
    expenses=[]
    #if file does not exist, create it.
    if not os.path.exists(filename):
        open(filename,"w").close()
    with open(filename,"r") as file:
        reader=csv.reader(file)
        for row in reader:
            if row:
                amount=float(row[0])
                category=row[1]
            expenses.append({"amount":amount,"category":category})
    return expenses
#function to show total and category
def show_total():
    expenses=load_expenses()
    if not expenses:
        print("No Expenses recorded yet")
        return
    total_monthly=0
    category_totals={}#Dictionary for category wise totals
    #calculate totals
    for expense in expenses:
        amount=expense["amount"]
        category=expense["category"]
        total_monthly+=amount
        if category in category_totals:
            category_totals[category]+=amount
        else:
            category_totals[category]=amount
    print("===TOTAL MONTHLY SUMMARY===")
    print(f"Total monthly expense:{total_monthly}")
    print("CATEGORY WISE TOTAL")
    for category, total in category_totals.items():
        print(f"{category}:{total}")
    print()
#Main Menu
def main():
    while True:
        print("===EXPENSE MANAGER===")
        print("1.Add expense.")
        print("2.Show total monthly and category totals.")
        print("3.Exit")
        choice=input("Enter your choice(1-3):")
        if choice=='1':
            add_expense()
        elif choice=='2':
            show_total()
        elif choice=='3':
            print("Exiting the program......")
            break
        else:
            print("Invalid choice.Try again.....")
main()



