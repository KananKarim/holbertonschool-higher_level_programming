class MyList(list):
    def print_sorted(self):
        print(sorted(self))
        

l1 = MyList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.print_sorted()