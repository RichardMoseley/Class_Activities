# # Number Chain

# Chain up the numbers

# ## Instructions
run = "y"
# * Using a while loop, ask the user "How many numbers?", then print out a chain of ascending numbers, starting at 0.
while run == "y":
    howMany = input("Please tell me what to count to!: ")
    for i in range(int(howMany)):
        print(i)
    run = input("Press 'Y' if you'd like to run again  ")
#   * If "y", restart the process, starting at 0 again.

#   * If "n", exit the chain.

# ## Bonus

# * Rather than just displaying numbers constantly starting at 0, have the numbers begin at the end of the previous chain.
