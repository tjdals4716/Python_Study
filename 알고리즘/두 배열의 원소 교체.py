def max_sum_after_k_swaps(N, K, A, B):
    # Step 1 : 배열 A를 오름차순으로 정렬
    A.sort()
    
    # Step 2 : 배열 B를 내림차순으로 정렬
    B.sort(reverse=True)
    
    # Step 3 : A의 가장 작은 원소와 B의 가장 큰 원소를 최대 K번 교환
    for i in range(K):
        if A[i] < B[i]:
            A[i], B[i] = B[i], A[i]
        else:
            break
    
    # Step 4 : A의 합을 계산
    return sum(A)

# 예제 입력
N = 5
K = 3
A = [1, 2, 5, 4, 3]
B = [5, 5, 6, 6, 5]

# 함수 호출 및 결과 출력
result = max_sum_after_k_swaps(N, K, A, B)
print(result)
