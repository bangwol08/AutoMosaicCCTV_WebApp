// 2. 법적고지 및 약관
// 2-1. 모달
document.getElementById('myLink').addEventListener('click', function () {
  var myModal = new bootstrap.Modal(document.getElementById('myModal'));
  myModal.show();
})

// 2-2.	라디오 버튼을 눌러도 모달이 켜지도록.
$(document).ready(function(){
  $('#terms').click(function(){
    $('#myModal').modal('show');
  });
});