const id = document.getElementById('id');
const idvalidation = document.getElementById('idvalidation');

const pw = document.getElementById('password');
const pwvalidation = document.getElementById('pwvalidation');

const pwc = document.getElementById('passcheck');
const pwcvalidation = document.getElementById('pwcvalidation');

const name = document.getElementById('name');
const namevalidation = document.getElementById('namevalidation');

const age = document.getElementById('age');
const agevalidation = document.getElementById('agevalidation');

const num = document.getElementById('phonenum');
const numvalidation = document.getElementById('numvalidation');

const address = document.getElementById('address');
const addressvalidation = document.getElementById('addressvalidation');

const submit = document.getElementById('submit');


id.addEventListener('input', function(event) {
    const inputValue = id.value;

    if (inputValue.length < 3) {
        idvalidation.textContent = '아이디는 최소 3자 이상입니다.'
        submit.disabled = true;
    } else {
        idvalidation.textContent = '';
        submit.disabled = false;
    }
});

pw.addEventListener('input', function(event) {
    const inputValue = pw.value;

    if (inputValue.length < 8 || pw.length > 20) {
        pwvalidation.textContent = '비밀번호는 8~20자 입니다.'
        submit.disabled = true;
    } else if(inputValue.search(/[0-9]/g)<0 || inputValue.search(/[a-z]/ig) < 0 || inputValue.search(/['~!@@#$%^&*|\\\'\";:\/?]/gi) < 0){
        pwvalidation.textContent = '영문, 숫자, 특수문자를 포함해주세요.'
        submit.disabled = true;
    }
    else {
        pwvalidation.textContent = '';
        submit.disabled = false;
    }
});
pwc.addEventListener('input', function(event) {
    const inputA = pw.value;
    const inputB = pwc.vlaue;
    if (inputA != inputB) {
        pwcvalidation.textContent = '입력하신 비밀번호와 맞지 않습니다.'
        submit.disabled = true;
    } else {
        pwcvalidation.textContent = '';
        submit.disabled = false;
    }
});

name.addEventListener('input', function(event) {
    const inputValue = name.value;

    if (inputValue.length < 2) {
        namevalidation.textContent = '이름은 2자 이상입니다.'
        submit.disabled = true;
    } else {
        namevalidation.textContent = '';
        submit.disabled = false;
    }
});

age.addEventListener('input', function(event) {
    const inputValue = age.value;

    if (inputValue < 0 || inputValue > 150) {
        agevalidation.textContent = '나이를 확인해주세요.'
        submit.disabled = true;
    } else {
        agevalidation.textContent = '';
        submit.disabled = false;
    }
});

age.addEventListener('input', function(event) {
    const inputValue = age.value;

    if (inputValue < 0 || inputValue > 150) {
        agevalidation.textContent = '나이를 확인해주세요.'
        submit.disabled = true;
    } else {
        agevalidation.textContent = '';
        submit.disabled = false;
    }
});

num.addEventListener('input', function(event) {
    const inputValue = num.value;
    const regex = /\d{3}-\d{4}-\d{4}/;
    if (!regex.test(inputValue)) {
        numvalidation.textContent = '휴대폰 번호는 000-0000-0000형태만 가능합니다.'
        submit.disabled = true;
    } else {
        numvalidation.textContent = '';
        submit.disabled = false;
    }
});