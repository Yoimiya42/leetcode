// 2. Add Two Numbers
// https://leetcode.com/problems/add-two-numbers/
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
function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    
};
