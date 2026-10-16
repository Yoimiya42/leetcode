// 61. Rotate List
// https://leetcode.com/problems/rotate-list/
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
function rotateRight(head: ListNode | null, k: number): ListNode | null {
    
};
