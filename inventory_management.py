#Displays the option screen + if user wants to see inventory
def display():
	print("\nOptions:")
	print("0. Exit/Print Output File")
	print("1. Display Inventory")
	print("2. Add Item")
	print("3. Delete Item")
	print("4. Update Item")
	choice=int(input('Please make your choice: '))
	return choice

#gets total from the inventory
def display_total(names,prices,quantities):
	inventory_total= zip(names,prices,quantities)
	for sublist in inventory_total:
		print(sublist)

#allows user to add items to inventory
def add_item(names,prices,quantities):
	names.append(input("Enter name you'd like: "))
	prices.append(float(input("Enter the price: ")))
	quantities.append(int(input("Enter the quantity: ")))
	return names,prices,quantities

#allows user to delete items to inventory
def delete_items(names,prices,quantities):
	item_to_delete=input("Please enter the name of the item you want to delete: ")
	try:
		index=names.index(item_to_delete)
		del names[index]
		del prices[index]
		del quantities[index]
	except ValueError:
		print(f"{item_to_delete} was not found in inventory\n")

#allows user to update price and quantity for items in inventory
def update_item(names,prices,quantities):
	updated_item= input("Enter the name of the item you want to update: ")
	try:
		index= names.index(updated_item)
		choice=input("Enter P for price, and Q for quantity: ")
		if choice== 'P':
			new_price= float(input("Enter new price: "))
			prices[index]=new_price
		elif choice == "Q":
			new_quantity==int(input("Enter new quantity: "))
			quantities[index]=new_quantity
		else:
			print("This is an invalid option")
	except ValueError:
		print(f"{updated_item} was not found in inventory \n")

#main function organizes csv file
def main ():
	current_inventory= open ('inventory.csv', 'r')
	read_inventory= current_inventory.readlines()
	
	for index in range(len(read_inventory)):
		read_inventory[index]=read_inventory[index].rstrip("\n")
	inventory_lines=[]
	for line in read_inventory:
		current=line.split(',')
		inventory_lines.append(current)
	inventory_empty=[]
	for sublist in inventory_lines:
		for item in sublist:
			inventory_empty.append(item)

	names=inventory_empty[0: :3]
	prices= inventory_empty[1: :3]
	quantities = inventory_empty[2: :3]

	del names[0]
	del prices[0]
	del quantities[0]
	
	for i in range (len(prices)):
		prices[i]= float(prices[i])
	for i in range(len(quantities)):
		quantities[i]=int(quantities[i])
	user_choice = display()

	while user_choice != 0:
		if user_choice ==1:
			display_total(names,prices,quantities)
		elif user_choice == 2:
			add_item(names,prices,quantities)
		elif user_choice ==3:
			delete_items(names,prices,quantities)
		elif user_choice == 4:
			update_item(names,prices,quantities)
		else:
			display_total_value(names,prices,quantities)

		user_choice = int(input("Enter a number you'd like): "))
	
	updated_inventory = zip (names,prices,quantities)
	final_inventory=[]
	for sublist in updated_inventory:
		final_inventory.append(sublist)
	format_inventory=[]
	for i in range(len(final_inventory)):
		for j in final_inventory[i]:
			format_inventory.append(j)
	print(format_inventory)

	new_inventory=open("inventory_output.csv", 'w')
	new_inventory.write("Name, Price, Quantity\n")
	for item in final_inventory:
		new_inventory.write(str(item) + '\n')
	new_inventory.close()

main()
