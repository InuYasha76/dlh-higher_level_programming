#!/usr/bin/python3
"""This module is about linked lists"""


class Node:
    """
    This class is about creating new nodes.
    Node:
        - data: instance attribute containing a value
        - next_node, instance attribute containing:
            - A pointer to the next node
            - None: for single nodes

    """

    def __init__(self, data, next_node=None):
        """Instanciates an obect of Node class"""
        self.data = data
        self.next_node = next_node

    def data(self):
        """Getter: returns the stored value"""
        return self.__data

    def data(self, value):
        """
        Setter: checks that the value is an integer before assignment
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    def next_node(self):
        """Getter: returns a pointer to the next linked node"""
        return self.__next_node

    def next_node(self, value):
        """Setter: links to the next node thus has to be a Node"""
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class is about creating a linked list of nodes.
    It also manages the insertion of new nodes.
    New nodes are inserted according to their data attribute''s value.
    The resulting list is sorted in ascending order.

    """

    def __init__(self):
        """Instanciates an empty list. An empty list is a pointer to None"""
        self.__head = None

    def __str__(self):
        """Returns a string containing the values of all linked nodes."""
        result = []
        current_node = self.__head
        while current_node is not None:
            result.append(str(current_node.data))
            current_node = current_node.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """Inserts new nodes according to their value, in ascending order."""
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.__next_node = self.__head
            self.__head = new_node
        else:
            current_node = self.__head
            while (value > current_node.data and
                   current_node.next_node is not None):
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node
