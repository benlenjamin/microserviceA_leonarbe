# microserviceA_leonarbe

Communication Contract:
a. To Request Data: Connect to the server using a socket (webSocket if HTML5).  Next send the data as a string to the server, followed by "End of Input Data.".  Next send a keyword using the same socket that you wish to search for in the data. (Example server is ran on localhost)
b. To Receive Data: Using the same socket object that was used to send data, receive the entries that contained the keyword sent earlier.  
c. [Uml diagram.pdf](https://github.com/benlenjamin/microserviceA_leonarbe/files/15385650/Uml.diagram.pdf)
