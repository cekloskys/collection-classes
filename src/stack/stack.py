from node.node import *

class stack:
    """Stack class that uses linked lists of nodes as its underlying data structure.
    """   
    def __init__(self):
        """Constructs an empty stack.
        """        
        self.__head = None          # reference to the top node in the stack
        self.__tail = self.__head   # reference to the bottom node in the stack
        self.__manyNodes = 0        # keeps track of the number of nodes in the stack

    def size(self):
        """Returns the number of nodes in the calling stack

        Returns:
            int: number of nodes
        """        
        return self.__manyNodes
    
    def getHead(self):
        """Returns a refernce to the head (top) of the calling stack

        Returns:
            node: reference to the head (top) of the calling stack
        """        
        return self.__head
    
    def getTail(self):
        """Returns a reference to the tail (bottom) of the calling stack

        Returns:
            node: reference to the tail (bottom) of the calling stack
        """        
        return self.__tail
    
    def getData(self):
        """Returns the data values in the calling stack

        Returns:
            str: data values in the calling stack
        """        
        cursor = self.__head    # used to step through the nodes in the calling stack
        data = ""               # string representation of data values in the calling stack
        i = 1                   # used to count the nodes in the calling stack

        # loop through the calling stack, one node at a time, getting the data values
        # and concatenating them to data
        while(i <= self.__manyNodes):
            data = data + (str(cursor.getData()) + ' ')
            cursor = cursor.getLink()
            i += 1

        # return data
        return data
    
    def __str__(self):
        """Returns string representation of the calling stack

        Returns:
            str: string representation of the calling stack
        """        
        return f"[ {self.getData()}]"
    
    def push(self, element):
        """Pushes (adds) the specified element to the top of the calling stack

        Args:
            element: specified element
        """    
        # if the calling stack is empty
        if (self.__head == None):
            # add node to calling stack
            self.__head = node(element, None) 
            # make tail refer to the same node as head
            self.__tail = self.__head
        else:
            # add node to the top of the stack
            self.__head = node(element, self.__head)

        # get the number of nodes in the calling stack
        self.__manyNodes = node.listLength(self.__head)

    def isEmpty(self):
        """Checks if the calling stack is empty.

        Returns:
            Boolean: True if the calling stack is empty, else False
        """        
        return self.size() == 0
    
    def pop(self):
        """Removes and returns the element at the head (top) of the calling stack.

        Raises:
            ValueError: indicates calling stack is empty

        Returns:
            _type_: element at the top of the calling stack
        """    
        try:
            # if the calling stack is empty, raise error
            if (self.isEmpty()):
                raise ValueError("Stack is empty.")
        except ValueError as e:
            # display value error and exit
            exit(e)
        else:
            # get data in node at the head (top) of the calling stack
            top = self.__head.getData()

            # advance head instance variable to next node
            self.__head = self.__head.getLink()

            # recompute the number of nodes in the calling stack
            self.__manyNodes = node.listLength(self.__head)

            # return data in node at the head (top) of the calling stack
            return top
        
    def peek(self):
        """Returns the element at the head (top) of the calling stack, without removing it.

        Raises:
            ValueError: indicates calling stack is empty

        Returns:
            _type_: element at the top of the calling stack
        """    
        try:
            # if the calling stack is empty, raise error
            if (self.isEmpty()):
                raise ValueError("Stack is empty.")
        except ValueError as e:
            # display value error and exit
            exit(e)
        else:
            # return data in node at the head (top) of the calling stack
            return self.__head.getData()