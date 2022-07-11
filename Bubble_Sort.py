# bubble_sort.py

def bubble_sort(list):
    for i in range(0, len(list) - 1):
        for j in range(0, len(list) - 1 - i): 
            if list[j] > list[j + 1]:   
                list[j], list[j+1] = list[j+1], list[j]
        print("pass", i + 1,": ", list)

xlist = list(eval(input("Enter a random series: ")))
print(xlist)
bubble_sort(xlist)
