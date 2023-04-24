class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next
    # end def
# end class

class ListNodeHelper:
    def __init__(self) -> None:
        pass
    # end def

    def ListToNode(self, input:list) -> ListNode:
        head = ListNode(input[0])
        currentNode = head

        for element in input[1:]:
            currentNode.next = ListNode(element)
            currentNode = currentNode.next
        # end loop

        return head
    # end def

    def NodeToList(self, head: ListNode) -> list:
        if head is None:
            return None

        currentElement = head
        list = []

        while currentElement is not None:
            list.append(currentElement.val)
            currentElement = currentElement.next
        # end loop

        return list
    # end def
# end class