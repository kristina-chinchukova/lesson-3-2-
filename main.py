my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
long = len(my_list)
account = []
number = 0
while long != 0:
    if my_list[number] >= 0 :
        if my_list[number] > 0 :
            account.append(my_list[number])
        long = long - 1
        number = number + 1
        continue
    break
print(account)
