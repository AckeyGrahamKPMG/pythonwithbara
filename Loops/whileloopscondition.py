# build a for loop that counts to 1 to 5 then stops

count = 0  # change the number for the initization of the count to 0 to start counting from 0 instead of 1
while count <= 10:  # extend the count
    print(count)
    count += 2  # change the increment to 2 to count by 2s instead of 1s


# make the loop more dynamic with input and then checked.
number = int(input("Enter a number to count to: "))
count = 0
while count <= number:
    print(count)
    count += 1


answer = ""

while answer.lower() != "yes":
    answer = input("Do you want to stop the loop? (yes/no): ")
    if answer.lower() != "yes":
        print("The loop continues...")
    else:
        print("The loop has stopped.")
