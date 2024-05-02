#Author: S@nity
#Portions of this code were adapted from a solution found
#on Stack Overflow.




#import for operating system operations 
import os
#import datetime to stop the script at a certain time
import datetime

#Important!: The program tracks the always the last entry
#            of the log in order to use less resources.
#            Also, make sure that the shell scripts have
#            execute permissions.
class listener:
    #create the variable to store the status of the call
    #set it to False by default to prevent errors
    execute = False
    #create the last_line variable to make it callable
    #from the mail-manager
    last_line = ""
    
    def __init__(self, wasCalled, hour, minute, loop_active):
        #was the program called by the manager
        self.execute = wasCalled
        #the hours of when to stop
        self.hour = hour
        #the minutes of when to stop
        self.minute = minute
        #the state of the loop of the listener
        self.loop_active = loop_active
        #start the listener
        self.start_listener()

    def start_listener(self):
        #run the program if the constructor was set properly
        if(self.execute):
            #the selected keyword the program looks out for
            keyword = "removeUserFromAcls?uis="
            #the path where the log is located
            log_path = "log.txt"
            #the script the program has to execute after the
            #keyword was found
            #!IMPORTANT!: Don't forget ./ in front of the string
            #             or else it will not execute!
            script_to_execute = "./test.sh"

            #just a placeholder to check if the last entry changed
            checked = ""

            #run the programm until it is cancled manually
            while self.loop_active:
                
                #refresh the current time after ever round of the loop
                currentTime = datetime.datetime.now()

                #check if the current time is equal to the time entered to stop
                #the program
                if(currentTime.hour == self.hour and currentTime.minute == self.minute):
                    # if so stop the loop
                    break

                #open the log in binary mode and define log as the log
                #binary mode = the program loads the data in bytes,
                #which is easier to manipulate
                with open(log_path, "rb") as log:
                    #look for exceptions
                    try:
                        #sets the search index two entries ahead of the last entry
                        #looks for the end of the file
                        log.seek(-2, os.SEEK_END)
                        #reads through all characters until it arrives at \n
                        #which indicates the beginning of an entry
                        while log.read(1) != b'\n':
                            #and then sets this as the beginning
                            log.seek(-2, os.SEEK_CUR)
            
                    except OSError:
                        #if an error occurs jump back to the beginning of the file
                        log.seek(0)

                    #take the selected text and decode it
                    self.last_line = log.readline().decode()
        
                #check if the last entry even changed
                if(self.last_line != checked):
                    #change the last check to the current check
                    checked = self.last_line
                    #check if the last line contains
                    #the selected keyword
                    if(keyword in self.last_line):
                        os.system(script_to_execute)
        else:
            #alert the user to use the manager to start the listener
            print("Error! Please use the Mail-Manager to run the program!")
    
    #function to stop the loop of the listener
    def stop_listener(self):
        #set the variable to stop the loop of the listener
        self.loop_active = False