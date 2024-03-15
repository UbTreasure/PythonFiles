#Defining the suitors and their titles and status
suitors = [
{"name": "David", "financial Status": "Rich", "church": "JW"},
{"name": "Joshua", "financial Status": "Poor", "church":"JW"},
{"name": "Peter", "financial Status": "Poor", "church": "Lutheran Church"}
]

FineGirlName = str(input("what is your name?\n"))

#Accessing attributes of the suitors
# 0 for David, 1 for Joshua and 2 for Peter, this is as a result of thier index numbers
suitorFinancialStatus = suitors[1]["financial Status"]
suitorChurch = suitors[1]["church"]

#Printing the financial status and church to confirm
#print(f"The first suitors financial status is: {suitorFinancialStatus}")
#print(f"The first suitors church is {suitorChurch}")

#checking conditions based on attributes
if (suitorFinancialStatus == "Rich" or suitorChurch == "JW"):
    print("I", FineGirlName, "is available")
else:
    print("I", FineGirlName, "is unavailable")
