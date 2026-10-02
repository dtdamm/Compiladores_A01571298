
# Diego Torre A01571298
# 01/10/2026

"""Implementacion y Documentacion de Dict, Fila y pila en Python con casos de preuba y manipulacion para verificar funcionalidad de funciones primarias.

Use una herramienta externa para generar el boiler-plate de las estrcuturas. La documentacion fue hecha por mi dentro del codigo usando las "Python Google Coding Conventions", tanto de las implementaciones como de los test cases. La funcionalidad se puede verificar ejecutando el segundo archivo de pruebas en el directorio.

Las preubas se pueden verificar usando el archivo Tarea1-pruebas.py el cual hace import de las implementaciones documentadas aqui

Se usó el modelo Sonnet 5.5 de Anthropic para realizar la tarea, se le realizaron las siguientes consultas:

Cuales son las operaciones de acceso y manipulación de un Stack, Queue y Dict?

En funcion de las funciones principales, que edge cases son primordiales para asegurar el funcionamiento de estas?

Proporciona el python el boilerplate necesario para hacer la implementacion de estas estructuras y test cases y de mi parte hacer la documentacion usando las "Python Google Coding Conventions" para la implmentacion, para que sea mi responsabilidad clarificar el funcionamiento y proposito del codigo, asi como test cases, dame el template para verificar funciones principales.

"""

EMPTY = 0
FILLED = 1
DELETED = 2


class Node:
    """Linked list node for stack and queue implementations

    Attributes:
        value: curr node value
        next (Node | None): direction of next node in list
    """

    def __init__(self, value, next=None):
        """ node constructor
        """
        self.value = value
        self.next = next


class Stack:
    """Stack (LIFO) implementation with elemantary functions push O(1), pop O(1), peek O(1), is_empty O(1)

    Attributes:
        _top (Node | None): node that was last inserted 
        _size (int): size of stack
    """

    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, value):
        """Place node on top of stack and add 1 to size

        Args:
            value: value to be inserted on top of stack
        """
        self._top = Node(value, self._top)
        self._size += 1

    def pop(self):
        """Remove item at top of stack, return its value and remove 1 from size

        Returns:
            value at node on top of stack

        Raises:
            Error when stack is empty
        """
        if self._top is None:
            raise IndexError("pop from empty stack")
        node = self._top
        self._top = node.next
        self._size -= 1
        return node.value

    def peek(self):
        """Read value at top of stack

        Returns:
            Value of node at top of stack

        Raises:
            Error when stack is empty
        """
        if self._top is None:
            raise IndexError("empty stack")
        return self._top.value

    def is_empty(self):
        """Returns boolean if stack contains any value

        Returns:
            bool: If stack has any values
        """
        return self._size == 0

    def __len__(self):
        """reads stack curr size value

        Returns:
            int: size of stack
        """
        return self._size


class Queue:
    """Implementation of Queue (FIFO) Structure with primary fucntions enqueue O(1), dequeue O(1), peek O(1) and is_empty O(1)


    Attributes:
        _head (Node | None): front of queue
        _tail (Node | None): last node on queue
        _size (int): total of nodes in queue
    """

    def __init__(self):
        """Construction of queue"""
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, value):
        """Addition of node to the back of queue, check if tail exists and add new value as it succesor, if not establish new value as tail

        Args:
            value: added value in new node
        """
        node = Node(value)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def dequeue(self):
        """ Remove head and establish prev from head as new head

        Returns:
            Value of head

        Raises:
            IndexError: queue empty throws error
        """
        if self._head is None:
            raise IndexError("empty queue")
        node = self._head
        self._head = node.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return node.value

    def peek(self):
        """ See element at head of queue

        Returns:
            curr value of head node

        Raises:
            IndexError: 
        """
        if self._head is None:
            raise IndexError("peek from empty queue")
        return self._head.value

    def is_empty(self):
        """Verify Queue is not empty

        Returns:
            bool: True if queue is empty, False if it contains at least one node
        """
        return self._size == 0

    def __len__(self):
        """return Queue length

        Returns:
            int: recorded size
        """
        return self._size


