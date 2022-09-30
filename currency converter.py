with open("currencyData.txt") as f:
    lines = f.readlines()

curr = {}
for line in lines:
    parsed = line.split("\t")
    # print(parsed)
    curr[parsed[0]] = parsed[1]

print(curr)
amt = int(input("Enter the amount: "))
print("Enter the amount you want to convert the amount to? Available Options:\n")

for i in curr.keys():
    print(i)

currency = input("Enter the currency: ")

print(f"{amt} INR is {amt * float(curr[currency])} {currency}")


##I have attached the currencyData.txt file in the comment box. Use the data from the same txt to solve the issue.
