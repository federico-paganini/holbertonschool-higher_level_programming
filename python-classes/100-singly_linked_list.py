#!/usr/bin/python3
"""
This module defines a Node class and a SinglyLinkedList class.
The Node class represents a single element in a singly linked list.
The SinglyLinkedList class supports insertion of nodes in sorted (ascending) order.
"""


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        __head (Node): Private head node of the list.

    Methods:
        sorted_insert(value): Inserts a new Node in the correct sorted position.
        __str__(): Returns a string representation of the list, one value per line.
    """

    def __init__(self):
        self.__head = None

    def __str__(self):
        result = []
        aux = self.__head
        while aux is not None:
            result.append(str(aux.data))
            aux = aux.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            aux = self.__head
            while aux.next_node is not None and aux.next_node.data < value:
                aux = aux.next_node

            new_node.next_node = aux.next_node
            aux.next_node = new_node


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
