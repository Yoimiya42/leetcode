// 427. Construct Quad Tree
// https://leetcode.com/problems/construct-quad-tree/
export {}; // local only: gives this file its own module scope

// ---- local definitions (do not submit) ----
class _Node {
    val: boolean
    isLeaf: boolean
    topLeft: _Node | null
	topRight: _Node | null
	bottomLeft: _Node | null
	bottomRight: _Node | null
	constructor(val?: boolean, isLeaf?: boolean, topLeft?: _Node, topRight?: _Node, bottomLeft?: _Node, bottomRight?: _Node) {
        this.val = (val===undefined ? false : val)
        this.isLeaf = (isLeaf===undefined ? false : isLeaf)
        this.topLeft = (topLeft===undefined ? null : topLeft)
        this.topRight = (topRight===undefined ? null : topRight)
        this.bottomLeft = (bottomLeft===undefined ? null : bottomLeft)
        this.bottomRight = (bottomRight===undefined ? null : bottomRight)
  }
}

// ---- submit below this line ----
function construct(grid: number[][]): _Node | null {

};
