def FCFS(number,process_queue):


	
	total = 0
	loop = 0
	inloop = 0
	from operator import itemgetter
	process_queue.sort(key = itemgetter('arrive'))
	while(loop < number):
		if loop == 0:
			total = total + process_queue[loop]['arrive'] + process_queue[loop]['burst']
		elif total > process_queue[loop]['arrive']:
			total = total + process_queue[loop]['burst']
		else:
			total = process_queue[loop]['arrive']  + process_queue[loop]['burst']
			
		print "Process %s Takes Total Time: %d" % (process_queue[loop]['name'],total)
		loop = loop+1	

	
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
FCFS(number,process_queue)
