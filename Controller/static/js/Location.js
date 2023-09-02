// 버튼 클릭 시 위치 정보 가져오는 함수
    function getLocation() {
      if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function(position) {
          const latitude = position.coords.latitude;
          const longitude = position.coords.longitude;
          const locationInput = document.getElementById("location");
          const locationBtn = document.getElementById("getLocationBtn")
          locationInput.value = `${latitude},${longitude}`;
          locationBtn.innerText = '위치정보수집완료';
          locationBtn.classList.add('btn-success'); // 클릭하면 버튼 초록색으로

        }, function(error) {
          console.error("Error getting location:", error);
        });
      } else {
        console.log("Geolocation is not available.");
      }
    }

    // // 내 위치 가져오기
    // // Assuming you have an input element with an id of "location"
    // const locationInput = document.getElementById("location");
    //
    // // To get the value of the input element
    // const locationValue = locationInput.value;
    //
    // // Now, locationValue contains the value of the input element
    // console.log(locationValue);