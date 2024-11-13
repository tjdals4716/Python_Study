package My_Study;

public class InheritanceExplicit {
    public static void main(String[] args) {
        C c = new D(10);
        c.paint();
        c.draw();
    }
}

class C {
    public C(){
        System.out.println("상속, 생성자 테스트");
    }

    public C(int a){
        System.out.println("부모 매개변수 생성자" + a);
    }

    public void paint(){
        System.out.println("ㅎㅇ");
        draw();
    }

    public void draw(){
        System.out.println("난 부모의 draw 함수야");
        draw();
    }
}

class D extends C {
    public D(){
        super.paint();
    }

    public D(int a){
        // 명시적 선언에서 생성자에 super() 무조건 최상위줄에 있어야함
        super(10);
        System.out.println("자식 매개변수 생성자" + a);
    }

    public void paint(){
        System.out.println("난 자식의 paint 함수야");
    }

    public void draw(){
        System.out.println("난 자식의 draw 함수야");
    }
}
