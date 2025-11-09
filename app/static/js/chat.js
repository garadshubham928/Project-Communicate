let currentRecipientId = null;

// Chat initialization
document.querySelectorAll('.chat-item, .user-item').forEach(item => {
    item.addEventListener('click', function() {
        const userId = this.dataset.userId;
        loadChat(userId);
    });
});

// Message form handling
const messageForm = document.getElementById('message-form');
const messageInput = document.getElementById('message-input');
const attachButton = document.getElementById('attach-button');

messageForm.addEventListener('submit', function(e) {
    e.preventDefault();
    if (messageInput.value.trim() && currentRecipientId) {
        sendMessage(messageInput.value.trim());
        messageInput.value = '';
    }
});

// File attachment handling
attachButton.addEventListener('click', function() {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = 'image/*';
    
    input.onchange = async function() {
        const file = input.files[0];
        if (file) {
            const formData = new FormData();
            formData.append('file', file);
            
            try {
                const response = await fetch('/api/upload', {
                    method: 'POST',
                    body: formData
                });
                const data = await response.json();
                
                if (data.filename) {
                    sendMessage(`[attachment:${data.filename}]`);
                }
            } catch (error) {
                console.error('Error uploading file:', error);
            }
        }
    };
    
    input.click();
});

// Socket.io message handling
socket.on('message', function(data) {
    if ((data.sender_id === currentRecipientId && data.recipient_id === currentUserId) ||
        (data.sender_id === currentUserId && data.recipient_id === currentRecipientId)) {
        appendMessage(data);
    }
});

// Load chat messages
async function loadChat(userId) {
    currentRecipientId = userId;
    const messagesContainer = document.getElementById('messages');
    messagesContainer.innerHTML = '';
    
    // Update chat title
    const userItem = document.querySelector(`.user-item[data-user-id="${userId}"]`);
    const username = userItem.querySelector('h5').textContent;
    document.getElementById('chat-title').textContent = username;
    
    // Show message form
    messageForm.classList.remove('d-none');
    
    try {
        const response = await fetch(`/api/messages/${userId}`);
        const messages = await response.json();
        
        messages.forEach(message => {
            appendMessage(message);
        });
        
        // Scroll to bottom
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    } catch (error) {
        console.error('Error loading messages:', error);
    }
}

// Send message
async function sendMessage(content) {
    if (!currentRecipientId) return;
    
    try {
        const response = await fetch('/api/send_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                recipient_id: currentRecipientId,
                content: content
            })
        });
        
        const message = await response.json();
        appendMessage(message);
    } catch (error) {
        console.error('Error sending message:', error);
    }
}

// Append message to chat
function appendMessage(message) {
    const messagesContainer = document.getElementById('messages');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message');
    messageDiv.classList.add(message.sender_id === currentUserId ? 'sent' : 'received');
    
    // Check if message contains attachment
    if (message.content.startsWith('[attachment:') && message.content.endsWith(']')) {
        const filename = message.content.slice(11, -1);
        const isImage = /\.(jpg|jpeg|png|gif)$/i.test(filename);
        
        if (isImage) {
            messageDiv.innerHTML = `
                <div class="message-attachment">
                    <img src="/static/uploads/${filename}" alt="Attachment">
                </div>
            `;
        } else {
            messageDiv.innerHTML = `
                <div class="message-attachment">
                    <a href="/static/uploads/${filename}" target="_blank">${filename}</a>
                </div>
            `;
        }
    } else {
        messageDiv.textContent = message.content;
    }
    
    messagesContainer.appendChild(messageDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}