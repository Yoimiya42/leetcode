/*
 Exercise 1 – Pancake Sorting
    Pancake Sort is a colloquial term for the mathematical problem of sorting a disordered stack of pancakes in order of size. A spatula can be inserted at any point i in the stack and used to flip all pancakes above it.

    Given an unsorted array, design and implement the pancake algorithm to sort it using only the “flip” operation, whose effect is to reverse the elements of the array between elements 0 and i (with i being the position where you imagine having inserted the spatula for flipping). Whereas a traditional sorting algorithm attempts to sort with the fewest comparisons possible, the goal here is to sort the sequence in as few “flips” as possible. Your algorithm should return the indices at which flips were performed.

    Example:
    Unsorted Input: [3,2,4,1]
    Sorted Output: [1,2,3,4]
    Algorithm Output: [1, 2, 3] ß indices where flips where performed (3 flips total).

    We have performed 3 flips (bold indicates it has been flipped):

    Start: [3, 2, 4, 1]
    1st flip (k = 1): [2, 3, 4, 1]
    2nd flip (k = 2): [4, 3, 2, 1]
    3rd flip (k = 3): [1, 2, 3, 4]

    Hint:
    Intuitively, this problem can be solved by:
    · Finding the largest out-of-order value
    · Flip that largest unsorted value to the bottom (you may need to flip it to the top first)
    · Repeat until the pancake stack is ordered
 */

 import java.util.ArrayList;
 

 class PancakeSort{
 
     public ArrayList<Integer> pancakeSort(int arr[]){
 
         int i = arr.length - 1;
         ArrayList <Integer> flips = new ArrayList<>();
 
         while(i > 0){
             int maxIndex = findMaxIndex(arr, 0, i);
             if(maxIndex != i)
             {
                 if(maxIndex != 0)
                 {
                     reverseArr(arr, 0, maxIndex);
                     flips.add(maxIndex + 1);
                 }
                 reverseArr(arr, 0, i );
                 flips.add(i + 1);
             }
 
             i--;
         }
 
         return flips;
     }
 
     public int findMaxIndex(int arr[], int left, int right){
         int max = left;
         for(int i = left; i <= right; i++)
             if(arr[i] > arr[max]) max = i;
         
         return max;
 
     }
 
 
     public void reverseArr(int arr[], int left , int right)
     {
         while(left < right)
             swap(arr, left++, right--);
     }
 
     public void swap(int arr[], int left, int right)
     {
         int temp = arr[left];
         arr[left] = arr[right];
         arr[right] = temp;
     }
 }
 