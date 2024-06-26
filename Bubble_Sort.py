def bubble_sort(a):
    # Outer loop: controls the number of passes
           # range(star,stop,step)
    for x in range(len(a)-1,0,-1):
        # Inner loop: compares adjacent elements
        for j in range(x):
            if a[j]>a[j+1]:
                # Swap if elements are in the wrong order
                a[j],a[j+1]=a[j+1],a[j]


list1=[6,3,1,5,9,8]
bubble_sort(list1)
print(list1)

list2=[2,3,5,39,11,8,9,166,45,23]
bubble_sort(list2)
print(list2)

list3=[1,2,3,4,5,6,7,8,9,10]
bubble_sort(list3)
print(list3)

list4=[10,9,8,7,6,5,4,3,2,1]
bubble_sort(list4)
print(list4)

list5=[4]
bubble_sort(list5)
print(list5)