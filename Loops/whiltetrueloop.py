# create a while true loop
# while True:
#     print("This loop will run forever until you stop it.")
#     user_input = input("Type 'stop' to end the loop: ")
#     if user_input.lower() == 'stop':
#         print("Loop has been stopped.")
#         break  # this will exit the loop when the user types 'stop'


while True:
    answer = input("Do you want to continue the loop? (yes/no): ")
    if answer.lower() == "yes":
        break
print("The loop has been stopped.")
