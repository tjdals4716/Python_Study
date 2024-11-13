package Java_Study.Data_Structure;

class HashMap {
    private final int SIZE = 10000; // 해시맵의 크기
    private Node[] nodes; // 노드 배열

    // 노드 클래스: 키-값 쌍을 저장
    private class Node {
        int key, value; // 키와 값
        Node next; // 다음 노드를 가리키는 포인터

        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    // MyHashMap 클래스의 생성자
    public HashMap() {
        nodes = new Node[SIZE];
    }

    // 키의 해시 코드를 기반으로 인덱스를 계산
    private int getIndex(int key) {
        return Integer.hashCode(key) % SIZE;
    }

    //주어진 키를 가진 노드를 찾기 위한 메서드
    private Node find(Node head, int key) {
        Node prev = head;
        Node curr = head.next;
        while (curr != null && curr.key != key) {
            prev = curr;
            curr = curr.next;
        }
        return prev;
    }

    //키-값 쌍을 추가하거나 업데이트하는 메서드
    public void put(int key, int value) {
        int index = getIndex(key);
        if (nodes[index] == null) {
            nodes[index] = new Node(-1, -1); // 더미 노드 추가
        }
        Node prev = find(nodes[index], key);
        if (prev.next == null) {
            prev.next = new Node(key, value);
            System.out.println("키 " + key + "와 값 " + value + "을(를) 추가했습니다.");
        } else {
            prev.next.value = value;
            System.out.println("키 " + key + "의 값을 " + value + "(으)로 업데이트했습니다.");
        }
    }

    //주어진 키에 해당하는 값을 반환하는 메서드
    public int get(int key) {
        int index = getIndex(key);
        if (nodes[index] == null) return -1;
        Node prev = find(nodes[index], key);
        if (prev.next == null) return -1;
        int value = prev.next.value;
        System.out.println("키 " + key + "의 값은 " + value + "입니다.");
        return value;
    }

    //주어진 키와 해당하는 키-값 쌍을 삭제하는 메서드
    public void remove(int key) {
        int index = getIndex(key);
        if (nodes[index] == null) return;
        Node prev = find(nodes[index], key);
        if (prev.next != null) {
            System.out.println("키 " + key + "와 해당하는 값을 제거했습니다.");
            prev.next = prev.next.next;
        }
    }

    // 메인 메서드: 해시맵의 동작을 테스트
    public static void main(String[] args) {
        HashMap hashMap = new HashMap();

        hashMap.put(1, 1); //키 1에 값 1 추가
        hashMap.put(2, 2); //키 2에 값 2 추가

        System.out.printf("키 1에 대한 값 : " + hashMap.get(1)); //예상 출력: 1
        System.out.printf("키 3에 대한 값 : " + hashMap.get(3)); //예상 출력: -1 (존재하지 않는 키)

        hashMap.put(2, 1); //키 2에 대한 값을 1로 업데이트
        System.out.printf("키 2에 대한 값 : " + hashMap.get(2)); //예상 출력: 1

        hashMap.remove(2); // 키 2와 해당 값을 제거
        System.out.printf("키 2에 대한 값 : " + hashMap.get(2)); //예상 출력: -1 (제거된 키)
    }
}