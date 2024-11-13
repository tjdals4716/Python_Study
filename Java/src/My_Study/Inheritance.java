package My_Study;

public class Inheritance {
    public static void main(String[] args) {
        // 이게 업캐스팅
        // 객체 b는 A이자 B이다 라는 뜻
        A b = new B();
        // 이 코드에서는 주석으로 자식 클래스에 paint 함수가 없앴으니 부모 클래스의 paint 함수를 호출
        b.paint();
        b.draw();
    }
}

class A{
    // 자식 생성자는 먼저 나오면 안되고 부모 생성자를 무조건 먼저 실행 시킨 뒤 자식 생성자가 실행 됨
    public A(){
        System.out.println("상속, 생성자 테스트");
    }

    // 자식 클래스에 paint나 draw 함수가 없다면 부모 클래스에서 그 함수를 사용
    public void paint(){
        System.out.println("ㅎㅇ");
        draw();
    }

    // 오버라이딩은 부모 것을 무시하고 자식 것만을 무조건 출력
    // 오버라이딩이니 무조건 자식 것만 출력
    // 오버라이딩의 조건은 상속받고 함수의 명과 매개변수가 같을 때
    public void draw(){
        System.out.println("난 부모의 draw 함수야");
//        draw();
    }
}

// 위 메인 함수에서 B()를 통해 B라는 생성자에 접근
// 자식 생성자는 먼저 나오면 안되고 부모 생성자를 무조건 먼저 실행 시킨 뒤 자식 생성자가 실행 됨
// 명시적이지 않을 때는 무조건 부모의 "빈 생성자"를 먼저 실행 후 자식의 빈 생성자든 매개변수를 가진 생성자를 실행
// 명시적일 땐? super(10) 이런식으로 명시적으로 호출 할 땐 부모의 "매개변수 생성자"를 실행
class B extends A {
    public B(){
        super.paint();
    }

//    public void paint(){
//        System.out.println("난 자식의 paint 함수야");
//    }

//    public void draw(){
//        System.out.println("난 자식의 draw 함수야");
//    }
}
