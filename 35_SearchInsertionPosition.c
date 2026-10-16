
/* 35. Search Insert Position
    Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.

        Example 1:

        Input: nums = [1,3,5,6], target = 5
        Output: 2
        Example 2:

        Input: nums = [1,3,5,6], target = 2
        Output: 1
        Example 3:

        Input: nums = [1,3,5,6], target = 7
        Output: 4
*/
// Start: Jan 17 22:35  
// End:   Jan 17 22:40  100% 0ms
int searchInsert(int* nums, int numsSize, int target)
{
    int start = 0;
    int end  = numsSize - 1;

    int mid;

    while(start <= end)
    {
        mid = start + (end - start) / 2;
        if(nums[mid] == target)
        {
            return mid;
        }

        if (nums[mid] < target)
        {
            start = mid + 1;
        }else{ // nums[mid] > target
            end = mid - 1;
        }
    }

    return start;
}
