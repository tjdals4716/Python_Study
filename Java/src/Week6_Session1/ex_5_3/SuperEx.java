package Week6_Session1.ex_5_3;

class Point {
    private int x;
    private int y;

    public Point(int x, int y){
        this.x = 0;
        this.y = 0;
    }

    public void showPoint(){
        System.out.println("(" + x + ", " + y + ")");
    }
}

class ColorPoint extends Point {
    private String color;
    public ColorPoint(int x, int y, String color){
        super(x, y);
        this.color = color;
    }

    public void showColorPoint(){
        System.out.print(color);
        showPoint();
    }
}

public class SuperEx {
    public static void main(String[] args) {
        ColorPoint cp = new ColorPoint(5, 6, "blue");
        cp.showColorPoint();
    }
}
