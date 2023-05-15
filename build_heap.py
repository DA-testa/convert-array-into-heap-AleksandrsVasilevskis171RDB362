# python3
from collections import deque
from distutils.command.check import check
import heapq
from this import d
#kkk



def build_heap ( data, lenth):
    swops = []
    count = 0
    
    i = 0
    last_peak = 0
    check = False
    
    while i <= lenth-1:
        left = 2*i+1
        right = 2*i+2    
        if left == lenth-1:
            
            last_peak = i
            #print("right",last_peak)
            break

        if  right == lenth-1:
            last_peak = i
            #print ("left",last_peak)
            break
        i=i+1

    
 

    while check == False:

        j = last_peak
        check = True
        while j >= 0:
             
            if lenth%2 == 0:
                if j == last_peak:
                    if int(data[j]) > int(data[2*j+1]):
                        temp = data[j]
                        data[j] = data[2*j+1]
                        data[2*j+1] = temp
                        count = count +1
                        check = False
                        swops.append(j)
                        swops.append(2*j+1)
                else:
                    if int(data[j]) > int(data[2*j+1]) or int(data[j]) > int(data[2*j+2]) :
  
                        if int(data[2*j+1]) > int(data[2*j+2]):
                            temp = data[j]
                            data[j] = data[2*j+2]
                            data[2*j+2] = temp
                            count = count +1
                            swops.append(j)
                            swops.append(2*j+2)
                            check = False
                        elif int(data[2*j+2]) > int(data[2*j+1]):
                            temp = data[j]
                            data[j] = data[2*j+1]
                            data[2*j+1] = temp
                            count = count +1
                            swops.append(j)
                            swops.append(2*j+1)
                            check = False
                        elif int(data[2*j+2]) == int(data[2*j+1]):
                            temp = data[j]
                            data[j] = data[2*j+1]
                            data[2*j+1] = temp
                            count = count +1
                            swops.append(j)
                            swops.append(2*j+1)
                            check = False
                            
                        


                
            else:

                if int(data[j]) > int(data[2*j+1]) or int(data[j]) > int(data[2*j+2]) :
  
                    if int(data[2*j+1]) > int(data[2*j+2]):
                        temp = data[j]
                        data[j] = data[2*j+2]
                        data[2*j+2] = temp
                        count = count +1
                        swops.append(j)
                        swops.append(2*j+2)
                        check = False

                        pass
                    elif int(data[2*j+2]) > int(data[2*j+1]):
                        temp = data[j]
                        data[j] = data[2*j+1]
                        data[2*j+1] = temp
                        count = count +1
                        swops.append(j)
                        swops.append(2*j+1)
                        check = False
                    elif int(data[2*j+2]) == int(data[2*j+1]):
                        temp = data[j]
                        data[j] = data[2*j+1]
                        data[2*j+1] = temp
                        count = count +1
                        swops.append(j)
                        swops.append(2*j+1)
                        check = False
                        
            j = j - 1

    swops.insert(0,count)
    #print (swops)   
    #print (data)   

    return swops

       
    


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
        if i[0] == "I":
            n = int(input())
            data = list(map(int, input().split()))
            swops = build_heap(data,n)
            print(swops[0])
            i = 1
            while i<len(swops)-1:
                print (swops[i],swops[i+1]
                i = i + 1
            #listArray=build_heap(data,n)
            #x=' '.join(listArray)
            

        elif i[0] == "F":
             url = r"tests/04"
             f = open(url)
             readFileArray = f.read().splitlines()
             elementCount=int(readFileArray[0])
             arrList = readFileArray[1]
             arrList = arrList.split()
             arrListInt = []
             for i in arrList:
                arrListInt.append(int(i)) 

             swops = build_heap(arrListInt,elementCount )
             print(swops[0])
             i = 1
             while i<len(swops)-1:        
              print (swops[i],swops[i+1])
              i = i + 1
        else:
            print("ERROR")
    

    # checks if lenght of data is the same as the said lenght
    

    # calls function to assess the data 
    # and give back all swaps
    

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    
    


if __name__ == "__main__":
    main()
