package Week7_Session1;

public class InstanceOfEx {
    public static void main(String[] args) {
        System.out.print("새로운 학생() -> \t");print(new Student());
        System.out.print("새로운 연구원() -> \t");print(new Researcher());
        System.out.print("새로운 교수() -> \t");print(new Professor());
    }

    static void print(Person p){
        if(p instanceof Person){
            System.out.print("사람 ");
        }

        if(p instanceof Student){
            System.out.print("학생 ");
        }

        if(p instanceof Researcher){
            System.out.print("연구원 ");
        }

        if(p instanceof Professor){
            System.out.print("교수 ");
        }
        System.out.println();
    }
}

class Person{}

class Student extends Person{}

class Researcher extends Person{}

class Professor extends Person{}