package Java_Study.Object_Oriented_Programming;

import java.util.Scanner;

//객체지향 프로그래밍, 학생 클래스와 평균을 구하는 메서드를 구현하여 학생의 점수 5개에 과목이 나오도록하고 평균을 출력하는 프로그램
public class StudentAverage_Upgrade {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] subjects = {"국어", "수학", "영어", "과학", "사회"};
        int[] scores = new int[subjects.length];
        String name;

        System.out.print("학생의 이름을 입력하세요 : ");
        name = scanner.nextLine();

        for (int i = 0; i < subjects.length; i++) {
            System.out.print(subjects[i] + " 점수를 입력하세요 : ");
            scores[i] = scanner.nextInt();
        }

        Student_Upgrade student = new Student_Upgrade(name, scores);
        double average = student.getAverage();
        System.out.println(name + "학생의 평균 점수 : " + average + "입니다.");

        scanner.close();
    }
}

class Student_Upgrade {
    String name;
    int[] score;

    public Student_Upgrade(String name, int[] score) {
        this.name = name;
        this.score = score;
    }

    public double getAverage() {
        int sum = 0;
        for (int scores : score) {
            sum += scores;
        }
        return (double) sum / score.length;
    }
}
