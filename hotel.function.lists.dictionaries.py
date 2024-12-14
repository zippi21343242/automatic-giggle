rooms = [
    {"type": "Economic", "count": 150, "price": 80},
    {"type": "Luxurious", "count": 100, "price": 140},
    {"type": "Suite", "count": 50, "price": 260},
]

tax_rate = 0.15

def show_available_rooms():
    print("\nAvailable Rooms:")
    for room in rooms:
        print(f"{room['type']} room | price = {room['price']} MAD | ({room['count']}) rooms available")

def book_rooms():
    try:
        num_rooms = int(input("How many rooms would you like to book? "))
        total_cost = 0  

        for _ in range(num_rooms):
            room_type = input("Enter the type of room (Economic, Luxurious, Suite): ").strip().capitalize()
            room = next((r for r in rooms if r["type"] == room_type), None)  
            if room:
                if room["count"] > 0:
                    nights = int(input("Enter the number of nights: "))
                    total_cost += room["price"] * nights
                    room["count"] -= 1  
                else:
                    print(f"No {room_type} rooms are available.")
            else:
                print("Invalid room type. Please choose Economic, Luxurious, or Suite.")

        tax = total_cost * tax_rate
        final_price = total_cost + tax
        print("\nInvoice:")
        print(f"Subtotal before tax: {total_cost} MAD")
        print(f"Tax (15%): {tax:.2f} MAD")
        print(f"Total price: {final_price:.2f} MAD")

    except ValueError:
        print("Invalid input. Please enter numeric values where required.")

def return_key():
    room_type = input("Enter the type of room you're returning (Economic, Luxurious, Suite): ").strip().capitalize()
    room = next((r for r in rooms if r["type"] == room_type), None)  
    if room:
        room["count"] += 1  
        print(f"{room_type} room returned successfully.")
    else:
        print("Invalid room type. Please choose Economic, Luxurious, or Suite.")

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Show available rooms")
        print("2. Book rooms")
        print("3. Return a room key")
        print("4. Exit")
        user_choice = input("Enter your choice (1-4): ").strip()

        if user_choice == '1':
            show_available_rooms()
        elif user_choice == '2':
            book_rooms()
        elif user_choice == '3':
            return_key()
        elif user_choice == '4':
            print("Exiting the system")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

main_menu()
