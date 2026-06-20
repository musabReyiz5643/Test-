def controlling_system(no, status):
    if no == 4 and status == "string-4-status-error":
        print("this can be create a high problem in system !")
    else:
        print("there is no problem in the system")
        
controlling_system(4 , "string-4-status-error")