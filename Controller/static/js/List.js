document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete-action');
    const confirmButton = document.getElementById('confirmDeleteButton');
    let cardIdToDelete;
    let videoNameToDelete;

    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            cardIdToDelete = this.getAttribute('data-card-id');
            videoNameToDelete = this.getAttribute('data-video-name');
        });
    });

    confirmButton.addEventListener('click', function() {
        if (cardIdToDelete !== undefined && videoNameToDelete !== undefined) {
            deleteVideo(cardIdToDelete, videoNameToDelete);
        }
    });

    function deleteVideo(cardId, videoName) {

        fetch(`/DeleteVideo/${cardId}`, {
            method: 'POST',
            body: JSON.stringify({ videoName: videoName }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                //  비디오 카드를 DOM에서 제거
                const videoCard = document.querySelector(`#card${cardId}`);
                if (videoCard) {
                    videoCard.remove();
                }
            } else {
                console.error('영상삭제 실패');
            }
        })
        .catch(error => {
            console.error('영상삭제 실패:', error);
        });
    }
});