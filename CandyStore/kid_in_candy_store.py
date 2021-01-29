# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options
        # Class perfered option **BUGGED
# for candy in candy_list:
#     print(f"[{candy.index(candy)}] {candy}")
    # Working Solution
for x in range(len(candy_list)):
    print(f"[{x}] {candy_list[x]}")
# Create a loop for number of candy allowances
for i in range(allowance):
    user_candy = int(input("Pick a candy! (number): "))
    candy_cart.append(candy_list[user_candy])

for candy in candy_cart:
    print(candy)