package Java_Study.Object_Oriented_Programming;

import java.util.Scanner;

//객체지향 프로그래밍, 학생 클래스와 평균을 구하는 메서드를 구현하여 학생의 점수 5개의 평균을 출력하는 프로그램
public class StudentAverage {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] score = new int[5];
        String name;

        System.out.printf("학생의 이름을 작성하세요 : ");
        name = scanner.nextLine();

        for(int i = 0;i < 5;i++){
            System.out.printf(name + "학생의 점수를 입력하세요 (" + (i + 1) + "/5): ");
            score[i] = scanner.nextInt();
        }

        //학생 객체를 생성
        Student student = new Student(name, score);
        double average = student.getAverage();
        System.out.printf(name + "학생의 점수 평균 : " + average);

        scanner.close();
    }
}

class Student{
    String name;
    int[] score;

    //생성자 생성, 스프링 프레임워크엔 lombok이 존재하니 거기선 따로 사용 안해도 상관없음
    public Student(String name, int[] score) {
        this.name = name;
        this.score = score;
    }

    //점수 평균 계산 메서드
    public double getAverage(){
        int sum = 0;
        for(int scores : score){
            sum += scores;
        }
        return (double) sum / score.length;
    }
}
