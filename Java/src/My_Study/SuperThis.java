package My_Study;

// super
// .은 그 값이나 함수등에 접근한다는 뜻 => 맴버변수
// 메서드 명이 클래스 명과 같으면 생성자
// super() 하는 순간 부모의 빈 생성자를 호출
// super(). 하고 뒤에 입력하는 것은 부모의 어떤 것을 가져오겠다라는 뜻. ex) super.n : 부모의 n을 가져옴
// 자식이 태어나면 무조건 부모의 빈 생성자를 호출
// A a = new A() : a라는 객체를 생성해서 A() 객체를 넣음

// this
// this는 "이것"의 지시대명사 => 여기서 "이것"이란 클래스로부터 파생된 객체 그 변수를 말한다
// this() : 이 객체의 생성자를 호출해라
// this(32, "Hello") : 이 객체의 매개변수 2개짜리 생성자를 호출해라
// this.age : 이 객체의 맴버변수 age를 호출해라
// this.countNumbers() : 이 객체의 메서드를 호출해라
// 결론적으로 this는 어떤 클래스로부터 만들어진 객체 그 자체가 들어감
// 다시 말하지만 클래스명과 메서드명이 같으면 그게 생성자!!! => 그리고 생성자는 리턴값이 없음
// this에 대해 간단하게 말하자만 this는 생성된 객체의 나 자신을 넣는것임
// this는 생성자 코드 맨처음에 반드시 실행 => 안그럼 에러뜸

// 정리
// this, super 둘다 ()가 붙으면 생성자
// this, super 둘다 뒤에 .이 붙으면 변수이거나 메서드

public class SuperThis {
    int x;
    int y;

    SuperThis(int y){
        // x와 y는 아에 다른 변수
        // 여기서 this는 main 함수의 각각 test1, test2 객체가 됨
        // this.x = x;

        // 여기서는 this 매개변수에 따른 다른 생성자를 사용하라는 뜻
        this(10, 0);
    }

    SuperThis(int x, int y){
        this.x = x;
        this.y = y;
    }

    // 이 함수는 리턴 값이 클래스명 => 이 클래스 형태의 객체를 그대로 반환한다는 뜻
    SuperThis a(int a){
        this.x = a;
        return this;
    }

    void display(){
        // 여기서도 마찬가지로 this가 각각 순서대로 test1, test2 객체임
        System.out.println("x = " + this.x);
        System.out.println("x = " + this.x + ",y = " + this.y);
    }

    public static void main(String[] args) {
        SuperThis test1 = new SuperThis(1);
        SuperThis test2 = new SuperThis(10, 100);
        test1.display();
        test2.display();
    }


}
