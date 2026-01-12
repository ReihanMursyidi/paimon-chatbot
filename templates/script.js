const welcomeScreen = document.getElementById('welcome-screen');
const chatContainer = document.getElementById('chat-container');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
let chatHistory = []; 

function fillInput(text) {
    userInput.value = text;
    userInput.focus();
}

function createBubble(text, isUser) {
    const div = document.createElement('div');
    div.className = "flex w-full " + (isUser ? "justify-end" : "justify-start");
    
    const bubble = document.createElement('div');
    
    // --- PERUBAHAN WARNA BUBBLE CHAT ---
    if (isUser) {
        // User: Biru tua solid dengan border emas
        bubble.className = "bg-[#2a2d55] border border-genshin-gold/40 text-genshin-cream px-5 py-3 rounded-3xl rounded-br-md max-w-[80%] leading-relaxed shadow-md";
    } else {
        // AI: Glassmorphism transparan dengan border biru/emas tipis
        bubble.className = "glass-ui text-genshin-cream px-5 py-3 rounded-3xl rounded-bl-md max-w-full prose prose-invert prose-p:leading-relaxed prose-p:text-genshin-cream prose-headings:text-genshin-gold prose-strong:text-genshin-gold prose-pre:bg-genshin-darker/70 prose-pre:border prose-pre:border-genshin-gold/20 prose-pre:rounded-xl shadow-sm";
    }
    
    if (isUser) {
        bubble.textContent = text;
    } else {
        if(text === "LOADING") {
            bubble.innerHTML = '<div class="flex items-center gap-2 ml-2"><div class="dot-flashing"></div></div>';
            bubble.id = "loading-bubble";
        } else {
            bubble.innerHTML = marked.parse(text);
        }
    }

    if (!isUser) {
        const wrapper = document.createElement('div');
        wrapper.className = "flex gap-3 max-w-full items-start";
        // Ikon AI diganti jadi bintang/sparkle emas-cyan
        wrapper.innerHTML = `
            <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-genshin-gold to-genshin-cyan flex-shrink-0 mt-1 flex items-center justify-center shadow-lg shadow-genshin-cyan/20">
                <i class="fa-solid fa-star text-genshin-darker text-sm"></i>
            </div>
        `;
        wrapper.appendChild(bubble);
        div.appendChild(wrapper);
    } else {
        div.appendChild(bubble);
    }

    chatContainer.appendChild(div);
    chatContainer.scrollTop = chatContainer.scrollHeight;
    return bubble;
}

chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const message = userInput.value.trim();
    if (!message) return;

    if (!welcomeScreen.classList.contains('hidden')) {
        welcomeScreen.classList.add('hidden');
        chatContainer.classList.remove('hidden');
        chatContainer.classList.add('flex', 'flex-col');
    }

    createBubble(message, true);
    userInput.value = '';
    userInput.disabled = true;
    sendBtn.disabled = true;

    const loadingBubble = createBubble("LOADING", false);

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                history: chatHistory,
                message: message
            })
        });

        const data = await response.json();
        loadingBubble.parentNode.parentNode.remove();
        createBubble(data.reply, false);

        chatHistory.push({ role: "user", content: message });
        chatHistory.push({ role: "model", content: data.reply });

    } catch (error) {
        loadingBubble.innerHTML = "<span class='text-red-400'>Error connecting to server.</span>";
    } finally {
        userInput.disabled = false;
        sendBtn.disabled = false;
        userInput.focus();
    }
});