// OlymPickScript.js

// 로그인 처리
document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault(); // 기본 폼 제출 동작을 막습니다.
    const uid = document.getElementById('uid').value;
    const password = document.getElementById('password').value;

    const data = {
        uid,
        password
    };

    fetch('http://localhost:8080/users/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (response.ok) {
            window.location.href = 'OlymPick 메인페이지.html'; // 로그인 성공 시 메인 페이지로 이동합니다.
        } else {
            alert('로그인 실패');
        }
    })
    .catch(error => console.error('로그인 에러:', error));
});

// 회원가입 처리
document.getElementById('signup-form').addEventListener('submit', function(event) {
    event.preventDefault(); // 기본 폼 제출 동작을 막습니다.
    const uid = document.getElementById('uid').value;
    const password = document.getElementById('password').value;
    const nickname = document.getElementById('nickname').value;
    const phoneNumber = document.getElementById('phoneNumber').value;
    const gender = document.getElementById('gender').value;
    const age = document.getElementById('age').value;
    const mbti = document.getElementById('mbti').value;

    const data = {
        uid,
        password,
        nickname,
        phoneNumber,
        gender,
        age,
        mbti
    };

    fetch('http://localhost:8080/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (response.ok) {
            alert('회원가입이 완료되었습니다!');
            window.location.href = 'OlymPick 로그인.html'; // 회원가입 성공 시 로그인 페이지로 이동합니다.
        } else {
            alert('회원가입 실패');
        }
    })
    .catch(error => console.error('회원가입 에러:', error));
});

function logout() {
    // 로그아웃 로직을 추가하세요 (예: 세션 종료, 토큰 삭제 등)
    alert('로그아웃되었습니다.');
    window.location.href = 'OlymPick 로그인.html'; // 로그아웃 후 로그인 페이지로 이동
}

function placeBid() {
    const bidAmount = document.getElementById('bid-amount').value;
    // 입찰 로직을 추가하세요 (예: 서버로 입찰 금액 전송)
    alert(`입찰 금액: ₩${bidAmount}`);
}

function goToCart() {
    window.location.href = 'OlymPick 장바구니.html'; // 장바구니 페이지로 이동
}
