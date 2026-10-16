/*
 *  9.Palindrome Number 
     Given an integer x, return true if x is a palindrome, and false otherwise.
 * 
 */

public class Palindrome {
    // Solution 1: Convert the integer to a string and compare the string with its reverse
    // Time Complexity: O(n)
    public boolean isPalindrome(int x)
    {   
        if(x < 0 || (x % 10 == 0 && x != 0))
        {
            return false;
        }
        String str = Integer.toString(x);
        String revStr = new StringBuilder(str).reverse().toString();
        return str.equals(revStr);

    }
    
    // Solution 2: Manually simulate the reverse process
    // Time Complexity: O(n)
    public boolean isPalindrome2(int x)
    {   
        if(x < 0)
        {
            return false;
        }

        StringBuilder sb = new StringBuilder();
        String str = String.valueOf(x);

        for(int i = str.length() - 1; i >= 0; i--)
        {
            sb.append(str.charAt(i));
        }

        return sb.toString().equals(str);
    }


}
