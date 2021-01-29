pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee",
            "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
customer_pies = []
cus_con = "y"
while cus_con == "y":
    # display the pies
    for x in range(len(pie_list)):
        print(f"[{x}] {pie_list[x]}")
    # select the pies
    for i in range(len(pie_list)):
        cus_pie_pick = int(input("Pick a Pie! (number): "))
        customer_pies.append(pie_list[cus_pie_pick])
        print(
            f"Great! We'll have that {str(pie_list[cus_pie_pick])} pie right out!")
        # print selected pies

        print(customer_pies)


# ask the user if they'd like to continue //Not sure my error here, ask in office hours
        cus_con = input("Would you like to continue?(y/n): ")
# print all customer pies
print(customer_pies)
