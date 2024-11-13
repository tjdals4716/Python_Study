package Week5_Session1.ex_4_3;

public class Circle {
    int radius;
    String name;

    public Circle(){
        radius = 1;
        name = "";

    }

    public Circle(int r , String n){
        radius = r;
        name = n;
    }

    public double getArea(){
        return 3.14 * radius * radius;
    }

    public static void main(String[] args) {
        Circle pizza = new Circle(10, "자바피자");
//        pizza.radius = 10; // 매개 변수를 가진 생성자가 없을 때
//        pizza.name = "자바피자"; // 매개 변수를 가진 생성자가 없을 때
        double area = pizza.getArea();
        System.out.println(pizza.name + "의 면적 : " + area);

        Circle donut = new Circle();
//        donut.radius = 2; // 매개 변수를 가진 생성자가 없을 때
        donut.name = "자바도넛";
        area = donut.getArea();
        System.out.println(donut.name + "의 면적 : " + area);
    }
}
