package My_Study.BuiltInFunction;

public class StringExample {
    public static void main(StringExample[] args) {
        String str = "Hello, Java World!";

        // length() 메서드
        System.out.println("Length: " + str.length());

        // charAt() 메서드
        System.out.println("Character at index 1: " + str.charAt(1));

        // substring() 메서드
        System.out.println("Substring (7, 11): " + str.substring(7, 11));

        // split() 메서드
        String[] words = str.split(" ");
        System.out.println("Split words: ");
        for (String word : words) {
            System.out.println(word);
        }

        // replace() 메서드
        System.out.println("Replace 'Java' with 'Python': " + str.replace("Java", "Python"));

        // toUpperCase(), toLowerCase() 메서드
        System.out.println("Uppercase: " + str.toUpperCase());
        System.out.println("Lowercase: " + str.toLowerCase());

        // trim() 메서드
        String withSpaces = "   trim example   ";
        System.out.println("Trimmed: '" + withSpaces.trim() + "'");
    }
}
