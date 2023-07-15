$(" #services ").click(function () {
    $(" #s-d ").toggleClass('show');
    // $("#nav-my-item").toggleClass("show");
    if (window.matchMedia("(max-width: 991px)").matches) {
        if ($(".dropdown").toggleClass("show")) {
            $("#nav-my-item").addClass("nav-my-item-show");
        } else {
            $("#nav-my-item").removeClass("nav-my-item-show");
        }
    }
});


// $(" #services ").click(function () {
//     if ($(" #s-d ").toggleClass('show')) {
//
//     // $("#nav-my-item").toggleClass("show");
//     if (window.matchMedia("(max-width: 991px)").matches) {
//         $("#nav-my-item").toggleClass("show");
//         $("#nav-my-item").addClass("nav-my-item-show");
//     } else {
//         $("#nav-my-item").removeClass("nav-my-item-show");
//     }
// }

$(document).ready(function() {
  $("#s-d").click(function() {
    $("#nav-msy-item").toggleClass("show");
    if ($("#nav-my-item").hasClass("show")) {
      $("#nav-my-item").css("margin", "12vh 0vw 0vh 0vw");
    } else {
      $("#nav-my-item").css("margin", "");
    }
  });
});

