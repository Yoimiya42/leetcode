public class ValidPalindrome {
    public static void main(String[] args){

    }
    // solution 1: reversion with rebuilding
    public static boolean isPalindrome(String s)
    {   
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < s.length(); i++)
        {   
            char ch = s.charAt(i);
            if(Character.isLetterOrDigit(ch))
            {
                sb.append(Character.toLowerCase(ch));
            }
        }
        String ori = sb.toString();
        return ori.equals(sb.reverse().toString());
    }
    
    // solution 2: Double pointer with rebuilding
    public static boolean isPalindrome2(String s)
    {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < s.length(); i++)
        {
            char ch = s.charAt(i);
            if(Character.isLetterOrDigit(ch))
            {
                sb.append(Character.toLowerCase(ch));
            }
        }

        int front = 0;
        int rear = sb.length() - 1;
        while(front < rear)
        {
            if(sb.charAt(front++) != sb.charAt(rear--)) return false;
        }

        return true;
    }

    // Best solution 3: double pointer without rebuilding
    // Time complexity: O(n)
    public static boolean isPalindrome3(String s)
    {
        int front = 0;
        int rear = s.length() - 1;

        while(front < rear)
        {
            while(front < s.length() - 1 && !Character.isLetterOrDigit(s.charAt(front)))
                front++;
            while(rear > 0 && !Character.isLetterOrDigit(s.charAt(rear)))
                rear--;
            if(front < rear && Character.toLowerCase(s.charAt(front)) != Character.toLowerCase(s.charAt(rear)))
                return false;
            
            front++;
            rear--;
        }

        return true;
    }


}
