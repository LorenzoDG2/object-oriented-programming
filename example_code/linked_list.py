"""A simple implementation of a linked list."""


import sys


class Link:
    """A link in a linked list.

    Parameters
    ----------
    value:
        The value to be stored in the link
    link: Link
        The next link in the list
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def insert(self, link):
        """Insert a new link after the current one."""
        link.next = self.next
        self.next = link

    def __iter__(self):
        return LinkIterator(self)


class LinkIterator:
    def __init__(self, link):
        self.current = link

    def __iter__(self):
        return self

    def __next__(self):  # makes more sense to me than in notes
        if self.current:
            value = self.current.value  # save value
            self.current = self.current.next
            return value
        else:
            raise StopIteration


def byte_size(n):
    """Print the size in bytes of lists up to length n."""
    data = []
    for i in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print(f"Length:{a}; Size in bytes:{b}")
        data.append(i)
