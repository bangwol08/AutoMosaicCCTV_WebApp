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

