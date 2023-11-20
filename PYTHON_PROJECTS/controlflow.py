total =22
discount1=1
discount2=2
if total > 10 and total<22:
    print("Total is greater than 10")
    total=total-discount1
elif total<=22:
    print("Total is greater than 22")
    total-=discount2
else:
    print("Total is less than 10")
print("Total:" + str(total))

