print "VIRTUAL ROUND ROBIN"
def VRR(number,process_queue):
	waiting_queue=[]
	ready_queue=[]
	auxilary_queue=[]

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
VRR(number,process_queue)
