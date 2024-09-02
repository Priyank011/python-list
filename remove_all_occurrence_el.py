# remove all occurrence of an element in a list
Number=["a","b","c","d","e",1,2,6,9,"a","b","c",1,2,3,6,8,9]
Number= [x for x in Number if x!=2]
Number= [x for x in Number if x!="a"]
print(Number)