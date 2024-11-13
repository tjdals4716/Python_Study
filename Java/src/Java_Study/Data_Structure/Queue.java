package Java_Study.Data_Structure;

import java.util.Stack;

class Queue {
    private Stack<Integer> stack1; //첫 번째 스택
    private Stack<Integer> stack2; //두 번째 스택

    //MyQueue 클래스의 생성자
    public Queue() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }

    //큐에 요소를 추가하는 메서드
    public void push(int x) {
        stack1.push(x);
        System.out.println("큐에 " + x + "을(를) 추가했습니다.");
    }

    //큐에서 요소를 제거하고 반환하는 메서드
    public int pop() {
        //두 번째 스택이 비어 있다면 첫 번째 스택의 모든 요소를 두 번째 스택으로 이동
        if (stack2.isEmpty()) {
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }
        int value = stack2.pop(); //두 번째 스택에서 요소를 제거
        System.out.println("큐에서 " + value + "을(를) 제거했습니다.");
        return value;
    }

    //큐의 맨 앞 요소를 반환하는 메서드
    public int peek() {
        //두 번째 스택이 비어 있다면 첫 번째 스택의 모든 요소를 두 번째 스택으로 이동
        if (stack2.isEmpty()) {
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }
        int value = stack2.peek(); //두 번째 스택의 맨 위 요소를 확인
        System.out.println("큐의 맨 앞 요소는 " + value + "입니다.");
        return value;
    }

    //큐가 비어 있는지 확인하는 메서드
    public boolean empty() {
        boolean isEmpty = stack1.isEmpty() && stack2.isEmpty(); //두 스택이 모두 비어 있는지 확인
        System.out.println("큐가 비어 있습니까? " + isEmpty);
        return isEmpty;
    }

    //메인 메서드 : 큐의 동작을 테스트
    public static void main(String[] args) {
        Queue queue = new Queue();

        queue.push(1); //큐에 1 추가
        queue.push(2); //큐에 2 추가
        queue.push(3); //큐에 3 추가

        System.out.println("확인된 값 : " + queue.peek()); //예상 출력: 1

        System.out.println("제거된 값 : " + queue.pop());  //예상 출력 : 1
        System.out.println("제거된 값 : " + queue.pop());  //예상 출력 : 2

        System.out.println("큐가 비어 있습니까? " + queue.empty()); //예상 출력 : false

        queue.push(4); //큐에 4 추가
        System.out.println("제거된 값 : " + queue.pop()); //예상 출력 : 3

        System.out.println("확인된 값 : " + queue.peek()); //예상 출력 : 4
        System.out.println("제거된 값 : " + queue.pop()); //예상 출력 : 4

        System.out.println("큐가 비어 있습니까? " + queue.empty()); //예상 출력 : true
    }
}