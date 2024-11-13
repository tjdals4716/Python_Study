package My_Study.BuiltInFunction;

public class ThreadExample extends Thread {
    public void run() {
        try {
            System.out.println("Thread is running...");
            Thread.sleep(1000);  // sleep() 메서드
            System.out.println("Thread woke up!");
        } catch (InterruptedException e) {
            System.out.println("Thread interrupted!");
        }
    }

    public static void main(String[] args) {
        ThreadExample thread = new ThreadExample();
        thread.start();  // start() 메서드

        // 다른 작업 가능
        System.out.println("Main thread is running...");
    }
}

