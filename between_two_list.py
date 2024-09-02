l1=[1,7,8,90,56,8,9,4,3]
l2=[4,5,7,67,89]
l3=list(set(l1) & set(l2))
print("common elements are:",l3)
l4=list(set(l1) - set(l2))
print("deff are :",l4)
l5=list(set(l1) | set(l2))
print("union is :",l5)
l6=list(set(l1) ^ set(l2))
print("Symmetric diff is :",l6)