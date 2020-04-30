class ReverseString
{
    public static void main(String[] args) {
        char[] s = {'a','b','c','d'};

        reverseString(s);
    }

    public static void reverseString(char[] s) {
        if(s.length>0)
        {
            reverseString(s);

        }
    }
}