/*
 *  9.Palindrome Number 
     Given an integer x, return true if x is a palindrome, and false otherwise.
 * 
 */
#include <string.h>
#include <stdbool.h>

/* Solution 1 : Reverse half of the number-------------------------------
    Time Complexity: O(log(n))
*/
bool isPalindrome(int x)
{
    if (x < 0 || (x != 0 && x % 10 == 0))
        return false;

    int res = 0;
    while (res < x)
    {
        res = res * 10 + x % 10;
        x /= 10;
    }

    return res == x || res / 10 == x;
}

/* Solution 2 : Double pointer-------------------------------
    Time Complexity: O(n)
*/

bool isPalindrome2(int x)
{   
    if (x < 0 || (x != 0 && x % 10 ==0))
        return false;

    char s[16];

    int length = snprintf(s, sizeof(s), "%d", x);

    int front = 0;
    int rear = length - 1;

    while(front < rear)
    {
        if(!(s[front++] == s[rear--]))
        {
            return false;
        }
    }
    return true;
}