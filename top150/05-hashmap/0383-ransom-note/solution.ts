// 383. Ransom Note
// https://leetcode.com/problems/ransom-note/
export {}; // local only: gives this file its own module scope

// ---- submit below this line ----
function canConstruct(ransomNote: string, magazine: string): boolean {
    const counter = Array(26).fill(0);
    for (const c of magazine) {
      counter[c.charCodeAt(0) - 'a'.charCodeAt(0)] ++;
    }
    for (const c of ransomNote) {
      if (--counter[c.charCodeAt(0) - 'a'.charCodeAt(0)] < 0)
        return false
    }
    return true
};
