// Socket.io connection
const socket = io();

// Update user status
socket.on('status', function(data) {
    const statusElement = document.querySelector(`.user-status[data-user-id="${data.user_id}"]`);
    if (statusElement) {
        statusElement.textContent = data.status;
        statusElement.classList.remove('online', 'offline');
        statusElement.classList.add(data.status);
    }
});