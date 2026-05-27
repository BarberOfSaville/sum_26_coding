#7-8: Deli/ 7-9: No Pastrami

sandwich_orders = ["tuna", "salami", "pastrami", "blt", "grilled cheese", 
                   "pastrami", "marmalade", "pastrami", "pastrami"]
finished_orders = []

print("Welcome to Shirley's Sandwiches!")
print("Heads up-- we are all out of pastrami today! Sorry!")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
    print("Again, we have no pastrami! Sorry folks.")

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print("I'm making the " + current_order + " sandwich now!")
    finished_orders.append(current_order)

print("Whew! I just made these sandwiches:")
for order in finished_orders:
    print("\tA " + order + " sandwich!")
