# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 16/09/21
# -----------------------------------------------

# ***** IMPLEMENT A PROGRAM TO PERFORM THE FOLLOWING OPERATIONS *****

# 1. INSERTING AT THE END OF THE LINKED LIST.
# 2. INSERTING VALUE AT THE BEGINNING OF THE LINKED LIST.
# 3. PRINTING THE VALUES FROM THE LINKED LIST
# 4. INSERT ARRAY IN THE LINKED LIST
# 5. COLLECTING THE LENGTH OF THE LINKED LIST
# 6. INSERTING ELEMENT AT THE INDEX OF THE LINKED LIST
# 7. REMOVE THE ELEMENT AT THE INDEX
# 8. TO REMOVE LINKED LIST NODE BY VALUE
# 9. REVERSE THE GIVEN LINKED LIST


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # INSERTING AT THE END OF THE LINKED LIST.
    def insert_at_end(self, value):
        if self.head is None:
            self.head = ListNode(value)
            return

        itr = self.head

        while itr.next:
            itr = itr.next
        itr.next = ListNode(value)

    # INSERTING VALUE AT THE BEGINNING OF THE LINKED LIST.
    def insert_at_begin(self, value):
        if self.head is None:
            self.head = ListNode(value)
            return
        node = ListNode(value)
        node.next = self.head
        self.head = node

    # PRINTING THE VALUES FROM THE LINKED LIST
    def print(self):
        if self.head is None:
            print("Empty linked list")
            return

        itr = self.head
        string = ""
        while itr:
            string += str(itr.val) + "-->" if itr.next else str(itr.val)
            itr = itr.next

        print(string)

    # INSERT ARRAY IN THE LINKED LIST
    def insert_list(self, arr):
        if arr is None:
            print("Array is empty")

        for data in arr:
            self.insert_at_end(data)

    # COLLECTING THE LENGTH OF THE LINKED LIST
    def get_linked_list_length(self):
        if self.head is None:
            return 0
        count = 0
        itr = self.head

        while itr.next:
            count += 1
            itr = itr.next

        return count

    # INSERTING ELEMENT AT THE INDEX OF THE LINKED LIST
    def insert_element_at_index(self, index, value):
        if self.get_linked_list_length() < index or index <= 0:
            print("Invalid index.")
            return

        if index == 0:
            self.insert_at_begin(value)
            return

        if index == self.get_linked_list_length():
            self.insert_at_end(value)
            return

        itr = self.head
        count = 1
        while itr:
            if count == index:
                node = ListNode(value)
                node.next = itr.next
                itr.next = node
                break
            else:
                itr = itr.next
            count += 1

    # REMOVE THE ELEMENT AT THE INDEX
    def remove_at_index(self, index):
        if self.head is None:
            print("There is nothing to remove")
            return

        if index == 0:
            itr = self.head.next
            self.head = itr

        itr = self.head
        count = 1
        while itr:
            if count == index:
                itr.next = itr.next.next
            itr = itr.next
            count += 1

    # TO REMOVE LINKED LIST NODE BY VALUE
    def remove_by_value(self, value):
        if self.head is None:
            print("Linked list is not exist, pls create new and try this operation.")
            return

        itr = self.head
        is_value_present = False
        if itr.val == value:
            itr = itr.next
            self.head = itr
            return

        while itr:
            if itr.next is not None and itr.next.val == value:
                itr.next = itr.next.next
                is_value_present = True
            itr = itr.next
        if not is_value_present:
            print("Given value is not present in the linked list.")

    # REVERSE THE GIVEN LINKED LIST
    def reverse(self):
        curr = self.head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_list([10, 20, 30, 40, 50])
    ll.print()
    print()
    print(ll.get_linked_list_length())
    ll.insert_at_begin(0)
    ll.print()
    ll.insert_element_at_index(5, 88)
    ll.print()
    ll.remove_at_index(0)
    ll.print()
    ll.remove_by_value(88)
    ll.print()
    ll.reverse()
    ll.print()
