import listener
import time

#main program for the mailcow listener
#used to set a time to when the listener should stop,
#to execute the last entries after the last execute of the
#listener
#and to delete all entries of the log-file to save
#memory space
class mailManager:
    #create a new instance of the listener
    #the format is: (execute,hour,minute,loop_active)
    #was the program started from the mailManager(set it always to True)
    #the hours of when to stop the listener
    #the minutes of when to stop the listener
    #the status of the variable to start the loop of the listener
    listenerInstance = listener.listener(True, 15, 52, True)
    
    #stop the listener
    listenerInstance.stop_listener()
    #just for testing purposes
    print(listenerInstance.last_line)

