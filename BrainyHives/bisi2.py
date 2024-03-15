#this code shows that both of the criteria must be met and then she decides

#Defining the suitors and their titles and status
suitors = [
{"name": "David", "financial Status": "Rich", "church": "JW"},
{"name": "Joshua", "financial Status": "Poor", "church":"JW"},
{"name": "Peter", "financial Status": "Poor", "church": "Lutheran Church"}
]

FineGirlName = str(input("what is your name?\n"))

#Accessing attributes of the suitors
# 0 for David, 1 for Joshua and 2 for Peter, this is as a result of thier index numbers
suitorFinancialStatus = suitors[2]["financial Status"]
suitorChurch = suitors[2]["church"]

#checking conditions based on attributes
if (suitorFinancialStatus == "Rich" and suitorChurch == "JW"):
    print("I", FineGirlName, "is available")
else:
    print("I", FineGirlName, "is unavailable")
