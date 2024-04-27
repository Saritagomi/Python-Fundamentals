a=[2,3,4,55,3,4,55,6,7,4,6,7,5]
listcount=a.count(6)
print("no. of times", listcount)

list  = [1,3,4,5,3,5,5,2,5,6,4,6,4,6]
fre= {}
for item in list:
   if item in fre:
         fre[item] += 1
   else:
         fre[item] = 1
print(fre)

def bubblesort(sim):
    for i in range(0, len(sim)):
        for j in range(len(sim) - 1):
            if (sim[j] > sim[j + 1]):
                temp = sim[j]
                sim[j] = sim[j + 1]
                sim[j + 1] = temp
    return sim
sim = [5, 3, 8, 6, 7, 2]
print("The sorted list is", bubblesort(sim))


