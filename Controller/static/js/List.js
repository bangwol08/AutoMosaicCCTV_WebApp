//
// const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]');
// const popoverContentContainer = document.getElementById('popover-content');
//
// popoverTriggerList.forEach((popoverTriggerEl, index) => {
//     const content = `
//         <p><strong>Video Title:</strong> ${items[index][1]}</p>
//         <p><strong>Requested By:</strong> ${items[index][2]}</p>
//         <p><strong>Request Time:</strong> ${items[index][3]}</p>
//     `;
//     popoverContentContainer.innerHTML = content;
//     popoverTriggerEl.setAttribute('data-bs-content', popoverContentContainer.innerHTML);
//
//     new bootstrap.Popover(popoverTriggerEl);
// });

// Add this code to your frontend JavaScript file
document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete-action');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const videoId = this.getAttribute('data-video-id');
            deleteVideo(videoId);
        });
    });

    function deleteVideo(videoId) {
        // Send an AJAX request to the backend to delete the video
        // You can use Fetch or other AJAX libraries here
        fetch(`/delete_video/${videoId}`, {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // If successful, remove the video card from the DOM
                const videoCard = document.querySelector(`.card${videoId}`);
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
