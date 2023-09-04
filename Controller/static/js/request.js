

// 날짜 선택 범위 0 + Today - 30
$(document).ready(function() {
    var today = new Date();
    var thirtyDaysAgo = new Date();
    thirtyDaysAgo.setDate(today.getDate() - 30);

    var formattedDate = today.toISOString().split('T')[0];
    var formattedThirtyDaysAgo = thirtyDaysAgo.toISOString().split('T')[0];

    var startDayInput = document.getElementById("startDay");
    startDayInput.value = formattedDate;
    startDayInput.setAttribute("min", formattedThirtyDaysAgo);
    startDayInput.setAttribute("max", formattedDate);
})

 // 시간 선택기 옵션
document.addEventListener('DOMContentLoaded', function () {
    var startTimePicker = flatpickr("#wantTime_s", {
        enableTime: true,
        enableSeconds: true,
        noCalendar: true,
        dateFormat: "H:i:S",
        time_24hr: true,
        defaultHour: 0,
        minuteIncrement: 1,
        position: "custom",
        appendTo: document.querySelector(".time-container-1"),
        inline: true, //false true
        onChange: validateTime
    });

    var endTimePicker = flatpickr("#wantTime_e", {
        enableTime: true,
        enableSeconds: true,
        noCalendar: true,
        dateFormat: "H:i:S",
        time_24hr: true,
        defaultHour: 0,
        minuteIncrement: 1,
        position: "custom",
        appendTo: document.querySelector(".time-container-2"),
        inline: true,
        onChange: validateTime
    });

    // 유효성 검사 - 시간 선택기
    function validateTime() {
        var startTime = startTimePicker.selectedDates[0];
        var endTime = endTimePicker.selectedDates[0];

        if (startTime && endTime) {
            if (startTime.getTime() < endTime.getTime()) {
                document.getElementById('wantTime_s').classList.add('is-valid');
                document.getElementById('wantTime_s').classList.remove('is-invalid');
                document.getElementById('wantTime_e').classList.add('is-valid');
                document.getElementById('wantTime_e').classList.remove('is-invalid');
            } else {
                document.getElementById('wantTime_s').classList.remove('is-valid');
                document.getElementById('wantTime_s').classList.add('is-invalid');
                document.getElementById('wantTime_e').classList.remove('is-valid');
                document.getElementById('wantTime_e').classList.add('is-invalid');
            }
        } else {
            if (startTime) {
                document.getElementById('wantTime_s').classList.remove('is-valid');
                document.getElementById('wantTime_s').classList.add('is-invalid');
            }
            if (endTime) {
                document.getElementById('wantTime_e').classList.remove('is-valid');
                document.getElementById('wantTime_e').classList.add('is-invalid');
            }
        }
    }
});



// 유효성 검사 - Check
var selectElement = document.getElementById('part');
var terms = document.getElementById('terms');

selectElement.addEventListener('change', function() {
    if (selectElement.value !== '') {
        selectElement.classList.add('is-valid');
    } else {
        selectElement.classList.remove('is-valid');
        selectElement.classList.add('is-invalid');
    }
});

terms.addEventListener('click', function() {
    terms.classList.add('is-valid');
});

terms.addEventListener('change', function() {
    if (terms.checked) {
        terms.classList.add('is-valid');
        terms.classList.remove('is-invalid');
    } else {
        terms.classList.remove('is-valid');
        terms.classList.add('is-invalid');
    }
});


// 유효성 검사 - Submit
document.getElementById('form').addEventListener('submit', function(event) {
    var startTimeValue = wantTime_s.value;
    var endTimeValue = wantTime_e.value;
    var termsChecked = terms.checked;
    var getLocationBtn = document.getElementById('getLocationBtn');
    var selectElement = document.getElementById('part');

    var messages = [];

    if (!getLocationBtn.classList.contains('btn-success')) {
        messages.push('위치정보 수집에 동의해주세요.');
    }

    if (!startTimeValue && !endTimeValue) {
        messages.push('시작 시간과 종료 시간을 입력해주세요.');
    } else if (!startTimeValue) {
        messages.push('시작 시간을 입력해주세요.');
    } else if (!endTimeValue) {
        messages.push('종료 시간을 입력해주세요.');
    } else if (startTimeValue >= endTimeValue) {
        messages.push('시작 시간은 종료 시간보다 빨라야 합니다.');
    }



    if (selectElement.value === '') {
        messages.push('열람 사유를 선택해주세요.');
    }

    if (!termsChecked) {
        messages.push('법적 고지 및 약관에 동의해주세요.');
    }

    if (messages.length > 0) {
        alert(messages.join('\n'));
        event.preventDefault();
    }
});

