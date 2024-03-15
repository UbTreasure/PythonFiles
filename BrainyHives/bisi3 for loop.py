suitors = [
{"name": "David", "financial Status": "Rich", "church": "JW"},
{"name": "Joshua", "financial Status": "Poor", "church":"JW"},
{"name": "Peter", "financial Status": "Poor", "church": "Lutheran Church"}
]

FineGirlName = str(input("what is your name?\n"))

#using a for loop to iterate through the suitors
for suitor in suitors:
    suitorFinancialStatus = suitor["financial Status"]
    suitorChurch = suitor["church"]
    suitorname = suitor["name"]

    #checking conditions based on attributes
    if suitorFinancialStatus == "Rich" or suitorChurch == "JW":
        print("I", FineGirlName, "is available to", suitorname)
        break
else:
    print("I", FineGirlName, "is unavailable")