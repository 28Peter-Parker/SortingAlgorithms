def bubbleSort(myList):

    n = len(myList) - 1

    noMoreSwaps = False

    Temp = 0

    while noMoreSwaps == False:

        noMoreSwaps = True

        for j in range(0,n):


            if myList[j] > myList[j+1]:

                Temp = myList[j]

                myList[j] = myList[j+1]

                myList[j+1] = Temp

                noMoreSwaps = False

        
        n = n-1

    return myList
    



def insertionSort(myList):

    maxIndex = len(myList)

    for i in range(1,maxIndex):

        currentValue = myList[i]

        currentPosition = i

        while currentPosition > 0 and myList[currentPosition - 1] > currentValue:

            myList[currentPosition] = myList[currentPosition - 1]

            currentPosition = currentPosition - 1


            myList[currentPosition] = currentValue

    return myList



def cocktailSort(myList):
    

    n = len(myList) 
    swapped = True
    start = 0
    end = n-1
    while  swapped == True: 
  
        
        swapped = False
  
        
        for i in range (start, end): 
            if  myList[i] > myList[i + 1]: 
                myList[i], myList[i + 1]= myList[i + 1], myList[i] 
                swapped = True
  
        
        if (swapped == False): 
            break
  
        
        swapped = False
  
        
        end = end-1
  
        
        for i in range(end-1, start-1, -1): 
            if  myList[i] > myList[i + 1]: 
                myList[i], myList[i + 1] = myList[i + 1], myList[i] 
                swapped = True
  
        
        start = start + 1

    return myList

    



    

    

                
                                   

                

            

            
        



        

        
