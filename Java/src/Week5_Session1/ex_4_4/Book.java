package Week5_Session1.ex_4_4;

public class Book {
    String title;
    String author;

    public Book(String t) {
//        title = t;
//        author = "작자미상";
        this.title = t;
        this.author = "작자미상";
    }

    public Book(String t, String a) {
//        title = t;
//        author = a;
        this.title = t;
        this.author = a;
    }

    public static void main(String[] args) {
        Book a = new Book("어린왕자", "생텍쥐페리");
        Book b = new Book("춘향전");
        System.out.println(a.title + " " + a.author);
        System.out.println(b.title + " " + b.author);
    }
}
