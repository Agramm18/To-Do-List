class to_do_List:
    def __init__(self):
        self.toDo = []

    def getList(self):
        while True:
            try:
                to_do_status = input("Do you have open To-Dos Y/N: ")
                if to_do_status == "Y":
                    to_do_count = int(input("How many open To-Dos do you have: "))
                    for i in range(to_do_count):
                        to_dos = input("Please type in your to dos: ")
                        self.toDo.append(to_dos)
                        ', '.join(self.toDo)
                        print(f"Your To Dos are: {self.toDo}")
                    break

                elif to_do_status.lower() == "N":
                    print("Okay thank you for using this programm")
                break

            except Exception as e:
                print("Invalid input please follow the instructions to continue")
                print(f"Error: {e}")


    def getRemoveToDo(self):
        while True:
            try:
                to_do_status = input("have you already worked through your to-dos Y/N: ")
                if to_do_status == "Y":
                    clear_status = input("Please type in all if you have done all your to dos or n if you have not"
                                         " done all of your to dos: ")

                    if clear_status == "all":
                        self.toDo.clear()
                        print(f"Your To-Dos are: {self.toDo}")
                        print("Well done you have done all your To-Dos")
                        print("Thank you for using this programm")
                        print("Have a nice day")
                        break

                    elif clear_status == "n":
                        done_to_dos_count = int(input("How many To-Dos do you have already done: "))
                        done_to_dos = input("What To-Dos do you have already done: ")
                        for i in range(done_to_dos_count):
                            self.toDo.remove(done_to_dos)
                            print(f"Your To-Do list is: {self.toDo}")
                            break

                elif to_do_status == "N":
                    print("Okay then do your To-Dos")
                    print("Have fun and a nice day")
                    break

            except Exception as e:
                print("Invalid input please follow the instructions to continue")
                print(f"Error: {e}")

list = to_do_List()
list.getList()
list.getRemoveToDo()