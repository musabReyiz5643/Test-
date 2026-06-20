def controlling_system(no, status):
    if no == 4 or status == "string-4-status-error":
        print("this can be create a high problem in system !")
    elif no == 5 or status == "string-5-status-error":
        print("this can be create a middle problem in system !")
    else:
        print("there is no problem in the system")

controlling_system(4, "string-4-status-error") # Testing 
controlling_system(5, "string-4-status-error") # Testing-2
controlling_system(6, "string-6-status-error") # Testing-3 