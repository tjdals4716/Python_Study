package Week9_Session2;

import java.io.*;
public class FileInputStreamEx {
    public static void main(String[] args) {
        byte b[] = new byte [6]; // 비어 있는 byte 배열
        try {
            FileInputStream fin = new FileInputStream("/Users/thdtjdals__/Desktop/문서/컴퓨터보안/encrypted_컴퓨터보안과제.txt");
            int n=0, c;
            while((c = fin.read())!= -1) {
                b[n] = (byte)c;
                n++;
            }
            System.out.println("/Users/thdtjdals__/Desktop/문서/컴퓨터보안/encrypted_컴퓨터보안과제.txt 에서 읽은 배열을 출력합니다.");
            for(int i=0; i<b.length; i++) System.out.print(b[i] + " ");
            System.out.println();
            fin.close();
        } catch(IOException e) {
            System.out.println("/Users/thdtjdals__/Desktop/문서/컴퓨터보안/encrypted_컴퓨터보안과제.txt 에서 읽지 못했습니다. 경로명을 체크해보세요");
        }
    }
}