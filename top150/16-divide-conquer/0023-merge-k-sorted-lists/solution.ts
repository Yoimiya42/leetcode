// 23. Merge k Sorted Lists
// https://leetcode.com/problems/merge-k-sorted-lists/
export {}; // local only: gives this file its own module scope

// ---- local definitions (do not submit) ----
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

// ---- submit below this line ----
function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    
};
