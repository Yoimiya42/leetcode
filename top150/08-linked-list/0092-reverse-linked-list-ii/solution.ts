// 92. Reverse Linked List II
// https://leetcode.com/problems/reverse-linked-list-ii/
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
function reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
    
};
