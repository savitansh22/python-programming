def task_manager():
    task_list = []
    is_running = True

    print("--- Welcome to the Task Manager ---")

    while is_running:
        print("\nOptions: [1] Add Task  [2] View Task  [3] Exit  [4] Delete Task")
        choice = int(input("Choose an option: \n"))

        
        if choice == 1:
            task = input("enter your task: \n")
            print(f"task: {task} has been added to your task list.")
            task_list.append(task)
            
        elif choice == 2:
            print (f"your current task is: \n")
            for number, task in enumerate(task_list, 1):
                            print(f"{number}. {task}") 
            
        elif choice  == 3:
            is_running =  False
            print("exiting, Goodbye!!")

        elif choice == 4:
            dlt = int(input("enter the task number you want to delete: \n"))
            deleted_task = task_list.pop(dlt-1)
            print(f"task:{deleted_task} has been deleted from yout taks list. \n")            
        else:
            print("invalid choice")

task_manager()