import Plyr from 'plyr';
const players = Plyr.setup('#players');

// Add an event listener to the delete buttons
// document.querySelectorAll('.delete-button').forEach(button => {
//     button.addEventListener('click', function() {
//         const videoId = button.getAttribute('data-video-id');
//         // Send an AJAX request to the backend to delete the video
//         fetch(`/delete_video/${videoId}`, { method: 'POST' })
//             .then(response => response.json())
//             .then(data => {
//                 if (data.success) {
//                     // Video was deleted successfully, remove the corresponding video card
//                     const videoCard = button.closest('.video-card');
//                     if (videoCard) {
//                         videoCard.remove();
//                     }
//                 } else {
//                     // Display an error message or handle failure
//                 }
//             })
//             .catch(error => {
//                 // Handle errors
//             });
//     });
// });