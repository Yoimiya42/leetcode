/*
 125. Valid Palindrome
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.
*/

# include <string.h>
# include <stdbool.h>
# include <ctype.h>

// solution 1 : Double pointer with rebuilding 
// Time Complexity: O(n)
bool isPalindrome(char* s)
{   // Part 1 : Rebuild the string without non-alphanumeric characters
    char* newStr = malloc(sizeof(char) * (strlen(s) + 1));
    int index = 0;

    for(int i = 0; s[i] != '\0'; i++)
    {
        if(isalnum(s[i]))
        {
            newStr[index++] = tolower(s[i]);
        }
    }
    newStr[index] = '\0';
    
    // Part 2: Compare the new string with double pointer
    int front = 0;
    int rear  = strlen(newStr) - 1;
    while(front < rear)
    {
        if (newStr[front++] != newStr[rear--])
        {
            free(newStr);
            return false;
        }
    }

    free(newStr);
    return true;
}
// solution 2: Double pointer without rebuilding
bool isPalindrome2(char* s)
{
    int front = 0;
    int rear  = strlen(s) - 1;

    while(front < rear)
    {
        while(front < strlen(s) - 1 && !isalnum(s[front])) 
            front++;
        while(rear > 0 && !isalnum(s[rear])) 
            rear--;
        if(front < rear && tolower(s[front]) != tolower(s[rear])) 
            return false;
            
        front++;
        rear--;
    }

    return true;
}