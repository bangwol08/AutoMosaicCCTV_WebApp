window.addEventListener('load', () => {
      const forms = document.getElementsByClassName('was-validated');

      Array.prototype.filter.call(forms, (form) => {
            button1.addEventListener('submit', function (event) {
              if (form.checkValidity() === false) {
                event.preventDefault();
                event.stopPropagation();
              }
              form.classList.add('was-validated');
            }, false);
      });
}, false);

var password = document.getElementById("password")
    , passcheck = document.getElementById("passcheck");
function validatePassword(){
    if(password.value != passcheck.value) {
        passcheck.setCustomValidity("패스워드가 일치하지 않습니다");
    }
    else {
        passcheck.setCustomValidity('');
    }
}

password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;

