package My_Study.BuiltInFunction;

public class ObjectExample {
    public static void main(String[] args) {
        Circle c1 = new Circle(5);
        Circle c2 = new Circle(5);

        // equals() 메서드
        System.out.println("Are circles equal? " + c1.equals(c2));

        // hashCode() 메서드
        System.out.println("Circle 1 hashcode : " + c1.hashCode());
        System.out.println("Circle 2 hashcode : " + c2.hashCode());

        // toString() 메서드
        System.out.println(c1.toString());
    }
}

class Circle {
    int radius;

    Circle(int radius) {
        this.radius = radius;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Circle) {
            Circle other = (Circle) obj;
            return this.radius == other.radius;
        }
        return false;
    }

    @Override
    public int hashCode() {
        return radius * 31;
    }

    @Override
    public String toString() {
        return "Circle with radius : " + radius;
    }
}

