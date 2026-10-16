
/*
Problem 83: Remove Duplicates from Sorted LinkedList
---------------------- J O U R N A L ---------------------
traversal operation 'cur = cur->next' must be placed in 'else' block
To avoid [1,1,1]
------------------- P R O B L E M - D E S C R I P T I O N ----------------------
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
*/
# include <stdlib.h>

typedef struct ListNode{
    int val;
    struct ListNode* next;
}ListNode;

ListNode* deleteDuplicates(ListNode* head)
{   
    if(!head)
        return head;

    ListNode* cur = head;
    while(cur && cur->next)
    {
        if(cur->val == cur->next->val)
        {   
            ListNode* temp = cur->next; 
            cur->next = temp->next;
            free(temp);
        }else{
            cur = cur->next;            
        }
    }
    return head;
}
