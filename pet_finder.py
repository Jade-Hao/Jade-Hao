import csv
from dog import Dog
from cat import Cat
from fish import Fish
from bird import Bird

pet_classes = { #used a dictonary to mark the classes as string types
    'dog': Dog,
    'cat': Cat,
    'fish': Fish,
    'bird': Bird,
}

def read_csv(fileName): #reads the CSV file
    pet_qualities = []
    with open(fileName, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            pet_type = row[0].lower() #looks at each row and identifies what is in each row
            name = row[1]
            birthday = row[2]
            breed = row[3]
            color = row[4]

            pet_class = pet_classes.get(pet_type)
            if pet_class:
                pet_qualities.append(pet_class(name, birthday, breed, color)) #writes out the qualities of the pet 
            else:
                print(f"Error: Unknown pet type '{pet_type}'")

    if len(pet_qualities) == sum(1 for line in open(fileName)):
        return pet_qualities
    else:
        print("Error: Number of pets does not match.")
        return []

def print_pet_names(pets_list): #looks the the pet list to get just the names
    for pet in pets_list:
        print(pet.get_name())

def pets_by_type(pets_list, pet_type):
    for pet in pets_list:
        if isinstance(pet, pet_classes.get(pet_type, object)): #used isinstance to return a t or f statment; if true prints pet
            print(pet)

def search_for_pet(pets_list, pet_name): #looks for pet in pet_list by looking/comparing at input from the user
    found = False
    for pet in pets_list:
        current_pet_name = pet.get_name().lower().strip()
        if current_pet_name == pet_name.lower().strip():
            print(f"Pet found: {pet}")
            found = True
            break
    if not found:
        print(f"Pet '{pet_name}' not found in the list.")

def sort_pets(pets_list): #used insertion to sort pets
    for i in range(1, len(pets_list)):
        current_pet = pets_list[i]
        position = i

        while position > 0 and get_pet_name(pets_list[position - 1]) > get_pet_name(current_pet):
            pets_list[position] = pets_list[position - 1]
            position -= 1

        pets_list[position] = current_pet

def get_pet_name(pet): #gets the name of the pet
    return pet.get_name()

def main():
    fileName = "pets.csv"
    pets_list = read_csv(fileName)

    while True: #menu 
        print("\nOptions:")
        print("1. Print only the names of all the pets")
        print("2. Show only pets of a certain type")
        print("3. Search for a pet")
        print("4. Sort list of pets")
        print("5. Exit program")

        choice = input("Please enter your choice, pick between 1-5: ") 

        if choice == "1": #goes through each option
            print_pet_names(pets_list)
        elif choice == "2":
            pet_type = input("Enter the type of pet (enter dog/cat/bird/fish): ").lower()
            if pet_type in pet_classes:
                pets_by_type(pets_list, pet_type)
            else:
                print("Invalid pet type.")
        elif choice == "3":
            pet_name = input("Enter the name of the pet to search for: ")
            search_for_pet(pets_list, pet_name)
        elif choice == "4":
            sort_pets(pets_list)
            print("List sorted by pet name.")
            for pet in pets_list:
                print(pet)
        elif choice == "5":
            print("Goodbye, thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5!")

if __name__ == "__main__":
    main()
