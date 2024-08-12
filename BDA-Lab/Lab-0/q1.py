from time import sleep

lst = [23, 35, 4, 53, 1, 77, 9, 4, 0, 33]

underline = "\033[4m{text}\033[0m"

def display(lst, step, pos=-1):
    print(f"Step {step} --->", end=" ")
    n = len(lst)
    for i in range(n):
        if i != pos:
            print(lst[i], end=" ")
        else:
            print(underline.format(text=lst[i]), end=" ")
    print()
    return

def bubble_sort(lst):
    lst = lst.copy()
    n = len(lst)
    highlight = -1
    for i in range(n-1):
        for j in range(n-1-i):
            display(lst, i, highlight)
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                highlight = j+1
            else:
                highlight = -1
    return lst

def selection_sort(lst):
    lst = lst.copy()
    n = len(lst)
    for i in range(n-1):
        pos = i
        for j in range(i+1, n):
            if lst[j] < lst[pos]:
                pos = j
        if i != pos:
            lst[i], lst[pos] = lst[pos], lst[i]
    return lst

print(bubble_sort(lst))
print(selection_sort(lst))
