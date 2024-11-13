package My_Study;

import java.util.Scanner;

public class Array2DRatation2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = 0;
        int b = 0;

        // 행 입력
        while (true) {
            System.out.print("행을 입력하세요 (2 ~ 4 사이값 입력) (-1 입력 시 프로그램 종료) : ");
            a = sc.nextInt();

            if (a > 1 && a < 5) {
                break; // 유효한 값일 경우 종료
            } else if (a == -1) {
                System.out.println("프로그램을 종료합니다.");
                return; // 프로그램 종료
            } else {
                System.out.println("행을 다시 입력하세요.");
            }
        }

        // 열 입력
        while (true) {
            System.out.print("열을 입력하세요 (2 ~ 4 사이값 입력) (-1 입력 시 행 입력으로 돌아감) : ");
            b = sc.nextInt();

            if (b > 1 && b < 5) {
                break; // 유효한 값일 경우 종료
            } else if (b == -1) {
                System.out.println("행 입력으로 돌아갑니다.");
                a = 0; // 행을 초기화하고 다시 입력받음
                continue; // 행 입력으로 돌아감
            } else {
                System.out.println("열을 다시 입력하세요.");
            }
        }

        // 배열 입력 받기
        System.out.print(a * b + "개 정수를 입력하세요 : ");
        int[][] i = new int[a][b];
        for (int row = 0; row < i.length; row++) {
            for (int col = 0; col < i[row].length; col++) {
                i[row][col] = sc.nextInt();
            }
        }

        // 배열 출력
        System.out.println("입력된 배열 : ");
        printMatrix(i);

        // 회전 입력 처리
        while (true) {
            System.out.print("배열을 왼쪽(-1) 또는 오른쪽(1)으로 회전하시겠습니까? (0 입력 시 종료) : ");
            int rotate = sc.nextInt();

            if (rotate == -1) {
                i = rotateCounterClockwise(i); // 반시계 방향 회전
                System.out.println("배열이 반시계 방향으로 회전되었습니다.");
                printMatrix(i);
            } else if (rotate == 1) {
                i = rotateClockwise(i); // 시계 방향 회전
                System.out.println("배열이 시계 방향으로 회전되었습니다.");
                printMatrix(i);
            } else if (rotate == 0) {
                System.out.println("프로그램을 종료합니다.");
                break; // 프로그램 종료
            } else {
                System.out.println("잘못된 입력입니다. 다시 입력하세요.");
            }
        }
    }

    // 배열 출력 함수
    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int elem : row) {
                System.out.print(elem + " ");
            }
            System.out.println();
        }
    }

    // 배열을 시계 방향으로 회전하는 함수
    public static int[][] rotateClockwise(int[][] matrix) {
        int a = matrix.length;
        int b = matrix[0].length;
        int[][] rotated = new int[b][a]; // 행과 열의 크기가 바뀜

        for (int row = 0; row < a; row++) {
            for (int col = 0; col < b; col++) {
                rotated[col][a - 1 - row] = matrix[row][col];
            }
        }
        return rotated;
    }

    // 배열을 반시계 방향으로 회전하는 함수
    public static int[][] rotateCounterClockwise(int[][] matrix) {
        int a = matrix.length;
        int b = matrix[0].length;
        int[][] rotated = new int[b][a]; // 행과 열의 크기가 바뀜

        for (int row = 0; row < a; row++) {
            for (int col = 0; col < b; col++) {
                rotated[b - 1 - col][row] = matrix[row][col];
            }
        }
        return rotated;
    }
}

