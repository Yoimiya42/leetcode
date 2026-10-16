// 138. Copy List with Random Pointer
// https://leetcode.com/problems/copy-list-with-random-pointer/
export {}; // local only: gives this file its own module scope

// ---- local definitions (do not submit) ----
class _Node {
    val: number
    next: _Node | null
    random: _Node | null
    constructor(val?: number, next?: _Node, random?: _Node) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
        this.random = (random===undefined ? null : random)
    }
}

// ---- submit below this line ----
function copyRandomList(head: _Node | null): _Node | null {
    
};
