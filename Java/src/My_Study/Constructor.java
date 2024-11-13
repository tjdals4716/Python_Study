package My_Study;

import javax.crypto.spec.PSource;

public class Constructor {
    public static void main(String[] args) {
        AB a = new AB();
        System.out.println("난 메인함수야" + a.i);
    }
}

class AB{
    int i = 0;

    public AB(){
        System.out.println("이건 빈 생성자야");
    }

    public AB(String a){
        System.out.println("이건 문자열 생성자야");
    }

    public AB(int a){
        System.out.println("이건 정수 생성자야");
    }
}
