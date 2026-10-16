// 101. Symmetric Tree
// https://leetcode.com/problems/symmetric-tree/
export {}; // local only: gives this file its own module scope

// ---- local definitions (do not submit) ----
class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

// ---- submit below this line ----
function isSymmetric(root: TreeNode | null): boolean {
    
};
