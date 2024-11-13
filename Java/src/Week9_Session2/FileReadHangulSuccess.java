package Week9_Session2;

// ANSI 코드로 저장해야 꺠지지않고 잘 나옴
import java.io.*;
public class FileReadHangulSuccess{
    public static void main(String[] args) {
        InputStreamReader in = null;
        FileInputStream fin = null;
        try {
            fin = new FileInputStream("/Users/thdtjdals__/Desktop/문서/컴퓨터보안/encrypted_컴퓨터보안과제.txt");
            in = new InputStreamReader(fin, "US-ASCII");
            int c;
            System.out.println("인코딩 문자 집합은 " + in.getEncoding());
            while ((c = in.read()) != -1) {
                System.out.print((char)c);
            }
            in.close();
            fin.close();
        } catch (IOException e) {
            System.out.println("입출력 오류");
        }
    }
}
