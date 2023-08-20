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

        }, function(error) {
          console.error("Error getting location:", error);
        });
      } else {
        console.log("Geolocation is not available.");
      }
    }