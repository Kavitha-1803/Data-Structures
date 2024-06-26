class InvalidOperationException(Exception):
    pass

class studentRecord:
    def __init__(self,i,Name):
        self.studentId=i
        self.studentName=Name

    def get_student_id(self):
        return self.studentId

    def set_student_id(self,i):
        self.studentId=i

    def __str__(self):
        return str(self.studentId)+" "+self.studentName

class HashTable:
    def __init__(self,tableSize=11):
        self.m=tableSize
        self.array=[None]*self.m
        self.n=0

    def hash1(self,key):
        return (key % self.m)

    def insert(self,newRecord):
        #fetches the ID of the student, which is the stored in the variable key
        key=newRecord.get_student_id()
        h=self.hash1(key)
        # Initial location is set to the hash value
        location=h

        # Start probing to find an empty slot
        for i in range(1,self.m):
            # If the slot is empty or contains a deleted record
            if self.array[location] is None or self.array[location].get_student_id()==-1:
                self.array[location]=newRecord    # Insert the new record
                self.n+=1
                return

            # If a record with the same key already exists
            if self.array[location].get_student_id==key:
                raise InvalidOperationException    # Raise an exception for duplicate key
            # Move to the next slot (linear probing)
            location=(h +i)%self.m
        print("Table is full : Record can't be inserted ")  # If the table is full, print an error message

    def search(self,key):
        h = self.hash1(key)
        location = h

        for i in range(1, self.m):
            if self.array[location] is None:
                return None

            if self.array[location].get_student_id() == key:
                # If the slot contains the key, return the record found at the current location
                return self.array[location]
            # Move to the next slot (linear probing)
            location = (h + i) % self.m
            # If the loop completes without finding the key, return None
        return None

    def display_table(self):
        for i in range(self.m):
            print("[", end='');
            print(i, end='');
            print("]", end='')

            if self.array[i] is not None and self.array[i].get_student_id() != -1:
                print(self.array[i])
            else:
                print("______")

    def delete(self,key):
        h = self.hash(key)
        location = h

        for i in range(self.m):
            if self.array[location] is None:
                return None

            if self.array[location].get_student_id() == key:
                temp = self.array[location]
                self.array[location].set_student_id(-1)
                self.n -= 1
                return temp
            location = (h + i) % self.m

        return None

size=int(input("Enter initial size of table : "))
table=HashTable(size)

while True:
    print("1.Insert a record")
    print("2.Search a record")
    print("3.Delete a record")
    print("4.Display table")
    print("5.Exit")

    option=int(input("Enter your option  : "))
    if option==1:
        id =int(input("Enter student id: "))
        name=input("Enter student name : ")
        aRecord=studentRecord(id,name)
        table.insert(aRecord)
    elif option==2:
        id = int(input("Enter a key to be searched : "))
        aRecord=table.search(id)
        if aRecord is None:
            print("Key is not found")
        else:
            print(aRecord)
    elif option==3:
        id = int(input("Enter a key to be deleted : "))
        table.delete(id)
    elif option==4:
        table.display_table()
    elif option==5:
        break
    else:
        print("Wrong option")
    print()