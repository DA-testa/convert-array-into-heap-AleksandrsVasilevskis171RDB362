# python3
from collections import deque
import heapq

swaps = []

def build_heap(data):
    count = 0
    

    dataLenth = len(data)
    
    check = False
    
    while(check ==False):
        i = dataLenth - 1
        check = True
        while (i >= 0):

            left = 2*i+1
            right = 2*i+2

            if left > dataLenth-1 and right > dataLenth-1:

                pass
            elif left <= dataLenth-1 and right > dataLenth-1:
                x = data[i]
                y = data[left]
                check = False
                if x > y:
                    data[i] = y
                    data[left] = x
                    count= count+1
                    string = str(i)+" "+str(left)
                   # print(count)

                    swaps.append(string)
                pass
                

            elif left <= dataLenth-1 and right <= dataLenth-1:
               
                x = data[i]
                y = data[left]
                z = data[right]

                if x > y and y<z:
                    check = False
                    data[i] = y
                    data[left] = x
                    count =count+1
                    string = str(i)+" "+str(left)
                    #print(count)
                    swaps.append(string)
                    pass
                elif x > z and z < y:
                    check = False
                    data[i] = z
                    data[right] = x
                    count=count+1
                    string = str(i)+" "+str(right)
                    #print(count)
                    swaps.append(string)
                pass

            i=i-1
    swaps.insert(0,str(count))
    
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    
    #return data
    
    return swaps


def main(): 
    #print("hi")
    x = 3 
    #print("hi1")
    y =[9,8,7,6,5,4,3,2,1]
    #print("hi2")
    #build_heap(y)
   # print("hi3")
    
    #print(listArray)

    check =input()
    for i in check:
        if i == "I":
            n = int(input())
            data = list(map(int, input().split()))
            listArray=build_heap(data)
            x=' '.join(listArray)
            print(x)

        elif i == "F":
             url = r"C:\Users\ReFoxiK\Downloads\convert-array-into-heap-AleksandrsVasilevskis171RDB362-main\convert-array-into-heap-AleksandrsVasilevskis171RDB362-main\tests\04"
             f = open(url)
             readFileArray = f.read().splitlines()
             elementCount=int(readFileArray[0])
             arrList = readFileArray[1]
             arrList = arrList.split()
             arrListInt = []
             for i in arrList:
                arrListInt.append(int(i)) 

             build_heap(arrListInt)
        else:
            print("ERROR")
    

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
