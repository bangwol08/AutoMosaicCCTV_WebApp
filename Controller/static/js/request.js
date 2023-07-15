// 0. 달력 선택 조정
var today = new Date();
// 오늘포함 이전 30일 까지 설정 for 상상기업
// var thirtyDaysAgo = new Date();
// thirtyDaysAgo.setDate(today.getDate() - 30);

//  "YYYY-MM-DD"
var formattedDate = today.toISOString().split('T')[0];
// 30일 전 for 상상기업
// var formattedT hirtyDaysAgo = thirtyDaysAgo.toISOString().split('T')[0];

var startDayInput = document.getElementById("startDay");
startDayInput.value = formattedDate;

// 오늘 날짜만
startDayInput.setAttribute("max", formattedDate);
startDayInput.setAttribute("min", formattedDate);
// 오늘포함 이전 30일 까지만 선택 가능 코드 for 상상기업
// startDayInput.setAttribute("min", formattedThirtyDaysAgo);

// 1. 시간 선택
// jQuery 시간 선택기 옵션
$(document).ready(function(){
    // Bootstrap 라이브러리 초기화
    // $('[data-toggle="tooltip"]').tooltip();
    // $('[data-toggle="popover"]').popover();
	$.datepicker.setDefaults({

    });
    
    // 창 크기 변경하면 사라지게
    $(window).resize(function () {
      $("#ui-datepicker-div").css({ display: "none" });
    })

	// 토글? 형식  0~12.
	// $('#wantTime_s').timepicker({
	// 	controlType: 'select',
	// 	oneLine: true,
	// 	timeFormat: 'hh:mm:ss',
	// 	hourMin: 0,
	//     hourMax: 23
	// });
	// $('#wantTime_e').timepicker({
	// 	controlType: 'select',
	// 	oneLine: true,
	// 	timeFormat: 'hh:mm:ss',
	// 	hourMin: 0,
	//     hourMax: 23
	// });

    // 해상도가 768px 이상인 경우에만 실행
    if ($(window).width() >= 768) {
        // 슬라이드 형식 0~23
        var startTimeTextBox = $('#wantTime_s');
        var endTimeTextBox = $('#wantTime_e');

        $.timepicker.timeRange(
            startTimeTextBox,
            endTimeTextBox,
            {
                timeOnlyTitle: '시간 선택',
                timeText: '시간',
                hourText: '시',
                minuteText: '분',
                secondText: '초',
                currentText: '현재 시간',
                closeText: '완료',
                // minInterval: (1000*60*60), // 1시간
                // minInterval: (1000*5),  // 이 값은 5초.
                timeFormat: 'HH:mm:ss',
                start: {}, // 시작 선택기 옵션
                end: {} // 끝 선택기 옵션
            }
        );
    }
});


// 3. 유효성 검사
$(document).ready(function(){
    (function () {
      // 'use strict'

      var forms = document.querySelectorAll('.needs-validation')

      Array.prototype.slice.call(forms).forEach(function(form) {
        form.addEventListener('submit', function(event) {
          var inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
          var radioChecked = document.querySelector('input[name="part"]:checked');

          // Check if all required inputs and radio button are filled
          var allInputsFilled = Array.prototype.every.call(inputs, function(input) {
            return input.checkValidity();
          });

          if (!allInputsFilled || !radioChecked) {
            event.preventDefault();
            event.stopPropagation();
          }

          form.classList.add('is-valid');
        }, false);
      });
    })();

    // 시간
    $(document).ready(function() {
  // Time picker validation
  $('#wantTime_s').timepicker({
    onClose: function(time) {
      validateTimePicker();
    }
  });

  $('#wantTime_e').timepicker({
    onClose: function(time) {
      validateTimePicker();
    }
  });

  function validateTimePicker() {
    var startTimeInput = $('#wantTime_s');
    var endTimeInput = $('#wantTime_e');

    if (startTimeInput.val() && endTimeInput.val()) {
      startTimeInput.removeClass('is-invalid').addClass('is-valid');
      endTimeInput.removeClass('is-invalid').addClass('is-valid');

      var startTimeValue = new Date(`2000-01-01T${startTimeInput.val()}:00`);
      var endTimeValue = new Date(`2000-01-01T${endTimeInput.val()}:00`);

      if (startTimeValue.getTime() === endTimeValue.getTime()) {
        endTimeInput.removeClass('is-valid');
      } else if (startTimeValue.getTime() > endTimeValue.getTime()) {
        endTimeInput.removeClass('is-valid');
      }
    } else {
      startTimeInput.removeClass('is-valid').addClass('is-invalid');
      endTimeInput.removeClass('is-valid').addClass('is-invalid');
    }
  }

  // Radio button validation
  var termRadios = document.getElementsByName("part");
  var personalLabel = $('label[for="Personal"]');
  var publicLabel = $('label[for="Public"]');

  Array.from(termRadios).forEach(function(radio) {
    radio.addEventListener("change", function() {
      if (radio.checked) {
        if (radio.value === "Personal") {
          personalLabel.addClass("is-valid");
          publicLabel.removeClass("is-valid");
        } else if (radio.value === "Public") {
          personalLabel.removeClass("is-valid");
          publicLabel.addClass("is-valid");
        }
      }
    });
  });
});
});



(function () {
   'use strict'
    var forms = document.querySelectorAll('.needs-validation')

    Array.prototype.slice.call(forms)
    .forEach(function (form) {
      var inputs = form.querySelectorAll('input[required], select[required], textarea[required]')

      Array.prototype.slice.call(inputs)
        .forEach(function (input) {
          input.addEventListener('input', function () {
            if (input.checkValidity()) {
              input.classList.remove('is-invalid')
              input.classList.add('is-valid')
            } else {
              input.classList.remove('is-valid')
              input.classList.add('is-invalid')
            }
          })
        })

      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()