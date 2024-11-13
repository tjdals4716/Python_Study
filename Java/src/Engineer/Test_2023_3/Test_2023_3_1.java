package Engineer.Test_2023_3;

public class Test_2023_3_1 {
    public static void main(String[] args) {
        A b = new B();
        b.paint();
        b.draw();
    }
}

class A {
    public void paint() {
        System.out.print("A");
        draw();
    }
    public void draw() {
        System.out.print("B");
        draw();
    }
}

class B extends A {
    public void paint() {
        super.draw();
        System.out.print("C");
        this.draw();
    }
    public void draw() {
        System.out.print("D");
    }
}
