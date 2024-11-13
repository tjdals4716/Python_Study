package Assignment;

import java.util.Scanner;
import java.util.InputMismatchException;

public class StudentManager {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        // 학생 정보 입력 받기
        String name = inputName();
        int koreanScore = inputScore("국어");
        int englishScore = inputScore("영어");
        int mathScore = inputScore("수학");

        // 1. 총점 및 평균 계산, 총점은 정수로 계산하되 평균은 실수형으로 계산할 것
        // 총점 (정수)
        int totalScore = koreanScore + englishScore + mathScore;
        // 평균 (실수형)
        double averageScore = totalScore / 3.0;

        // 학점 계산
        String grade = calculateGrade(averageScore);

        // 결과 출력
        printResult(name, koreanScore, englishScore, mathScore, totalScore, averageScore, grade);
        scanner.close();
    }

    // 2. 이름 입력 메소드 (입력에 공백이 있는지 없는지 판단하여, 공백이 있으면 다시 입력받을 것)
    public static String inputName() {
        while(true){
            System.out.print("이름을 입력하세요 : ");
            String name = scanner.nextLine();
            if(name == ""){
                System.out.println("이름에 공백을 입력했습니다. 이름을 정확히 입력해주세요");
            } else{
                return name;
            }
        }
    }

    // 3. 점수 입력 메소드 (점수에 숫자 아닌 것이 입력 안되도록, 0-100 사이 숫자만 입력되도록 제한할 것)
    public static int inputScore(String subject) {
        while(true){
            try{
                System.out.print(subject + " 점수를 입력하세요 : ");
                int score = scanner.nextInt();
                if(0 <= score && score <= 100) {
                    return score;
                } else{
                    System.out.println("현재 입력한 값은 " + score + "입니다. " + "0 ~ 100 사이의 값을 입력하세요");
                }
            // Exception in thread "main" java.util.InputMismatchException 에러 로그 확인 후 try catch문으로 감싸서 사용
            } catch (InputMismatchException e){
                // 현재 입력 스트림에 남아있는 토큰을 확인하려면 아래와 같이 작성 (3-17 참고)
                String ex = scanner.nextLine();
                // 잘못된 입력을 없애고 새로운 입력을 받도록 scanner 객체의 nextLine() 사용 (3-17 참고)
                System.out.println("현재 입력한 " + "'" + ex + "'" + "는(은) 숫자 정수가 아닙니다. 숫자 정수를 입력하세요");
            }
        }
    }

    // 4. 학점 계산 메소드 (~95 A+, ~ 90 A, ~85 B+, ~ 80 B, ~75 C+, ~70 C, ~65 D+, ~ 60 D, 이하 F)
    // 문자 타입 char은 단 하나의 문자만 저장하므로 문자 두개 이상 리턴 불가
    // ex) A+, 가나다 ...
    public static String calculateGrade(double averageScore) {
        if(95 <= averageScore && averageScore <= 100){
            return "A+";
//            'A' + '+';
        } else if(90 <= averageScore && averageScore <= 94) {
            return "A";
//            return 'A';
        } else if(85 <= averageScore && averageScore <= 89) {
            return "B+";
//            return 'B';
        } else if(80 <= averageScore && averageScore <= 84) {
            return "B";
//            return 'B';
        } else if(75 <= averageScore && averageScore <= 79) {
            return "C+";
//            return 'C';
        } else if(70 <= averageScore && averageScore <= 74) {
            return "C";
//            return 'C';
        } else if(65 <= averageScore && averageScore <= 69) {
            return "D+";
//            return 'D';
        } else if(60 <= averageScore && averageScore <= 64) {
            return "D";
//            return 'D';
        } else{
            return "F";
//            return 'F';
        }
    }

    // 5. 결과 출력 메소드
    public static void printResult(String name, int koreanScore, int englishScore, int mathScore, int totalScore, double averageScore, String grade) {
        System.out.println("\n==== 학생 성적 정보 ====");
        System.out.println("이름 : " + name);
        System.out.println("국어 : " + koreanScore);
        System.out.println("영어 : " + englishScore);
        System.out.println("수학 : " + mathScore);
        System.out.println("총점 : " + totalScore);
        System.out.printf("평균 : %.2f\n", averageScore);
        System.out.println("학점 : " + grade);
    }
}
