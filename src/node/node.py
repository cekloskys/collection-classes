class node:
    """The node class holds a collection of values using nodes. It includes
    methods that allow the nodes to be manipulated and modified.
    """   
    def __init__(self, data, link):
        """Constructs a node using the specified data value and link.

        :ivar __data: data value of node
        :ivar __link: link portion of node

        Args:
            data: specified data value
            link: specified link
        """        
        self.__data = data
        self.__link = link

    def getData(self):
        """Returns the data value stored in the calling node.

        Returns:
            _type_: data value stored in the calling node.
        """               
        return self.__data
    
    def setData(self, data):
        """Sets the data value stored in the calling node to the 
        specified data value.

        Args:
            data (_type_): specified data value
        """        
        self.__data = data

    def getLink(self):
        """Returns the link stored in the calling node.

        Returns:
            node: link stored in the calling node
        """        
        return self.__link
    
    def setLink(self, link):
        """Sets the link stored in the calling node to the specified link.

        Args:
            link (node): specified link
        """        
        self.__link = link

    def addNodeAfter(self, element):
        """Adds a new node containing a specified element value
        at a selected position in the calling node.

        Args:
            element (_type_): specified element value
        """        
        self.__link = node(element, self.__link)

    def removeNodeAfter(self):
        """Removes a node from a selected position in the calling node.
        """        
        self.__link = self.__link.__link

    @staticmethod
    def listLength(head):
        """Computes and returns the number of nodes in a specified node.

        Args:
            head (node): specified node

        Returns:
            int: number of nodes
        """  
        cursor = head   # cursor used to step through the specified node
        length = 0      # used to count the nodes

        # step through the nodes in the specified node as long as the
        # cursor isn't null
        while (cursor != None):
            # increment length
            length += 1

            # move cursor to next node
            cursor = cursor.getLink()

        # return length
        return length

    @staticmethod
    def listSearch(head, target):
        """Searches for a specified target in a specified node.

        Args:
            head (node): specified node
            target: specified target

        Returns:
            node: reference to node that contains specified target value
            if specified target value is found, else None
        """      
        cursor = head   # cursor used to step through the specified node

        # step through the nodes in the specified node as long as the
        # cursor isn't None
        while (cursor != None):
            # check if the data value in the node cursor refers to is equal
            # to the target
            if (cursor.getData() == target):
                # return cursor
                return cursor

            # move cursor to next node
            cursor = cursor.getLink()

        # return None
        return None  
    
    @staticmethod
    def listPosition(head, position: int):
        """Searches for a node in a specified node based on a specified position.

        Args:
            head (node): specified node
            position (int): specified position

        Raises:
            ValueError: indicates position is less than one

        Returns:
            node: reference to node at specified position if specified position
            is found, else None
        """       
        cursor = head   # used to step through the specified node
        i = 1           # used to count the nodes 

        try:
            # if position is less than 1, raise error
            if (position < 1):
                raise ValueError("Position may not be less than 1.")
        except ValueError as e:
            # display error and exit
            exit(e)
        else:
            # move cursor forward the correct number of nodes
            # as long as i is less than position and cursor isn't
            # equal to None
            # if cursor becomes None, that means the specified position
            # was greater than the number of nodes in the specified node
            while ((i < position) and (cursor != None)):
                # move the cursor to the next node
                cursor = cursor.getLink()
                # increment counter variable
                i += 1

            # return cursor
            return cursor
        
    @staticmethod
    def listCopy(source):
        """Make a copy of a specified node.

        Args:
            source (node): specified node

        Returns:
            node: reference to the head node in the copy
        """      
        # if specified source node is None, return None
        if (source is None):
            return None

        # make copy head refer to a node that contains the same
        # data value in the specified source node to be copied
        copyHead = node(source.getData(), None)
        # make copy tail refer to the same node as copy head
        copyTail = copyHead

        # keep looping through the specified source node to be copied
        # until we reach the node that has a link of None
        while (source.getLink() != None):
            # advance to the next node in the specified source node to be copied
            source = source.getLink()
            # get the data value in the specified source nod and add it to the
            # end of copy tail
            copyTail.addNodeAfter(source.getData())
            # advance copy tail to the next node
            copyTail = copyTail.getLink()

        # return copy head
        return copyHead
    
    @staticmethod
    def listCopyWithTail(source):
        """Makes a copy of a specified node

        Args:
            source (node): specified node to be copied

        Returns:
            [node]: references to head and tail of the copy
        """   
        # if specified source node is None, return None
        if (source is None):
            return None

        # make copy head refer to a node that contains the same
        # data value in the specified source node to be copied
        copyHead = node(source.getData(), None)
        # make copy tail refer to the same node as copy head
        copyTail = copyHead

        # keep looping through the specified source node to be copied
        # until we reach the node that has a link of None
        while (source.getLink() != None):
            # advance to the next node in the specified source node to be copied
            source = source.getLink()
            # get the data value in the specified source nod and add it to the
            # end of copy tail
            copyTail.addNodeAfter(source.getData())
            # advance copy tail to the next node
            copyTail = copyTail.getLink()

        # return copy head and copy tail
        return [copyHead, copyTail]     