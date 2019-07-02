from operator import itemgetter
from itertools import *

def main():

    data1=[01,02,03,10,11,100,9999]
    data2=[0001,0002,0003,0010,0011,0100,9999]
    data3=['image_0001','image_0002','image_0003','image_0010','image_0011','image_0011-2','image_0011-3','image_0100','image_9999']

    list1 = []
    #for k, g in groupby(enumerate(data1), lambda (i,x):i-x):
    for k, g in groupby(enumerate(data1), lambda x:x[0]-x[1]):
        list1.append(map(itemgetter(1), g))
    print 'data1'
    print list1

    list2 = []
    #for k, g in groupby(enumerate(data2), lambda (i,x):i-x):
    for k, g in groupby(enumerate(data2), lambda x:x[0]-x[1]):
        list2.append(map(itemgetter(1), g))
    print '\ndata2'
    print list2


if __name__ == "__main__":
    main()
