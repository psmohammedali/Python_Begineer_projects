import db_helper

def main():
    db_helper.create_table()
    temp = 1
    print("<--- Welcome to Ali's TODO Application, Please Select the required option --->  \n")
    print("1.Add TODO App\n"
          "2.Print the TODO List\n"
          "3.Delete TODO Task\n"
          "4.Exit The TODO Application\n")

    while temp:
        user_op = int(input("Enter the choice (1-4): "))

        if user_op == 1:
            task_enter = str(input("Enter the task: "))
            db_helper.data_entry(task_enter)

        elif user_op == 2:
            db_helper.print_data()

        elif user_op == 3:
            index_delete = int(input("Enter the Task index to be deleted: "))
            db_helper.delete_task(index_delete)

        elif user_op == 4:
            db_helper.closeconection()
            temp = 0

        else:
            print("Please Enter the choice between 1-4 !!!")

if __name__ == "__main__": main()
