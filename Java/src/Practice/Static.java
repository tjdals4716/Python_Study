package Practice;

// 굳이 static을 사용하려는 이유
// 그 함수나 변수를 전역적으로 사용하려고
// => 다른 클래스에서도 사용이 가능하도록
// => 굳이 public int 처럼 선언하지않고
public class Static {
    public static void main(String[] args) {
        A a = new A();
        A b = new B();
        B c = new B();
        System.out.println(a.a);
        System.out.println(a.b);
//        System.out.println(a.c); // private라 불가
//        System.out.println(a.d); // private라 불가
        System.out.println(a.e);
    }
}

class A {
    public int a = 1;
    public static int b = 2;
    private int c = 3;
    private static int d = 4;
    protected int e = 5;

    public A(){
        System.out.println("테스트입니다");
    }
}

// 여기서 마찬가지로 자식 생성자는 먼저 호출되면 안되고 부모 생성자 호출 후 부모 생성자 호출
class B extends A{
    public B(){
        System.out.println("안녕하세요");
    }
}