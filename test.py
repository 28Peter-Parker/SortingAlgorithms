#These first two lines begin the test
import timeit
code_to_test="""

#This program will test your sorting algorithms
import sort as sort

#Access file with test list
f=open('TestFile.txt','r')
List=[]
for line in f:
	line = line.strip() # strip whitespace
	if line: 
		List.append(int(line))

#This is where you will call your sorting algorithms. Comment out the ones you don't want to test.

sort.bubbleSort(List)

#sort.insertionSort(List)

#sort.cocktailSort(List)

"""
#These last three lines allow you to adjust your test. N is the number of runs
N=1
elapsed_time = timeit.timeit(code_to_test, number=N)/N
print(elapsed_time)
