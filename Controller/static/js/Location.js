// 버튼 클릭 시 위치 정보 가져오는 함수
    function getLocation() {
      if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function(position) {
          const latitude = position.coords.latitude;
          const longitude = position.coords.longitude;
          const locationInput = document.getElementById("location");
          const locationBtn = document.getElementById("getLocationBtn")
          locationInput.value = `${latitude},${longitude}`;
          console.log(locationInput.value);
          locationBtn.innerText = '위치정보수집완료';
          locationBtn.classList.add('btn-success'); // 클릭하면 버튼 초록색으로

        }, function(error) {
          console.error("Error getting location:", error);
        });
      } else {
        console.log("Geolocation is not available.");
      }
    }

    function getMapLocation(latitude, longitude) {

          const data = { latitude, longitude };

          // Ajax 요청으로 위치 정보를 Flask 서버에 전송
          fetch('/cameraMap', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json'
              },
              body: JSON.stringify(data)
          })
          .then(response => response.json())
          .then(data => {
              // 서버에서 처리한 결과를 사용
              console.log(data);
          })
          .catch(error => {
              console.error("Error sending location to server:", error);
          });

    }