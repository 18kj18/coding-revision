import statistics; print(statistics.median([4, 5, 9, 8, 10, 17, 99, 77]))

list = [4, 5, 9, 8, 10, 17, 99, 77]
list.sort()

#is length even?
if len(list) % 2 == 0:
    middle1 = list[int((len(list)-1)/2)]
    middle2 = list[int(len(list)/2)]
    median = (middle1 + middle2)/2
    print(median)
else:
    median = list[int((len(list)-1)/2)]
    print(median)