class Dict:
    """Dictionary structure with primary functions insert O(1), update O(1), delete O(1), exists,O(1) resize O(n) and find O(1)

    Attributes:
        _limit (int): max table slots size
        _size (int): amount of registers
        _used (int): slots that have been filled, marked as FILLED
        _state (list[int]): State of actual slots between EMPTY, FILLLED and DELETED
        _keys (list[int]): keys in each slot
        _values (list): values mapped to keys in dict
    """

    def __init__(self):
        self._limit = 10
        self._size = 0
        self._used = 0
        self._state = [EMPTY] * self._limit
        self._keys = [0] * self._limit
        self._values = [None] * self._limit

    def _check(self, key):
        """look for existance of key in dict

        Args:
            key: value of key to be looked for

        Raises:
            TypeError: If attribute key is not int
        """
        if type(key) is not int:
            raise TypeError(f"key must be an integer, got {key!r}")

    def _find(self, key):
        """Looks for state of hashed key and checks its status and verifies there is no collision in key to be inerted/updated

        Args:
            key (int): Key to be hashed and searched

        Returns:
            tuple[int | None, int | None]: returns either found index of key and its value or None if free slot
        """
        slot = hash(key) % self._limit
        free = None
        while True:
            state = self._state[slot]
            if state == EMPTY:
                return None, (free if free is not None else slot)
            if state == DELETED:
                if free is None:
                    free = slot
            elif self._keys[slot] == key:
                return slot, free
            slot = (slot + 1) % self._limit

    def _resize(self):
        """Looks for slots with filled state and reinserts them, disregarding deleted or empty state ones and rebuilding to adjust for collisions in new resulting dict"""
        old_state, old_keys, old_values = self._state, self._keys, self._values
        self._limit *= 2
        self._size = 0
        self._used = 0
        self._state = [EMPTY] * self._limit
        self._keys = [0] * self._limit
        self._values = [None] * self._limit
        for state, key, value in zip(old_state, old_keys, old_values):
            if state == FILLED:
                self.insert(key, value)

    def insert(self, key, value):
        """Hash key, look for slot until no collisions affect insertion and add the key value pair to new slot

        Args:
            key (int): key to be inserted
            value: new value to be mapped to complete key, value pair
        """
        self._check(key)
        index, free = self._find(key)
        if index is not None:
            self._values[index] = value
            return
        if self._state[free] == EMPTY:
            self._used += 1
        self._state[free] = FILLED
        self._keys[free] = key
        self._values[free] = value
        self._size += 1
        if self._used > self._limit * 2 / 3:
            self._resize()

    def get(self, key):
        """

        Args:
            key (int): lookup key in dictionary and return its mapped value

        Returns:
            valuemapped to arg key

        Raises:
            TypeError: 
            KeyError: 
        """
        self._check(key)
        index, _ = self._find(key)
        if index is None:
            raise KeyError(key)
        return self._values[index]

    def exists(self, key):
        """Checks if key exists inside dict

        Args:
            key: target key to look up

        Returns:
            bool: result, True if contained, flase if not
        """
        if type(key) is not int:
            return False
        index, _ = self._find(key)
        return index is not None

    def delete(self, key):
        """IF key exists in dict, remove its pair

        Args:
            key (int(): key too look up

        Raises:
            TypeError: Key is not correct type
            KeyError: Key does not exist in dict
        """
        self._check(key)
        index, _ = self._find(key)
        if index is None:
            raise KeyError(key)
        self._state[index] = DELETED
        self._values[index] = None
        self._size -= 1

    def __len__(self):
        """return

        Returns:
            int: 
        """
        return self._size

    def __getitem__(self, key):
        """Use get fucntion to get correpsonding val."""
        return self.get(key)

    def __setitem__(self, key, value):
        """insert key value pair"""
        self.insert(key, value)

    def __delitem__(self, key):
        """Remove key value pair from dict if it exists"""
        self.delete(key)

    def __contains__(self, key):
        """Verify key exits within the dictionary"""
        return self.exists(key)
