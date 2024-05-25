# echo server
import socket

HOSTaddress = "127.0.0.1"  # localhost
PORT = 53

print("Server Loop is Running...")

tempSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tempSock.bind((HOSTaddress, PORT))

pastDataEntry = 0

while True:
    # must get data first from client
    inputList = []
    numInputLoops = 0

    dataBase = []
    outputList = []
    outputString = ""

    while pastDataEntry == 0:
        print("CP 1")
        inputDataRaw, client_address = tempSock.recvfrom(1024)
        inputData = inputDataRaw.decode().strip()
        # check for delimiter phrase
        if inputData == "End of Input Data.":
            pastDataEntry = 1
        else:
            numInputLoops = numInputLoops + 1
            inputList.append(inputData)
    # outside of data entry loop
    # debug
    # print(f"numInputLoops: {numInputLoops}")
    # print(f"Input Data: {inputList}")
    # next msg is keyword (includes string date)

    for entryBlock in inputList:
        # go from blocks of entries to each entry being an item in a list (dataBase)
        # .split() separates blocks of text into lines based on newline chars, removes newlines
        splitEntries = entryBlock.split('\n')
        # .append() would add the list splitEntries as an entry
        # .extend() will add each individual entry to the list dataBase
        dataBase.extend(splitEntries)

    # this is where the loop would be to search the same data again for a new keyword

    doneSearching = 0

    while doneSearching != 1:
        outputString = ""
        inputDataRaw, client_address = tempSock.recvfrom(1024)
        keyword = inputDataRaw.decode().strip()

        if keyword == "End of Search.":
            break

        # now to search through all entries with keyword
        for eachEntry in dataBase:
            if eachEntry.find(keyword) != -1:
                # means the keyword was in this entry
                # commented out below line as for now just the simple output string should be sufficient
                # outputList.append(eachEntry)
                outputString = outputString + eachEntry + "\n"
            # else:
            # pass
        # outside of search loop
        # debug
        # print(f"Results: {outputList}")
        print(f"Results:\n{outputString}")

        # client may need to loop through recvfrom to get all entries
        tempSock.sendto(outputString.encode(), client_address)

    # data, client_address = tempSock.recvfrom(1024)
    # message = data.decode().strip()

    # print(f"message: {message}")
    # tempSock.sendto(message.encode(), client_address)


# with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as tempSock:
#    tempSock.bind((HOSTaddress, PORT))
#    # tempSock.bind(('', PORT))
#    tempSock.listen()

#    conn, CONNaddress = tempSock.accept()
#    with conn:
#        print("Connected with {CONNaddress}")
#        while True:
#            data = conn.recv(1024)
#            if not data:
#                break
#            conn.sendall(data)
