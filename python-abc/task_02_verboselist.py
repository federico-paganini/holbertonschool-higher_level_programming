#!/usr/bin/python3


class VerboseList(list):

    def append(self, item):
        super().append(item)
        print("")

    def extend(self, item):
        super().extend(item)

    def remove(self, item):
        super().remove(item)

    def pop(self, index=None):
        super().pop(index)
