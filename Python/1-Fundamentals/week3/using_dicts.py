state_capitols = {"Washington": "Olympia", "Oregon": "Salem", "California": "Sacramento"}
#print(len(state_capitols))
#print(state_capitols["Washington"])
state_capitols["Washington"] = "Aberdeen" 
state_capitols["Texas"] = "Austin"
print(state_capitols)
del state_capitols["California"]
print(state_capitols)
state_capitols.pop("Oregon")
print(state_capitols)