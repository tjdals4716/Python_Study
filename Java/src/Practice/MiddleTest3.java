package Practice;

// 레퍼런스 => 주소값, 주소값을 가리키는 행위
// 인스턴스화 => 객체화시킨다
// 자바에서 인스턴스 => 객체의 껍데기

// 추상화에 정의된 함수는 무조건 구현이 안되도됨. 하지만 추상 메서드는 무조건 구현해야함
// 추상화는 다중상속 불가
// 인터페이스에 정의된 함수는 무조건 구현 해야함
// 인터페이스는 다중상속 가능
// 두 기능 모두 결국 코드의 유지 보수성과 가독성, 가장 큰 것은 다형성을 위해 사용함
public class MiddleTest3 {
    static void print(Person p){
        if(p instanceof Person){
            System.out.println("참");
        }
    }

    public static void main(String[] args) {
        E a = new E();
        F b = new F();
        a.a();
        a.d();
        b.a();
        b.d();
    }
}

class Person{

}

abstract class C{
    void a(){}
    void b(){}
    void c(){}
    abstract void d();
}

interface D{
    void a();
    void b();
    void c();
    abstract void d();
}

class E extends C{
    void a(){
        System.out.println("난 추상 메소드 a야");
    }

    void b(){
        System.out.println("난 추상 메소드 b야");
    }

    // 여기 주석처리하면 에러 발생
    // 추상 메소드는 무조건 선언해야한다
    void d(){
        System.out.println("난 추상 메소드 d야");
    }
}

class F implements D{
    public void a(){
        System.out.println("난 인터페이스 a야");
    }

    public void b() {
        System.out.println("난 인터페이스 b야");
    }

    public void c() {
        System.out.println("난 인터페이스 c야");
    }

    public void d(){
        System.out.println("난 인터페이스 d야");
    }
}
