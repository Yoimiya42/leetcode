// 112. Path Sum
// https://leetcode.com/problems/path-sum/
#include <bits/stdc++.h>
using namespace std;

// ---- local definitions (do not submit) ----
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// ---- submit below this line ----
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        
    }
};
