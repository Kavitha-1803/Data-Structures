def shell_sort(a):
    h=int(input(("Enter the increment value : ")))
    while h>=1:
        for i in range(h,len(a)):
            temp=a[i]
            j=i-h
            # Shift elements that are greater than temp to the right by the gap h
            while j>=0 and a[j]>temp:
                a[j+h]=a[j]
                j=j-h
            # Place temp in its correct position
            a[j+h]=temp
        # Reduce the gap for the next pass
        h=h-2


list1=[65,73,21,90,6,239,3,35,1,15,5,9,8,23,12,5,7,2,19,34]
shell_sort(list1)
print(list1)