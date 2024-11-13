package Week6_Session1.ex_5_2;

class Person{
    private int weight;
    int age;
    protected String height;
    public String name;

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public int getWeight(){
        return weight;
    }
}

class Student extends Person{
    public void set(){
        age = 30;
        name = "홍길동";
        height = "180";
        setWeight(99);
    }
}

public class InheritanceEx {
    public static void main(String[] args) {
        Student s = new Student();
        s.set();
    }
}
