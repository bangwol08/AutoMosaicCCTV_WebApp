// import Plyr from 'plyr';
// const player = Plyr.setup('#players');


document.addEventListener('DOMContentLoaded', function () {
    // 모든 비디오 요소에 대해 Plyr 초기화
    const videoElements = document.querySelectorAll('.video-container video');
    videoElements.forEach(function (videoElement) {
        var player = new Plyr(videoElements, {
            controls: ['play-large', 'play', 'progress', 'current-time', 'mute', 'volume', 'captions', 'settings', 'pip', 'airplay', 'fullscreen'],
            invertTime: false,
            keyboard: {
                focused: false,
                global: false
            },
            listeners: {
                // 리스너로 seek 안되게 처리할려면 요렇게
                seek: function customSeekBehavior(e) {
                    //e.preventDefault();
                    //alert('변경 불가능');
                    //return false;
                }
            }
        });
    });
});
