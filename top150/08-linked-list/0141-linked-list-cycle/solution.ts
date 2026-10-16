// 141. Linked List Cycle
// https://leetcode.com/problems/linked-list-cycle/
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
function hasCycle(head: ListNode | null): boolean {
    
};
