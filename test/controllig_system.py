def controlling_system(no, status):
    if no == 4 or status == "string-4-status-error":
        print("this can be create a high problem in system !")
    elif no == 5 or status == "string-5-status-error":
        print("this can be create a middle problem in system !")
    else:
        print("there is no problem in the system")