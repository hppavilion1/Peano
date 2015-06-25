class OrderedDict:
    def __init__(self, **kwargs): #Constructor (Note that kwargs does not preserve order)
        '''Construct an ordered dict'''
        self._l = [] #List (for order)
        self._d = {} #Dict (for mapping)
        for x in kwargs: #Add each of the kwarg keys to a list and their key/value pairs to a dict
            self._l.append(x)
            self._d[x] = kwargs[x]

    def append(self, x): #x is a tuple representing (key, value) pair
        '''Add key/value pair (key, value) to the end of the ordered dict'''
        if x[0] in self._l:
            raise ValueError('Tried to add already existing key to OrderedDict: '+x)
        self._l.append(x[0]) #Add key to end of list
        self._d[x[0]] = x[1] #Add (key, value) pair to dictionary

    def extend(self, m):
        '''Append the elements of x to self'''
        for x in m: #Add each of the kwarg keys to a list and their key/value pairs to a dict
            if x[0] in self._l:
                raise ValueError('Tried to add already existing key to OrderedDict: '+x)
            self._l.append(x)
            self._d[x] = kwargs[x]

    
