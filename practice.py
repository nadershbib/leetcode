




arr = [1,1,1,13,3,3,3,"-",3,3,3,"_","_"]
freq = {}
for num in arr:
    freq[num] = freq.get(num,0) + 1

print(list(freq.keys()))
print(arr.sort())