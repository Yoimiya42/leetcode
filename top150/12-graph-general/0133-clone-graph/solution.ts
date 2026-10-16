// 133. Clone Graph
// https://leetcode.com/problems/clone-graph/
export {}; // local only: gives this file its own module scope

// ---- local definitions (do not submit) ----
class _Node {
    val: number
    neighbors: _Node[]
    constructor(val?: number, neighbors?: _Node[]) {
        this.val = (val===undefined ? 0 : val)
        this.neighbors = (neighbors===undefined ? [] : neighbors)
    }
}

// ---- submit below this line ----
function cloneGraph(node: _Node | null): _Node | null {
	
};
