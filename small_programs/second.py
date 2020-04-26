import random

user_chnaces=int(input("ENter the chnaces: "))
magic_numbers=[random.randint(0,9),random.randint(0,9)]

def ask_user_and_check_number():
    user_numbers=int(input("ENter the no: "))
    if (user_numbers) in magic_numbers:
        return "You got it"
    if (user_numbers) not in magic_numbers:
        return "You did not get it"
        

  
def run_program_x_times(user_chnaces):
    for c in range(user_chnaces):
        print("This is attempt {}".format(c))
        ask_user_and_check_number()

        message=ask_user_and_check_number()
        print(message)
       


run_program_x_times(user_chnaces)


