package Week5_Session2.ex_4_6;

class Circle {
    int radius;

    public Circle(int radius){
        this.radius = radius;
    }

    public double getArea(){
        return 3.14 * radius * radius;
    }

    public int getSum(int i, int j){
        return i + j;
    }

    public double getSum(double i, double j){
        return(double)(i + j);
    }
}

public class CircleArray {
    public static void main(String[] args) {
        Circle c[] = new Circle[5];

        for(int i = 0;i < c.length;i++){
            c[i] = new Circle(i);
            System.out.print((int)(c[i].getArea()) + " ");
        }
        System.out.println();

        for(int i = 0;i < c.length;i++){
            System.out.print((int)(c[i].getArea()) + " ");
        }
    }
}

