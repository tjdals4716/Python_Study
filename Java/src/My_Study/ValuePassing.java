package My_Study;

public class ValuePassing {
    public static void main(String[] args) {
        int n = 10;
        Circle pizza = new Circle(10);
        int a[] = {1, 2, 3, 4, 5};

        increase1(10);
        increase2(pizza);
        increase3(a);

        System.out.println(n);
        System.out.println(pizza.radius);

        for(int i = 0;i < a.length;i++){
            System.out.print(a[i] + " ");
        }

        // 위 for문 foreach 예시
        for (int j : a) {
            System.out.print(j + " ");
        }
    }

    static void increase1(int n) {
        n = n + 1;
    }

    static void increase2(Circle m){
        m.radius++;
    }

    static void increase3(int a[]){
        for(int i = 0;i < a.length;i++){
            a[i]++;
        }
    }
}

class Circle{
    int radius;

    public Circle(int r){
        radius = r;
        System.out.println("생성자 출력해보기");
    }
}

