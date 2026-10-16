/**
 * You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.


    Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

    Example 2:
    Input: list1 = [], list2 = []
    Output: []

    Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]
 */


public class MergeTwoSortedLists<T extends Comparable<T>> {
    
    private static class ListNode<T extends Comparable<T>>{
        T val;
        ListNode<T> next;

        ListNode(T val){
            this.val = val;
        }

        @Override
        public String toString(){
            StringBuilder sb = new StringBuilder();

            ListNode<T> curr = this;
            while(curr != null){
                sb.append(curr.val);
                sb.append("->");
                curr = curr.next;
            }

            sb.append("null");
            return sb.toString();
        }
    }

    public ListNode<T> mergeTwoSortedLists(ListNode<T> list1, ListNode<T> list2){

        if (list1 == null)
            return list2;
        if (list2 == null)
            return list1;    
            
        ListNode<T> mergedList = new ListNode<>(null);
        ListNode<T> merged_curr = mergedList;
        ListNode<T> curr1 = list1;
        ListNode<T> curr2 = list2;

        while(true){
            if (curr1.val.compareTo(curr2.val) < 0){
                merged_curr.next = curr1;
                curr1 = curr1.next;
            }else{
                merged_curr.next = curr2;
                curr2 = curr2.next;
            }
                merged_curr = merged_curr.next;
            
            if (curr1 == null){
                merged_curr.next = curr2;
                break;
            }
            if (curr2 == null){
                merged_curr.next = curr1;
                break;
            }
        }

        return mergedList.next;
    }


    // Solution
    public ListNode<T> mergeTwoSortedLists_solution(ListNode<T> list1, ListNode<T> list2){

    ListNode<T> mergedList = new ListNode<>(null);
    ListNode<T> curr_merged = mergedList;
    while (list1 != null && list2 != null){
        if (list1.val.compareTo(list2.val) < 0){
            curr_merged.next = list1;
            list1 = list1.next;
        }else{
            curr_merged.next = list2;
            list2 = list2.next;
        }

        curr_merged = curr_merged.next;
    }

    curr_merged.next = list1 == null ? list2 : list1;
    return mergedList.next;
    }

}
