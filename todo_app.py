

# To-Do List

tasks = []

print("Welocm to the To-Do List App!\n ")

while True:
    print("------------------")
    print("Choose an option: ")
    print("1 . Add task")
    print("2 . View tasks")
    print("3 . Delete task")
    print("4 . Exit\n")
    print("------------------")

    choice = input("Enter your choice (1-4) :")

    if choice == "1":

      value = input("Enter your task : ")
      tasks.append(value)

      print("Task Added!")


    elif choice == "2":
       if not tasks:
          print("No taskes yet ")  
       else:
          print("Your Taskes: ")
          i = 1
          for data in tasks:
             print(i,data) 
             i += 1


    elif choice == "3":
       if not tasks:
          print("No Tasks to delete : ")   
       else:
          i = 1
          print("Your tasks : ")
          for data in tasks:
             print(i , data)
             i += 1   

          task_number = input("Enter Task number to delete :")
          task_number = int(task_number)  

          if task_number >= 1 and task_number <= len(tasks):
             deleted = tasks.pop(task_number - 1 )
             print(f"deleted Task : {deleted}")
          
                

          

     









