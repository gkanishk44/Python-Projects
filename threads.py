import threading 

barrier = threading.Barrier(4) 

class thread(threading.Thread): 
	def __init__(self, thread_ID, thread_name): 
		threading.Thread.__init__(self) 
		self.thread_ID = thread_ID 
		self.thread_name = thread_name 
	def run(self): 
		print("ThreadID = " + str(self.thread_ID) + ", ThreadName = " +
self.thread_name + "\n") 
		try: 
			barrier = threading.Barrier(4) 
			barrier.wait() 
		except: 
			print("barrier broken") 
thread1 = thread(100, "GFG") 
thread2 = thread(101, "Geeks") 
thread3 = thread(102, "GeeksforGeeks") 

thread1.start() 
thread2.start() 
thread3.start() 

barrier.wait() 

print("Exit") 
