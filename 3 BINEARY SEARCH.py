Arr =[3,554,676,78,66,54]

Sorted_arr = sorted(Arr)
print(Sorted_arr)
def bineary_search(Sorted_arr, query):
    low,high = 0, len(Sorted_arr)-1
    while low <= high:
        mid = (low+ high)//2
        mid_number = Sorted_arr[mid]
        print(low,high, mid )
        if mid_number == query:
            return mid
        elif mid_number > query:
            high = mid- 1
        elif mid_number < query:
            low = mid + 1
    return  -1
print(bineary_search(Sorted_arr,54))