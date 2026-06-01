tasks=[]
while True:
    print("a. Add task")
    print("b. View task")
    print("c. delete task")
    print("d. exit")
    op=input("Enter Your choice :").lower()
    if op=="a":
        task=input("Enter the task: ")
        tasks.append(task)
    elif op=="b":
        if not tasks:
            print("No tasks available")
        else:   
            for i, task in enumerate(tasks):
                print(i, task)
    elif op=="c":
        if not tasks:
            print("no tasks to delete")
        else:
            index=int(input("Enter the number of task you want to remove"))
            if index<len(tasks):
                print(tasks.pop(index), " was removed")
            else: 
                print("Invalid option")         
    elif op=="d":
        print("Thank you for Using my program")
        break
    else:
        print("Invalid option")
