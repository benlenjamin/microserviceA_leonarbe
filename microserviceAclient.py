# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 53  # The port used by the server

# sample entries to show functionality
database = '''5/1/2024: Meal: Fried Chicken 650 Calories
5/1/2023: Snack: Potato Chips: 180 Calories
5/2/2023: Snack: Popsicle: 140 Calories
5/2/2024: Drink: Dr. Pepper: 150 Calories
5/2/2024: Drink: 2% Milk: 125 Calories
5/3/2025: Exercise: Running: 1 Mile
6/4/2025: Exercise: Push-ups: 17
12/12/2012: Exercise: Dumbbell Curls: 25 lbs: 10 reps
12/22/2015: Exercise: Barbell Squats: 135 lbs: 6 reps
1/1/2020: Meal: Cheeseburger and Fries: 990 Calories'''

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.sendto(database.encode(), (HOST, PORT))

message = "End of Input Data."
clientSocket.sendto(message.encode(), (HOST, PORT))

while True:
    keyword = input("Enter keyword for search (Case Sensitive): ")
    clientSocket.sendto(keyword.encode(), (HOST, PORT))

    response, _ = clientSocket.recvfrom(1024)

    # print("Echo Server Response: " + response.decode())
    outputString = response.decode()
    print(f"Search Results:\n{outputString}")

    choice = input("Do you want to continue? (y/n)")
    if choice.lower() != "y":
        message = "End of Search."
        clientSocket.sendto(message.encode(), (HOST, PORT))
        break

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#    s.connect((HOST, PORT))
#    s.sendall(b"Hello, world")
#    data = s.recv(1024)

# print(f"Received {data!r}")
