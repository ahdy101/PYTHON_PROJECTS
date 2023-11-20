str="looping"
for item in str:
    print(item)

for idx, i in enumerate(str):
    print(idx, i)

count=0

while count<len(str):
    print("i like", str[count])
    count +=1
