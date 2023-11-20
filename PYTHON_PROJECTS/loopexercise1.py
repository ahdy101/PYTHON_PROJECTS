num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
counter=0
for idx, i in enumerate(num_list):
    print(i)
    if i >45:
        print(idx,i, "Over 45")
        break
    else:
        print(idx,i, "Under 45")
    counter=counter+1
print(counter)
