my_list = ['name', 'age', '1', '19']


def list_reversed():
    mylist1 = my_list[0:len(my_list)//2]
    mylist2 = my_list[len(my_list)//2: len(my_list)]
    mylist1 = mylist1[::-1]
    for i in mylist2[::-1]:
        print(i)
        mylist1.append(i)
    print(mylist1)

list_reversed()