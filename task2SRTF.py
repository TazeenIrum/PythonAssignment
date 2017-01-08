print "SHORTEST JOB FIRST"
def SRTF(number,process_queue):
	
	total_time = 0
	i = number
	ready_queue = []
	from operator import itemgetter
	process_queue.sort(key = itemgetter('arrive'))
	temp = process_queue[0]
	del process_queue[0]
	total_time = temp['arrive']
	
	while(i):
		if(len(process_queue) != 0):
			if(process_queue[0]['arrive'] <= total_time):
				ready_queue += [process_queue[0]]
				del process_queue[0]
			
		if(len(ready_queue) != 0):
			ready_queue.sort(key = itemgetter('burst'))

		if(len(ready_queue) != 0 ):
			if(temp['burst'] > ready_queue[0]['burst']):
				ready_burst += [temp]
				temp = ready_queue[0]
				del ready_queue[0]
		
		temp['burst'] -= 1
		total_time += 1
		if(temp['burst'] == 0):
			print "Process %s Total Turn Around Time Is : %d and Waiting Time Is : %d" % (temp['name'],total_time,total_time-(temp['arrive']))
			i = i - 1
			if(len(ready_queue) != 0):
				temp = ready_queue[0]
				del ready_queue[0]

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
SRTF(number,process_queue)
