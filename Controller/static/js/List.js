document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete-action');
    const confirmButton = document.getElementById('confirmDeleteButton');
    let cardIdToDelete;
    let videoNameToDelete;
    var userId;

    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            // cardIdToDelete = this.getAttribute('data-card-id');
            const videoCardElement = this.closest('.video-card');
            cardIdToDelete = videoCardElement.getAttribute('id');
            videoNameToDelete = this.getAttribute('data-video-name');
        });
    });

    confirmButton.addEventListener('click', function() {
        if (cardIdToDelete !== undefined && videoNameToDelete !== undefined) {
            deleteFileUpdate(cardIdToDelete, videoNameToDelete, userId);
        }
    });

    function deleteFileUpdate(cardId, videoName, userId) {
        // Construct the data to send in the request
        const requestData = {
            cardId: cardId,
            videoName: videoName,
            UserId: UserId
        };

        fetch('/deleteUpdate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log('Video deleted and progress updated.');
            } else {
                console.error('Error deleting video:', data.error);
            }
        })
        .catch(error => {
            console.error('AJAX error:', error);
        });
    }

});


// document.addEventListener('DOMContentLoaded', function() {
//     const deleteButtons = document.querySelectorAll('.delete-action');
//     const dconfirmButton = document.getElementById('dconfirmDeleteButton');
//     let cardIdToDelete;
//     let videoNameToDelete;
//
//     deleteButtons.forEach(button => {
//         button.addEventListener('click', function() {
//             cardIdToDelete = this.getAttribute('data-card-id');
//             videoNameToDelete = this.getAttribute('data-video-name');
//         });
//     });
//
//     dconfirmButton.addEventListener('click', function() {
//         if (cardIdToDelete !== undefined && videoNameToDelete !== undefined) {
//             UpdateDeleteVideo(cardIdToDelete, videoNameToDelete);
//         }
//     });
//
//     function UpdateDeleteVideo(cardId, videoName) {
//         fetch(`/UpdateDeleteVideo/${cardId}`, {
//             method: 'POST',
//             body: JSON.stringify({ videoName: videoName }),
//             headers: {
//                 'Content-Type': 'application/json'
//             }
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.success) {
//                 // 비디오 카드를 DOM에서 제거
//                 const videoCard = document.querySelector(`#card${cardId}`);
//                 if (videoCard) {
//                     videoCard.remove();
//                 }
//
//                 // 영상 파일을 서버에서 삭제
//                 deleteVideoFile(videoName);
//             } else {
//                 console.error('영상삭제 실패');
//             }
//         })
//         .catch(error => {
//             console.error('영상삭제 실패:', error);
//         });
//     }
//
//     function deleteVideoFile(videoName) {
//         // 서버로부터 비디오 파일을 삭제하는 fetch 요청 추가
//         fetch(`/deleteVideoFile/${videoName}`, {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             }
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.success) {
//                 console.log('영상 파일 삭제 성공');
//             } else {
//                 console.error('영상 파일 삭제 실패');
//             }
//         })
//         .catch(error => {
//             console.error('영상 파일 삭제 실패:', error);
//         });
//     }
// });
