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
        // Send an AJAX request to the backend to delete the video
        // You can use Fetch or other AJAX libraries here
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
                // If successful, remove the video card from the DOM
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
