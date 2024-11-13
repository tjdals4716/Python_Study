package Week6_Session1.ex_5_1;

class Point{
    private int x, y; // 상속 불가한 것은 private로 정의
    public void set(int x, int y){ //set, showPoint만 상속 가능!
        this.x = x;
        this.y = y;
    }

    public void showPoint(){
        System.out.println("(" + x + ", " + y + ")");
    }
}

// 자식의 public은 부모가 사용 불가
// 부모꺼도 내꺼, 내꺼도 내꺼, 하지만 부모에 private가 걸리면 내꺼 아님
class ColorPoint extends Point{
    private String color;
    public void setColor(String color){
        this.color = color;
    }

    public void showColorPoint(){
        System.out.println(color);
        showPoint();
    }
}

public class ColorPointEx {
    public static void main(String[] args) {
        Point p =  new Point();
        p.set(1, 2);
        p.showPoint();

        ColorPoint cp = new ColorPoint();
        cp.set(3, 4);
        cp.setColor("red");
        cp.showColorPoint();
    }
}
