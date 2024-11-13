package Week7_Session1;

public class MethodOverridingEx {
    public static void main(String[] args) {
        Line line = new Line();
        paint(line);
        paint(new Shape());
        paint(new Line());
        paint(new Rect());
        paint(new Circle());
    }

    static void paint(Shape p) {
        p.draw();
    }
}

class Shape{
    public Shape next;
    public Shape(){
        next = null;
    }

    public void draw(){
        System.out.println("모양");
    }
}

class Line extends Shape{
    public void draw(){
        System.out.println("선");
    }
}

class Rect extends Shape{
    public void draw(){
        System.out.println("사각형");
    }
}

class Circle extends Shape{
    public void draw(){
        System.out.println("원");
    }
}
