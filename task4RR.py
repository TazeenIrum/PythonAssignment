print "ROUND ROBIN"
def RR(number,process_queue):
	waiting_queue=[]
	ready_queue=[]
        loop = number
	total = 0	
	temp = None
	from operator import itemgetter
	waiting_queue.sort(key = itemgetter('wait'))	
        while(loop):

		if(len(process_queue) != 0):
			if(process_queue[0]['arrive'] <= total):
				ready_queue += [process_queue[0]]
        return
def GetProcessNumber():
	
	print("Enter number of processes: ")
	return input()
def GetUserInput(number,process_queue):
	
	num1 = 0
	loop = 0

	while(num1 < number):
		process = {}
		process['name']=raw_input ("Enter process Name : ")
		process['arrive']=input ("Enter process arrival Time : ")
		process['burst']=input ("Enter process Burst Time : ")
		process_queue.append(process)
		num1 = num1+1
	return
	
number = GetProcessNumber()

process_queue = []
GetUserInput(number,process_queue)
RR(number,process_queue)
