package Week7_Session2;

interface PhoneInterface{
    final int TIMEOUT = 10000;
    void sendCall();
    void receiveCall();
    default void printLogo(){
        System.out.println("폰");
    }
}

interface MobilePhoneInterface extends PhoneInterface{
    void sendSMS();
    void receiveSMS();
}

interface MP3Interface{
    public void play();
    public void stop();
}

class PDA{
    public int calculate(int x, int y){
        return x + y;
    }
}

class SamsungPhone extends PDA implements PhoneInterface, MobilePhoneInterface, MP3Interface{
    @Override
    public void sendCall(){
        System.out.println("띠리링");
    }

    @Override
    public void receiveCall(){
        System.out.println("전화 왔습니다");
    }

    @Override
    public void sendSMS(){
        System.out.println("문자 전송 중");
    }

    @Override
    public void receiveSMS(){
        System.out.println("문자 도착!");
    }

    @Override
    public void play(){
        System.out.println("음악이 재생됩니다");
    }

    @Override
    public void stop(){
        System.out.println("음악 재생을 중단합니다");
    }

    public void schedule(){
        System.out.println("일정을 관리합니다");
    }

    public void flash(){
        System.out.println("폰에 불이 켜짐");
    }
}

public class InterfaceEx {
    public static void main(String[] args) {
        SamsungPhone samsung = new SamsungPhone();
        samsung.printLogo();
        samsung.sendCall();
        samsung.receiveCall();
        samsung.flash();
    }
}
