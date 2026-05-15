// ── KDK logo mark for avatars ──
const KDK_FAVICON = 'https://www.kdksoftware.com/assets/img/favicons/favicon-32x32.png';
const KDK_ICON = `<img class="kdk-logo-img" src="${KDK_FAVICON}" alt="KDK" onerror="this.replaceWith(document.createTextNode('KDK'))">`;

// ── State ──
const SESSION_ID   = crypto.randomUUID();
let messages       = [];
let isStreaming    = false;
let demoFormActive = false;
let demoBooked     = false;
let bookedDemoDetails = null;
let userProfile    = null;
let widgetOpen     = false;

// ── Widget Controls ──
function toggleWidget() { widgetOpen ? closeWidget() : openWidget(); }

function openWidget() {
  widgetOpen = true;
  document.getElementById('chat-widget').classList.remove('hidden');
  document.getElementById('chat-launcher').classList.add('open');
  if (!userProfile) {
    setTimeout(() => document.getElementById('pc-name')?.focus(), 120);
  } else {
    setTimeout(() => document.getElementById('msg-input')?.focus(), 120);
  }
}

function closeWidget() {
  widgetOpen = false;
  document.getElementById('chat-widget').classList.add('hidden');
  document.getElementById('chat-launcher').classList.remove('open');
}

// ── Training Mode State ──
let trainingMode   = false;
let trainingStep   = 0;
let trainingData   = {};
let trainingBanner = null;

// ── Voice State ──
let mediaRecorder  = null;
let recordingStream = null;
let audioChunks    = [];
let isRecording    = false;
let isProcessingVoice = false;
let ttsEnabled     = false;
let voiceCallMode  = false;
let vcTimerInterval = null;
let vcSeconds      = 0;
let currentAudio   = null;

// ── Chat History State ──
let chatSessions   = {};
let activeChatId   = null;

// ── DOM Refs ──
const messagesArea   = document.getElementById('messages');       // for appendChild
const messagesScroll = document.getElementById('messages-area'); // for scrollTop
const msgInput       = document.getElementById('msg-input');
const sendBtn        = document.getElementById('send-btn');
const typingRow      = document.getElementById('typing');
const micBtn         = document.getElementById('mic-btn');
const voiceBar       = document.getElementById('voice-bar');
const voiceLabel     = document.getElementById('voice-label');
const historyList    = document.getElementById('history-list');

// ─────────────────────────────────────────────
// INIT
// ─────────────────────────────────────────────
window.addEventListener('DOMContentLoaded', () => {
  fetchDemoCount();

  // Auto-resize textarea
  msgInput.addEventListener('input', () => {
    msgInput.style.height = 'auto';
    msgInput.style.height = Math.min(msgInput.scrollHeight, 130) + 'px';
  });

  // Enter = send, Shift+Enter = new line
  msgInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });

  // Pre-chat keyboard navigation
  document.getElementById('pc-name').addEventListener('keydown', (e) => {
    if (e.key === 'Enter') document.getElementById('pc-email').focus();
  });
  document.getElementById('pc-email').addEventListener('keydown', (e) => {
    if (e.key === 'Enter') submitPrechat();
  });

  // Focus handled by openWidget()
});

// ─────────────────────────────────────────────
// LEFT PANEL (mobile slide-in)
// ─────────────────────────────────────────────
function openMobilePanel() {
  document.getElementById('left-panel')?.classList.add('open');
  document.getElementById('lp-overlay')?.classList.add('visible');
}

function closeMobilePanel() {
  document.getElementById('left-panel')?.classList.remove('open');
  document.getElementById('lp-overlay')?.classList.remove('visible');
}

function leftPanelTopic(text) {
  closeMobilePanel();
  if (!userProfile) return;
  handleUserMessage(text);
}

// ─────────────────────────────────────────────
// SIDEBAR (no-op compat)
// ─────────────────────────────────────────────
function openSidebar() {}
function closeSidebar() {}

// ─────────────────────────────────────────────
// PRE-CHAT FORM
// ─────────────────────────────────────────────
async function submitPrechat() {
  const name  = document.getElementById('pc-name').value.trim();
  const email = document.getElementById('pc-email').value.trim();
  const role  = document.querySelector('input[name="pc-role"]:checked')?.value || 'Business / Enterprise';

  if (!name) {
    showToast('Please enter your name.');
    document.getElementById('pc-name').focus();
    return;
  }
  if (!email || !email.includes('@')) {
    showToast('Please enter a valid email.');
    document.getElementById('pc-email').focus();
    return;
  }

  const submitBtn = document.getElementById('pc-submit');
  submitBtn.textContent = 'Starting...';
  submitBtn.disabled = true;

  // Save lead to server
  try {
    await fetch('/api/save-lead', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email, role })
    });
  } catch(e) {
    // Non-blocking, continue even if save fails
  }

  userProfile = { name, email, role };

  // Switch screens inside widget
  document.getElementById('prechat-screen').classList.add('pc-hidden');
  document.getElementById('chat-screen').classList.remove('hidden');
  // Update profile bar
  const initials = name.split(' ').map(w => w[0]).join('').slice(0, 2).toUpperCase();
  document.getElementById('user-av').textContent = initials;
  document.getElementById('user-name-label').textContent = name;
  document.getElementById('user-role-label').textContent =
    role === 'CA / Tax Professional' ? 'CA / Tax Professional' : 'Business';

  // Show empty state, then welcome after delay
  showEmptyState();
  setTimeout(() => showWelcome(), 300);
}

// ─────────────────────────────────────────────
// EMPTY STATE
// ─────────────────────────────────────────────
function showEmptyState() {
  const firstName = userProfile ? userProfile.name.split(' ')[0] : 'there';
  const el = document.createElement('div');
  el.className = 'empty-state';
  el.id = 'empty-state';
  el.innerHTML = `
    <div class="empty-bot-wrap">
      <div class="empty-bot-av">${KDK_ICON}</div>
      <div class="empty-bot-ring"></div>
    </div>
    <h1 class="empty-title">Hi ${escapeHtml(firstName)}, <span>welcome!</span></h1>
    <p class="empty-sub">KDK Sales Team is here to help with products, demos, and fitment.</p>
    <div class="suggestion-grid">
      <button class="suggestion-card sc-gst" onclick="handleUserMessage('Tell me about Express GST')">
        <div class="sc-icon-box">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="18" height="20" rx="3" stroke="currentColor" stroke-width="2"/><path d="M7 8h10M7 12h7M7 16h5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
        </div>
        <div class="sc-text">
          <div class="sc-label">Express GST</div>
          <div class="sc-desc">Filing, reconciliation &amp; e-invoicing</div>
        </div>
        <span class="sc-arrow">›</span>
      </button>
      <button class="suggestion-card sc-tds" onclick="handleUserMessage('Tell me about Express TDS')">
        <div class="sc-icon-box">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="18" height="20" rx="3" stroke="currentColor" stroke-width="2"/><path d="M7 8h10M8 16l2 2 4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
        <div class="sc-text">
          <div class="sc-label">Express TDS</div>
          <div class="sc-desc">TDS returns, TRACES &amp; certificates</div>
        </div>
        <span class="sc-arrow">›</span>
      </button>
      <button class="suggestion-card sc-itr" onclick="handleUserMessage('Tell me about Express ITR')">
        <div class="sc-icon-box">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="18" height="20" rx="3" stroke="currentColor" stroke-width="2"/><path d="M12 17v-6M10 13l2-2 2 2" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
        <div class="sc-text">
          <div class="sc-label">Express ITR</div>
          <div class="sc-desc">ITR filing, tax audit &amp; AIS import</div>
        </div>
        <span class="sc-arrow">›</span>
      </button>
      <button class="suggestion-card sc-cal" onclick="handleUserMessage('I want to book a free demo')">
        <div class="sc-icon-box">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><rect x="3" y="4" width="18" height="18" rx="2" stroke="currentColor" stroke-width="2"/><path d="M8 2v4M16 2v4M3 10h18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
        </div>
        <div class="sc-text">
          <div class="sc-label">Book a Free Demo</div>
          <div class="sc-desc">20-min walkthrough, no commitment</div>
        </div>
        <span class="sc-arrow">›</span>
      </button>
    </div>
    <div class="empty-trust">
      <div class="et-item"><div class="et-num">10K+</div><div class="et-lbl">CAs Trust</div></div>
      <div class="et-div"></div>
      <div class="et-item"><div class="et-num">20+</div><div class="et-lbl">Yrs in India</div></div>
      <div class="et-div"></div>
      <div class="et-item"><div class="et-num">Free</div><div class="et-lbl">Demo</div></div>
    </div>`;
  messagesArea.appendChild(el);
}

function removeEmptyState() {
  document.getElementById('empty-state')?.remove();
}

// ─────────────────────────────────────────────
// WELCOME MESSAGE
// ─────────────────────────────────────────────
function showWelcome() {
  const firstName = userProfile ? userProfile.name.split(' ')[0] : 'there';
  const isCA      = userProfile?.role === 'CA / Tax Professional';

  const welcomeText = isCA
    ? `Hi ${firstName}! Great to connect. I'm from KDK Software's Sales Team.\n\n` +
      `We work with thousands of CAs and tax professionals across India, helping them manage compliance for all their clients from a single platform. **Express GST**, **Express TDS**, and **Express ITR** are built specifically for practices like yours.\n\n` +
      `To help me point you in the right direction, which area are you looking to streamline first?`
    : `Hi ${firstName}! Great to have you here. I'm from KDK Software's Sales Team.\n\n` +
      `We help businesses stay on top of their tax compliance, GST, TDS, and income tax, without the stress of deadlines and notices. Everything runs on the cloud, so your team can work from anywhere.\n\n` +
      `What brings you here today? Are you exploring a specific product or looking for an all-in-one solution?`;

  const quickReplies = ['Express GST', 'Express TDS', 'Express ITR', 'All three products'];

  appendBotMessage(welcomeText, quickReplies);
}

// ─────────────────────────────────────────────
// SEND MESSAGE
// ─────────────────────────────────────────────
function sendMessage() {
  const text = msgInput.value.trim();
  if (!text || isStreaming) return;
  msgInput.value = '';
  msgInput.style.height = 'auto';
  handleUserMessage(text);
}

async function handleUserMessage(text) {
  if (isStreaming) return;
  document.querySelectorAll('.quick-chips').forEach(el => el.remove());

  const commandText = text.trim().replace(/[.。]+$/, '');
  if (commandText === 'Kartik_Train##') {
    appendUserMessage(text);
    enterTrainingMode();
    return;
  }
  if (commandText === 'Kartik_Train@@') {
    appendUserMessage(text);
    exitTrainingMode();
    return;
  }
  if (trainingMode) {
    appendUserMessage(text);
    await handleTrainingMessage(text);
    return;
  }

  appendUserMessage(text);
  if (demoBooked && isRescheduleIntent(text)) {
    appendBotMessage('Sure, let\'s update your demo details. Please fill in your new preferred date and time.');
    demoFormActive = true;
    setTimeout(() => showDemoForm(true), 250);
    return;
  }
  if (isDemoIntent(text)) {
    if (demoBooked && bookedDemoDetails) {
      appendBotMessage(
        `Your demo is already confirmed for ${escapeHtml(bookedDemoDetails.date)} at ${escapeHtml(bookedDemoDetails.time)}. Our team will reach out shortly.`,
        ['Change date/time', 'What will be covered?', 'Something else']
      );
    } else if (!demoFormActive) {
      appendBotMessage('Sure. Please fill this short card and our team will coordinate the demo with you.');
      demoFormActive = true;
      setTimeout(showDemoForm, 250);
    }
    return;
  }
  messages.push({ role: 'user', content: text });
  await streamBotReply();
}

function isDemoIntent(text) {
  return /\b(book|schedule|arrange|need|want|request)\b.*\b(demo|walkthrough|trial)\b|\b(demo|walkthrough)\b.*\b(book|schedule|arrange|request)\b/i.test(text);
}

function isRescheduleIntent(text) {
  return /\b(reschedule|rebook|change|update|modify|shift|move|cancel)\b.*\b(demo|time|date|slot|appointment|booking)\b|\b(demo|appointment|booking)\b.*\b(change|update|reschedule|modify|shift|move)\b/i.test(text);
}

// ─────────────────────────────────────────────
// TRAINING MODE
// ─────────────────────────────────────────────
function enterTrainingMode() {
  trainingMode = true;
  trainingStep = 1;
  trainingData = {};

  // Auto-capture last customer question + Aria's last response
  for (let i = messages.length - 1; i >= 0; i--) {
    if (messages[i].role === 'assistant' && !trainingData.botResponseGiven) {
      trainingData.botResponseGiven = messages[i].content;
    }
    if (messages[i].role === 'user' && trainingData.botResponseGiven) {
      trainingData.customerQuestion = messages[i].content;
      break;
    }
  }

  trainingBanner = document.createElement('div');
  trainingBanner.id = 'training-banner';
  trainingBanner.innerHTML = '<strong>Training Mode Active</strong>, feedback saved for admin review. Type <code>Kartik_Train@@</code> to exit.';

  const chatScreen = document.getElementById('chat-screen');
  chatScreen.insertBefore(trainingBanner, messagesScroll);

  const preview = trainingData.botResponseGiven
    ? `I've captured KDK Sales' last response for feedback.\n\n**Customer asked:** "${(trainingData.customerQuestion || '').slice(0, 120)}"\n\n**KDK Sales said:** "${trainingData.botResponseGiven.slice(0, 200)}${trainingData.botResponseGiven.length > 200 ? '...' : ''}"\n\nWhat should the correct answer have been? Write in any language, no grammar needed.`
    : 'Training mode activated. No recent response found, please scroll to the wrong response and re-enter training mode.\n\nType **Kartik_Train@@** to exit.';

  appendTrainingBotMessage(preview);
  if (!trainingData.botResponseGiven) { trainingStep = 0; }
}

function exitTrainingMode() {
  trainingMode = false;
  trainingStep = 0;
  trainingData = {};
  if (trainingBanner) { trainingBanner.remove(); trainingBanner = null; }
  appendTrainingBotMessage('Training mode ended. Back to normal chat!');
}

async function handleTrainingMessage(text) {
  if (trainingStep !== 1) return;
  try {
    const res = await fetch('/api/training-feedback', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        sessionId:           SESSION_ID,
        submittedBy:         userProfile?.name || 'Unknown',
        userRole:            userProfile?.role || '',
        customerQuestion:    trainingData.customerQuestion || '',
        botResponseGiven:    trainingData.botResponseGiven || '',
        suggestedCorrection: text
      })
    });
    const data = await res.json();
    if (data.success) {
      appendTrainingBotMessage('Feedback saved! Admin will review it before it goes live.\n\nType **Kartik_Train@@** to go back to normal chat.');
    } else {
      appendTrainingBotMessage('Could not save. Please try again.');
    }
  } catch(e) {
    appendTrainingBotMessage('Connection error. Please try again.');
  }
  trainingMode = false;
  trainingStep = 0;
  trainingData = {};
  if (trainingBanner) { trainingBanner.remove(); trainingBanner = null; }
}

function appendTrainingBotMessage(text) {
  removeEmptyState();
  const wrapper = document.createElement('div');
  wrapper.className = 'msg-bot training';
  wrapper.innerHTML = `
    <div class="msg-bot-header">
      <div class="msg-bot-av">${KDK_ICON}</div>
      <span class="msg-bot-name">Training Mode</span>
      <span class="msg-bot-time">${now()}</span>
    </div>
    <div class="msg-bot-content">${renderMarkdown(text)}</div>`;
  messagesArea.appendChild(wrapper);
  scrollToBottom();
  // Intentionally not pushed to messages[], training messages never go to OpenAI.
}

// ─────────────────────────────────────────────
// STREAM BOT REPLY
// ─────────────────────────────────────────────
async function streamBotReply() {
  isStreaming = true;
  sendBtn.disabled = true;
  sendBtn.classList.add('sending');
  typingRow.classList.remove('hidden');
  if (voiceCallMode) setVcStatus('thinking');
  scrollToBottom();

  let accumulated = '';

  try {
    const resp = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        messages,
        userContext: userProfile || null,
        sessionId: SESSION_ID
      })
    });

    typingRow.classList.add('hidden');

    if (!resp.ok || !resp.body) {
      const details = await resp.text().catch(() => '');
      throw new Error(details || `Chat request failed with status ${resp.status}`);
    }

    const wrapper = document.createElement('div');
    wrapper.className = 'msg-bot';
    wrapper.innerHTML = `
      <div class="msg-bot-header">
        <div class="msg-bot-av">${KDK_ICON}</div>
        <span class="msg-bot-name">KDK Sales</span>
        <span class="msg-bot-time">${now()}</span>
      </div>
      <div class="msg-bot-content"></div>`;
    messagesArea.appendChild(wrapper);
    const contentEl = wrapper.querySelector('.msg-bot-content');
    scrollToBottom();

    const reader  = resp.body.getReader();
    const decoder = new TextDecoder();
    let buf = '';

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      buf += decoder.decode(value, { stream: true });
      const lines = buf.split('\n');
      buf = lines.pop();

      for (const line of lines) {
        if (!line.startsWith('data: ')) continue;
        const raw = line.slice(6).trim();
        if (!raw || raw === '[DONE]') continue;
        try {
          const parsed = JSON.parse(raw);
          if (parsed.error) {
            contentEl.innerHTML = `<em style="color:#EF4444">${escapeHtml(parsed.error)}</em>`;
            continue;
          }
          if (parsed.text) {
            accumulated += parsed.text;
            contentEl.innerHTML = renderMarkdown(stripTokens(accumulated));
            scrollToBottom();
          }
        } catch(e) {}
      }
    }

    if (!accumulated.trim()) {
      throw new Error('No response received from chat service.');
    }

    const parsedReply = parseTokens(accumulated);
    const clean = cleanResponseText(parsedReply.text);
    const { quickReplies, collectDemoInfo, escalateToHuman, offerCallback } = parsedReply;
    contentEl.innerHTML = renderMarkdown(clean);
    messages.push({ role: 'assistant', content: clean });
    speakText(clean);

    if (escalateToHuman) {
      setTimeout(showEscalationCard, 350);
    } else if (collectDemoInfo && demoBooked && bookedDemoDetails) {
      setTimeout(() => appendBotMessage(
        `Just a reminder — your demo is already confirmed for ${escapeHtml(bookedDemoDetails.date)} at ${escapeHtml(bookedDemoDetails.time)}. Our team will reach out to you.`,
        ['Change date/time', 'What will be covered?', 'Something else']
      ), 350);
    } else if (collectDemoInfo && !demoFormActive) {
      demoFormActive = true;
      setTimeout(showDemoForm, 350);
    } else if (offerCallback) {
      setTimeout(showCallbackCard, 350);
    } else if (quickReplies.length > 0) {
      wrapper.appendChild(buildQuickReplies(quickReplies));
    }

    scrollToBottom();

  } catch(e) {
    typingRow.classList.add('hidden');
    console.error('Chat error:', e);
    appendBotMessage('Having trouble connecting right now. Please check your internet and try again.');
  } finally {
    isStreaming = false;
    sendBtn.disabled = false;
    sendBtn.classList.remove('sending');
  }
}

// ─────────────────────────────────────────────
// DOM HELPERS, MESSAGES
// ─────────────────────────────────────────────
function appendBotMessage(text, quickReplies = []) {
  removeEmptyState();
  const wrapper = document.createElement('div');
  wrapper.className = 'msg-bot';
  wrapper.innerHTML = `
    <div class="msg-bot-header">
      <div class="msg-bot-av">${KDK_ICON}</div>
      <span class="msg-bot-name">KDK Sales</span>
      <span class="msg-bot-time">${now()}</span>
    </div>
    <div class="msg-bot-content">${renderMarkdown(text)}</div>`;
  if (quickReplies.length > 0) wrapper.appendChild(buildQuickReplies(quickReplies));
  messagesArea.appendChild(wrapper);
  scrollToBottom();
  messages.push({ role: 'assistant', content: text });
  speakText(text);
}

function appendUserMessage(text) {
  removeEmptyState();

  // Add to sidebar history on the first user message of this chat
  if (messages.filter(m => m.role === 'user').length === 0) {
    addToHistory(text.length > 35 ? text.substring(0, 35) + '…' : text);
  }

  const el = document.createElement('div');
  el.className = 'msg-user';
  el.innerHTML = `
    <div class="msg-user-bubble"><p>${escapeHtml(text)}</p></div>
    <span class="msg-user-time">${now()}</span>`;
  messagesArea.appendChild(el);
  scrollToBottom();
}

function buildQuickReplies(options) {
  const el = document.createElement('div');
  el.className = 'quick-chips';
  options.forEach(opt => {
    const chip = document.createElement('button');
    chip.className = 'qr-chip';
    chip.textContent = opt;
    chip.onclick = () => {
      document.querySelectorAll('.quick-chips').forEach(r => r.remove());
      handleUserMessage(opt);
    };
    el.appendChild(chip);
  });
  return el;
}

// ─────────────────────────────────────────────
// CHAT HISTORY
// ─────────────────────────────────────────────
function addToHistory(title) {
  const id = Date.now().toString();
  activeChatId = id;

  // Create or find "Today" group label
  let group = historyList.querySelector('[data-group="Today"]');
  if (!group) {
    const label = document.createElement('div');
    label.className = 'hist-group-label';
    label.textContent = 'Today';
    label.dataset.group = 'Today';
    historyList.insertBefore(label, historyList.firstChild);
    group = label;
  }

  // Mark all others inactive
  document.querySelectorAll('.hist-item').forEach(el => el.classList.remove('active'));

  const item = document.createElement('div');
  item.className = 'hist-item active';
  item.dataset.chatId = id;
  item.innerHTML = `
    <span class="hist-item-title">${escapeHtml(title)}</span>
    <button class="hist-item-del" onclick="deleteHistory(event,'${id}')" title="Delete">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round">
        <line x1="18" y1="6" x2="6" y2="18"/>
        <line x1="6" y1="6" x2="18" y2="18"/>
      </svg>
    </button>`;
  item.onclick = (e) => {
    if (!e.target.closest('.hist-item-del')) selectHistory(id, item);
  };

  // Insert directly after the group label
  group.insertAdjacentElement('afterend', item);

  // Store session snapshot
  chatSessions[id] = { id, title, messages: [...messages] };
  return id;
}

function selectHistory(id, el) {
  document.querySelectorAll('.hist-item').forEach(i => i.classList.remove('active'));
  el.classList.add('active');
  activeChatId = id;
  // Show a note that the session has ended (we don't store full DOM)
  messagesArea.innerHTML = '';
  const note = document.createElement('div');
  note.className = 'msg-bot';
  note.innerHTML = `
    <div class="msg-bot-header">
      <div class="msg-bot-av">${KDK_ICON}</div>
      <span class="msg-bot-name">KDK Sales</span>
    </div>
    <div class="msg-bot-content">This conversation has ended. <a href="#" onclick="newChat();return false;" style="color:var(--primary);font-weight:600;">Start a new chat</a> to continue.</div>`;
  messagesArea.appendChild(note);
  closeSidebar();
}

function deleteHistory(e, id) {
  e.stopPropagation();
  const item = historyList.querySelector(`[data-chat-id="${id}"]`);
  if (item) item.remove();
  delete chatSessions[id];
  if (activeChatId === id) {
    activeChatId = null;
  }
}

function filterHistory(query) {
  const q = query.toLowerCase();
  document.querySelectorAll('.hist-item').forEach(item => {
    const title = item.querySelector('.hist-item-title')?.textContent.toLowerCase() || '';
    item.style.display = title.includes(q) ? '' : 'none';
  });
}

// ─────────────────────────────────────────────
// NEW CHAT
// ─────────────────────────────────────────────
function newChat() {
  if (isStreaming) return;
  messages = [];
  demoFormActive = false;
  demoBooked = false;
  bookedDemoDetails = null;
  if (trainingBanner) { trainingBanner.remove(); trainingBanner = null; }
  trainingMode = false;
  trainingStep = 0;
  trainingData = {};
  messagesArea.innerHTML = '';
  activeChatId = null;
  document.querySelectorAll('.hist-item').forEach(el => el.classList.remove('active'));
  showEmptyState();
  closeSidebar();
  msgInput?.focus();
}

// ─────────────────────────────────────────────
// RESET CHAT (back to pre-chat modal)
// ─────────────────────────────────────────────
function resetChat() {
  if (isStreaming) return;
  messages = [];
  demoFormActive = false;
  demoBooked = false;
  bookedDemoDetails = null;
  userProfile = null;
  trainingMode = false;
  trainingStep = 0;
  trainingData = {};
  if (trainingBanner) { trainingBanner.remove(); trainingBanner = null; }
  messagesArea.innerHTML = '';
  historyList.innerHTML = '';
  chatSessions = {};
  activeChatId = null;
  document.getElementById('chat-screen').classList.add('hidden');
  document.getElementById('prechat-screen').classList.remove('pc-hidden');
  document.getElementById('pc-name').value = '';
  document.getElementById('pc-email').value = '';
  document.getElementById('pc-submit').textContent = 'Start Conversation →';
  document.getElementById('pc-submit').disabled = false;
}

// ─────────────────────────────────────────────
// DEMO FORM
// ─────────────────────────────────────────────
function showDemoForm(isUpdate = false) {
  const prefillName  = escapeHtml(userProfile?.name  || '');
  const prefillEmail = escapeHtml(userProfile?.email || '');
  const today = new Date().toISOString().split('T')[0];
  const headTitle = isUpdate ? 'Update Your Demo' : 'Book Your Free Demo';
  const headSub   = isUpdate ? 'Change your preferred date or time below' : '20 min · Personal walkthrough · No commitment';
  const btnLabel  = isUpdate ? 'Update Demo →' : 'Confirm My Demo →';

  const wrapper = document.createElement('div');
  wrapper.className = 'card-msg';
  wrapper.innerHTML = `
    <div class="inline-card">
      <div class="inline-card-head demo-head">
        <div class="card-head-title">
          <span class="card-mini-icon">${iconCalendar()}</span>
          ${headTitle}
        </div>
        <div class="card-head-sub">${headSub}</div>
      </div>
      <div class="inline-card-body">
        <div class="card-field">
          <label>Your Name *</label>
          <input type="text" id="d-name" value="${prefillName}" placeholder="e.g. Rahul Sharma">
        </div>
        <div class="card-field">
          <label>Phone Number *</label>
          <input type="tel" id="d-phone" placeholder="e.g. 98765 43210">
        </div>
        <div class="card-field">
          <label>Email Address *</label>
          <input type="email" id="d-email" value="${prefillEmail}" placeholder="e.g. rahul@firm.com">
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
          <div class="card-field" style="margin-bottom:0">
            <label>Preferred Date *</label>
            <input type="date" id="d-date" min="${today}" style="cursor:pointer">
          </div>
          <div class="card-field" style="margin-bottom:0">
            <label>Preferred Time *</label>
            <input type="time" id="d-time" placeholder="e.g. 14:00" style="cursor:pointer">
          </div>
        </div>
        <div class="card-field" style="margin-bottom:6px;margin-top:8px">
          <label style="margin-bottom:4px">Quick pick</label>
          <div class="time-slots">
            <div class="time-slot" onclick="selectTimeSlot(this,'10:00')">10 AM</div>
            <div class="time-slot" onclick="selectTimeSlot(this,'14:00')">2 PM</div>
            <div class="time-slot" onclick="selectTimeSlot(this,'17:00')">5 PM</div>
          </div>
        </div>
        <button class="card-submit demo-submit" id="d-submit" onclick="submitDemo(this)">
          ${btnLabel}
        </button>
        <p class="card-privacy">🔒 Your info is private. Our team will reach out personally.</p>
      </div>
    </div>`;
  messagesArea.appendChild(wrapper);
  scrollToBottom();
}

function selectTimeSlot(el, timeValue) {
  el.closest('.time-slots').querySelectorAll('.time-slot').forEach(s => s.classList.remove('selected'));
  el.classList.add('selected');
  const timeInput = document.getElementById('d-time');
  if (timeInput && timeValue) timeInput.value = timeValue;
}

function formatDemoDate(dateStr) {
  if (!dateStr) return '';
  const d = new Date(dateStr + 'T00:00:00');
  return d.toLocaleDateString('en-IN', { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' });
}

function formatTimeDisplay(timeStr) {
  if (!timeStr) return '';
  const [h, m] = timeStr.split(':').map(Number);
  const ampm = h >= 12 ? 'PM' : 'AM';
  const hour = h % 12 || 12;
  return m === 0 ? `${hour} ${ampm}` : `${hour}:${String(m).padStart(2, '0')} ${ampm}`;
}

async function submitDemo(btn) {
  const isUpdate = demoBooked;
  const name    = document.getElementById('d-name').value.trim();
  const email   = document.getElementById('d-email').value.trim();
  const phone   = document.getElementById('d-phone').value.trim();
  const company = '';
  const preferredDate  = document.getElementById('d-date').value;
  const rawTime        = document.getElementById('d-time').value;
  const timePreference = rawTime ? formatTimeDisplay(rawTime) : '';

  if (!name || !phone) { showToast('Please enter your name and phone number.'); return; }
  if (!email || !email.includes('@')) { showToast('Please enter a valid email address.'); return; }
  if (!preferredDate) { showToast('Please select a preferred date.'); return; }
  if (!timePreference) { showToast('Please enter a preferred time.'); return; }

  btn.textContent = isUpdate ? 'Updating...' : 'Booking...';
  btn.disabled = true;

  try {
    const res = await fetch('/api/book-demo', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email, phone, company, preferredDate, timePreference, role: userProfile?.role || '' })
    });
    const data = await res.json();

    if (data.success) {
      const formMsg = btn.closest('.card-msg');
      const successEl = document.createElement('div');
      successEl.className = 'card-msg';
      const cardTitle = isUpdate ? 'Demo Updated!' : 'Demo Confirmed!';
      const cardSub   = isUpdate
        ? `Hi <strong>${escapeHtml(name.split(' ')[0])}</strong>! Your demo has been rescheduled to <strong>${escapeHtml(formatDemoDate(preferredDate))}, ${escapeHtml(timePreference)}</strong>.<br>We'll confirm at <strong>${escapeHtml(phone)}</strong> and send an update to <strong>${escapeHtml(email)}</strong>.`
        : `Hi <strong>${escapeHtml(name.split(' ')[0])}</strong>! Your demo is scheduled for <strong>${escapeHtml(formatDemoDate(preferredDate))}, ${escapeHtml(timePreference)}</strong>.<br>We'll confirm at <strong>${escapeHtml(phone)}</strong> and send a confirmation to <strong>${escapeHtml(email)}</strong>.`;
      successEl.innerHTML = `
        <div class="inline-card card-success">
          <div class="success-icon-wrap">${iconCalendar()}</div>
          <div class="success-card-title">${cardTitle}</div>
          <div class="success-card-sub">${cardSub}</div>
        </div>`;
      formMsg.replaceWith(successEl);
      fetchDemoCount();
      demoBooked = true;
      bookedDemoDetails = { date: formatDemoDate(preferredDate), time: timePreference };
      messages.push({ role: 'assistant', content: `Demo ${isUpdate ? 'rescheduled' : 'booked'} for ${bookedDemoDetails.date} at ${bookedDemoDetails.time}. Confirmation sent to ${email}.` });

      setTimeout(() => {
        const firstName = name.split(' ')[0];
        const followUp = isUpdate
          ? `Done, ${escapeHtml(firstName)}! Your demo has been updated to ${escapeHtml(bookedDemoDetails.date)} at ${escapeHtml(bookedDemoDetails.time)}. An updated confirmation has been sent to ${escapeHtml(email)}. Is there anything else I can help with?`
          : `You're all set, ${escapeHtml(firstName)}! Your demo is confirmed for ${escapeHtml(bookedDemoDetails.date)} at ${escapeHtml(bookedDemoDetails.time)}. A confirmation has been sent to ${escapeHtml(email)}.\n\nIs there anything specific you'd like us to cover — a particular product, a feature, or a competitor comparison?`;
        const chips = isUpdate
          ? ['What will be covered?', 'Something else']
          : ['Walk me through Express GST', 'How does it compare to competitors?', 'How does migration work?'];
        appendBotMessage(followUp, chips);
        demoFormActive = false;
      }, 700);
    }
  } catch(e) {
    btn.textContent = isUpdate ? 'Update Demo →' : 'Confirm My Demo →';
    btn.disabled = false;
    showToast('Something went wrong. Please try again.');
  }
}

// ─────────────────────────────────────────────
// ESCALATION CARD
// ─────────────────────────────────────────────
function showEscalationCard() {
  const prefillName = escapeHtml(userProfile?.name || '');
  const wrapper = document.createElement('div');
  wrapper.className = 'card-msg';
  wrapper.innerHTML = `
    <div class="inline-card">
      <div class="inline-card-head escalation-head">
        <div class="card-head-title">
          <span class="card-mini-icon">${iconPhone()}</span>
          Connect With Our Senior Team
        </div>
        <div class="card-head-sub">Share your number and we'll call you right away</div>
      </div>
      <div class="inline-card-body">
        <div class="card-field">
          <label>Your Name *</label>
          <input type="text" id="esc-name" value="${prefillName}" placeholder="Your name">
        </div>
        <div class="card-field">
          <label>Phone Number *</label>
          <input type="tel" id="esc-phone" placeholder="e.g. 98765 43210">
        </div>
        <div class="card-field">
          <label>Best Time to Call</label>
          <select id="esc-time">
            <option>Morning (9am to 12pm)</option>
            <option>Afternoon (12pm to 4pm)</option>
            <option>Evening (4pm to 7pm)</option>
          </select>
        </div>
        <button class="card-submit escalation-submit" onclick="submitEscalation(this)">
          Request Callback
        </button>
      </div>
    </div>`;
  messagesArea.appendChild(wrapper);
  scrollToBottom();
}

async function submitEscalation(btn) {
  const name  = document.getElementById('esc-name').value.trim();
  const phone = document.getElementById('esc-phone').value.trim();
  const time  = document.getElementById('esc-time').value;

  if (!name || !phone) { showToast('Please enter your name and phone number.'); return; }

  btn.textContent = 'Requesting...';
  btn.disabled = true;

  try {
    await fetch('/api/request-callback', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, phone, timePreference: time, type: 'escalation', role: userProfile?.role || '' })
    });

    const formMsg = btn.closest('.card-msg');
    const successEl = document.createElement('div');
    successEl.className = 'card-msg';
    successEl.innerHTML = `
      <div class="inline-card card-success">
        <div class="success-icon-wrap">${iconPhone()}</div>
        <div class="success-card-title">You're all set!</div>
        <div class="success-card-sub">
          Our senior expert will call <strong>${escapeHtml(phone)}</strong> during <strong>${escapeHtml(time)}</strong>. You won't have to repeat yourself, we'll have the full context ready.
        </div>
      </div>`;
    formMsg.replaceWith(successEl);
    scrollToBottom();

    setTimeout(() => {
      appendBotMessage(
        "Our senior product expert will be in touch very shortly. Is there anything specific you'd like them to cover on the call?",
        ['Product pricing details', 'Migration from existing software', 'Feature walkthrough']
      );
    }, 600);
  } catch(e) {
    btn.textContent = 'Request Callback';
    btn.disabled = false;
    showToast('Something went wrong. Please try again.');
  }
}

// ─────────────────────────────────────────────
// CALLBACK CARD
// ─────────────────────────────────────────────
function showCallbackCard() {
  const prefillName = escapeHtml(userProfile?.name || '');
  const wrapper = document.createElement('div');
  wrapper.className = 'card-msg';
  wrapper.innerHTML = `
    <div class="inline-card">
      <div class="inline-card-head callback-head">
        <div class="card-head-title">
          <span class="card-mini-icon">${iconPhone()}</span>
          Quick Callback
        </div>
        <div class="card-head-sub">Leave your number and we'll call you back shortly</div>
      </div>
      <div class="inline-card-body">
        <div class="card-field">
          <label>Your Name *</label>
          <input type="text" id="cb-name" value="${prefillName}" placeholder="Your name">
        </div>
        <div class="card-field">
          <label>Phone Number *</label>
          <input type="tel" id="cb-phone" placeholder="e.g. 98765 43210">
        </div>
        <button class="card-submit" onclick="submitCallback(this)">
          Call Me Back
        </button>
      </div>
    </div>`;
  messagesArea.appendChild(wrapper);
  scrollToBottom();
}

async function submitCallback(btn) {
  const name  = document.getElementById('cb-name').value.trim();
  const phone = document.getElementById('cb-phone').value.trim();

  if (!name || !phone) { showToast('Please enter your name and phone number.'); return; }

  btn.textContent = 'Requesting...';
  btn.disabled = true;

  try {
    await fetch('/api/request-callback', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, phone, type: 'callback', role: userProfile?.role || '' })
    });

    const formMsg = btn.closest('.card-msg');
    const successEl = document.createElement('div');
    successEl.className = 'card-msg';
    successEl.innerHTML = `
      <div class="inline-card card-success">
        <div class="success-icon-wrap">${iconPhone()}</div>
        <div class="success-card-title">We'll call you back!</div>
        <div class="success-card-sub">
          Expect a call at <strong>${escapeHtml(phone)}</strong> from our team very shortly.
        </div>
      </div>`;
    formMsg.replaceWith(successEl);
    scrollToBottom();
  } catch(e) {
    btn.textContent = 'Call Me Back';
    btn.disabled = false;
    showToast('Something went wrong. Please try again.');
  }
}

// ─────────────────────────────────────────────
// QUICK ACTIONS
// ─────────────────────────────────────────────
function quickAsk(text) {
  if (isStreaming) return;
  if (!userProfile) { showToast('Please introduce yourself first.'); return; }
  handleUserMessage(text);
}

function triggerDemo() {
  if (isStreaming) return;
  if (!userProfile) { showToast('Please introduce yourself first.'); return; }
  handleUserMessage("I'd like to book a free demo");
}

// ─────────────────────────────────────────────
// ICON HELPERS
// ─────────────────────────────────────────────
function iconStack() {
  return `<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M12 4 4 8l8 4 8-4-8-4Z" fill="currentColor" opacity=".28"/><path d="m4 12 8 4 8-4M4 16l8 4 8-4" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>`;
}

function iconFlow() {
  return `<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M7 7h10v10H7z" fill="currentColor" opacity=".22"/><path d="M7 7h10v10H7zM3 12h4M17 12h4M12 3v4M12 17v4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
}

function iconChart() {
  return `<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M5 19V5h14v14H5Z" fill="currentColor" opacity=".20"/><path d="M8 16v-4M12 16V8M16 16v-6M5 19h14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>`;
}

function iconBundle() {
  return `<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M12 3 4 7.5v9L12 21l8-4.5v-9L12 3Z" fill="currentColor" opacity=".22"/><path d="M12 3 4 7.5m8-4.5 8 4.5M4 7.5l8 4.5m-8-4.5v9L12 21m0-9 8-4.5M12 12v9m8-13.5v9L12 21" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>`;
}

function iconCalendar() {
  return `<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M5 7h14v12H5z" fill="currentColor" opacity=".22"/><path d="M7 3v4M17 3v4M5 10h14M5 7h14v12H5z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
}

function iconPhone() {
  return `<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M8 5h3l2 5-2.5 1.5a12 12 0 0 0 5 5L17 14l4 2v3c0 1.1-.9 2-2 2A16 16 0 0 1 3 5c0-1.1.9-2 2-2h3v2Z" fill="currentColor" opacity=".24"/><path d="M8 5h3l2 5-2.5 1.5a12 12 0 0 0 5 5L17 14l4 2v3c0 1.1-.9 2-2 2A16 16 0 0 1 3 5c0-1.1.9-2 2-2h3v2Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>`;
}

function iconChat() {
  return `<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M4.5 7.5A4.5 4.5 0 0 1 9 3h6a4.5 4.5 0 0 1 4.5 4.5v4A4.5 4.5 0 0 1 15 16h-3.8L6.6 20.1c-.7.6-1.8.1-1.8-.8V15.7A4.5 4.5 0 0 1 4.5 7.5Z" fill="currentColor" opacity=".22"/><path d="M8 9h8M8 12h5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>`;
}

// ─────────────────────────────────────────────
// PARSE SPECIAL TOKENS
// ─────────────────────────────────────────────
function parseTokens(text) {
  let quickReplies    = [];
  let collectDemoInfo = false;
  let escalateToHuman = false;
  let offerCallback   = false;

  const qrMatch = text.match(/QUICK_REPLIES:\[([^\]]+)\]/s);
  if (qrMatch) {
    try {
      quickReplies = JSON.parse('[' + qrMatch[1] + ']');
    } catch(e) {
      quickReplies = qrMatch[1]
        .split('","')
        .map(s => s.replace(/^["'\s]+|["'\s]+$/g, ''))
        .filter(Boolean);
    }
    text = text.replace(/QUICK_REPLIES:\[[^\]]*\]/gs, '').trim();
  }

  if (text.includes('COLLECT_DEMO_INFO:true') || text.includes('SHOW_DEMO_CARD:true')) {
    collectDemoInfo = true;
    text = text.replace(/COLLECT_DEMO_INFO:true/g, '').replace(/SHOW_DEMO_CARD:true/g, '').trim();
  }

  if (text.includes('ESCALATE_TO_HUMAN:true')) {
    escalateToHuman = true;
    text = text.replace(/ESCALATE_TO_HUMAN:true/g, '').trim();
  }

  if (text.includes('OFFER_CALLBACK:true')) {
    offerCallback = true;
    text = text.replace(/OFFER_CALLBACK:true/g, '').trim();
  }

  return { text, quickReplies, collectDemoInfo, escalateToHuman, offerCallback };
}

function cleanResponseText(text) {
  return String(text)
    .replace(/[—–]/g, ', ')
    .replace(/â€”/g, ', ')
    .replace(/\s+,/g, ',')
    .replace(/,\s*,+/g, ', ')
    .replace(/[ \t]{2,}/g, ' ')
    .trim();
}

function stripTokens(text) {
  return cleanResponseText(text
    .replace(/QUICK_REPLIES:\[[^\]]*\]?/gs, '')
    .replace(/COLLECT_DEMO_INFO:true/g, '')
    .replace(/SHOW_DEMO_CARD:true/g, '')
    .replace(/ESCALATE_TO_HUMAN:true/g, '')
    .replace(/OFFER_CALLBACK:true/g, '')
    .trim());
}

// ─────────────────────────────────────────────
// MARKDOWN RENDERER
// ─────────────────────────────────────────────
function renderMarkdown(raw) {
  const safe = escapeHtml(cleanResponseText(raw));
  const lines = safe.split('\n');
  const out = [];
  let pending = [];
  let inUl = false;
  let inOl = false;

  function flushPending() {
    const text = pending.join('\n').trim();
    if (text) out.push(`<p>${text.replace(/\n/g, '<br>')}</p>`);
    pending = [];
  }
  function closeLists() {
    if (inUl) { out.push('</ul>'); inUl = false; }
    if (inOl) { out.push('</ol>'); inOl = false; }
  }

  for (const line of lines) {
    const t = line.trim();

    if (!t) { flushPending(); closeLists(); continue; }
    if (/^#{1,2} /.test(t)) {
      flushPending(); closeLists();
      out.push(`<p class="msg-h">${t.replace(/^#{1,2} /, '')}</p>`);
      continue;
    }
    if (/^### /.test(t)) {
      flushPending(); closeLists();
      out.push(`<p class="msg-h3">${t.slice(4)}</p>`);
      continue;
    }
    if (/^-{3,}$/.test(t) || /^\*{3,}$/.test(t)) {
      flushPending(); closeLists();
      out.push('<hr class="msg-hr">');
      continue;
    }
    if (/^[-*•] /.test(t)) {
      flushPending();
      if (inOl) { out.push('</ol>'); inOl = false; }
      if (!inUl) { out.push('<ul class="msg-ul">'); inUl = true; }
      out.push(`<li>${t.slice(2)}</li>`);
      continue;
    }
    if (/^\d+\. /.test(t)) {
      flushPending();
      closeLists();
      const number = t.match(/^(\d+)\. /)?.[1] || '1';
      out.push(`<div class="msg-num"><span class="msg-num-index">${number}.</span><span>${t.replace(/^\d+\. /, '')}</span></div>`);
      continue;
    }
    closeLists();
    pending.push(t);
  }
  flushPending();
  closeLists();

  let result = out.join('');
  result = result.replace(/\*\*(.+?)\*\*/gs, '<strong>$1</strong>');
  result = result.replace(/(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)/gs, '<em>$1</em>');
  result = result.replace(/`([^`]+)`/g, '<code class="msg-code">$1</code>');
  return result;
}

function escapeHtml(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// ─────────────────────────────────────────────
// UTILS
// ─────────────────────────────────────────────
function scrollToBottom() {
  messagesScroll.scrollTop = messagesScroll.scrollHeight;
}

function now() {
  return new Date().toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit', hour12: true });
}

async function fetchDemoCount() {
  /* no-op: demo counter element removed from UI */
}

function showToast(msg) {
  const t = document.createElement('div');
  t.className = 'toast';
  t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(() => { t.style.opacity = '0'; t.style.transition = 'opacity 0.3s'; }, 2500);
  setTimeout(() => t.remove(), 2800);
}

// ─────────────────────────────────────────────
// VOICE (browser SpeechRecognition — no API key, silence detection built-in)
// ─────────────────────────────────────────────
let recognition    = null;
let resultReceived = false;

function toggleMic() {
  if (voiceCallMode) endVoiceCall();
  else startVoiceCall();
}

// Single function used for both call mode and one-off input
function startVoiceRecording() {
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SR) {
    showToast('Voice input requires Chrome or Edge browser.');
    if (voiceCallMode) endVoiceCall();
    return;
  }

  resultReceived = false;
  recognition = new SR();
  recognition.lang = 'en-IN';
  recognition.continuous = false;
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  recognition.onstart = () => {
    isRecording = true;
    if (voiceCallMode) {
      setVcStatus('listening');
    } else {
      if (micBtn)    micBtn.classList.add('recording');
      if (voiceBar)  voiceBar.classList.add('active');
      if (voiceLabel) voiceLabel.textContent = 'Listening...';
    }
  };

  recognition.onresult = (event) => {
    resultReceived = true;
    const text = event.results[0][0].transcript.trim();
    if (!text) return;

    if (voiceCallMode) {
      setVcStatus('thinking');
      handleUserMessage(text);
    } else {
      // One-off mode: put text in input box, user can review then send
      msgInput.value = text;
      msgInput.style.height = 'auto';
      msgInput.style.height = Math.min(msgInput.scrollHeight, 130) + 'px';
      msgInput.focus();
      if (voiceBar)  voiceBar.classList.remove('active');
      if (micBtn)    micBtn.classList.remove('recording');
    }
  };

  recognition.onerror = (event) => {
    if (event.error === 'not-allowed') {
      showToast('Microphone access denied. Allow it in browser settings.');
      if (voiceCallMode) endVoiceCall();
    }
    // 'no-speech' and other errors handled in onend
  };

  recognition.onend = () => {
    isRecording = false;
    if (!voiceCallMode) {
      if (micBtn)   micBtn.classList.remove('recording');
      if (voiceBar) voiceBar.classList.remove('active');
    }
    // In call mode, if no speech was detected, restart listening
    if (voiceCallMode && !resultReceived) {
      setTimeout(() => { if (voiceCallMode) startVoiceRecording(); }, 300);
    }
  };

  try {
    recognition.start();
  } catch(e) {
    showToast('Could not start voice. Try clicking the mic again.');
    if (voiceCallMode) endVoiceCall();
  }
}

function stopVoiceRecording() {
  if (recognition) {
    try { recognition.abort(); } catch(e) {}
    recognition = null;
  }
  isRecording = false;
  if (voiceCallMode) setVcStatus('processing');
}

// ─────────────────────────────────────────────
// VOICE OUTPUT (Web Speech TTS)
// ─────────────────────────────────────────────
function toggleTTS() {
  ttsEnabled = !ttsEnabled;
  document.querySelectorAll('.tts-btn').forEach(b => {
    b.classList.toggle('tts-on', ttsEnabled);
    b.title = ttsEnabled ? 'Voice: ON' : 'Voice: OFF';
    b.setAttribute('aria-label', ttsEnabled ? 'Turn off voice responses' : 'Turn on voice responses');
  });
  if (!ttsEnabled && currentAudio) { currentAudio.pause(); currentAudio = null; }
  showToast(ttsEnabled ? 'Voice responses enabled' : 'Voice responses disabled');
}

// ─────────────────────────────────────────────
// VOICE CALL MODE
// ─────────────────────────────────────────────
function startVoiceCall() {
  voiceCallMode = true;
  ttsEnabled    = true;

  document.getElementById('vc-overlay').classList.remove('hidden');
  if (micBtn) { micBtn.classList.add('active'); micBtn.title = 'End voice conversation'; }

  // Start timer
  vcSeconds = 0;
  vcTimerInterval = setInterval(() => {
    vcSeconds++;
    const m = Math.floor(vcSeconds / 60);
    const s = vcSeconds % 60;
    const el = document.getElementById('vc-timer');
    if (el) el.textContent = `${m}:${String(s).padStart(2, '0')}`;
  }, 1000);

  startVoiceRecording();
}

function endVoiceCall() {
  voiceCallMode = false;
  ttsEnabled    = false;

  clearInterval(vcTimerInterval);
  vcTimerInterval = null;

  if (currentAudio) { currentAudio.pause(); currentAudio = null; }

  // Stop SpeechRecognition if active
  stopVoiceRecording();
  isRecording = false;

  document.getElementById('vc-overlay').classList.add('hidden');
  if (micBtn) { micBtn.classList.remove('active', 'recording', 'processing'); micBtn.title = 'Voice conversation'; }
}

function setVcStatus(state) {
  const statusEl = document.getElementById('vc-status');
  const waveEl   = document.getElementById('vc-wave');
  if (!statusEl || !waveEl) return;

  const map = {
    listening:  { label: 'Listening...',  cls: 'listening'  },
    processing: { label: 'Processing...', cls: 'processing' },
    thinking:   { label: 'Thinking...',   cls: 'thinking'   },
    speaking:   { label: 'Speaking...',   cls: 'speaking'   },
  };
  const s = map[state] || map.listening;
  statusEl.textContent = s.label;
  statusEl.className   = `vc-status ${s.cls}`;
  waveEl.className     = `vc-wave ${['listening','speaking'].includes(state) ? state : ''}`;
}

async function speakText(text) {
  if (!ttsEnabled) return;
  const plain = text
    .replace(/\*\*(.+?)\*\*/g, '$1')
    .replace(/\*(.+?)\*/g, '$1')
    .replace(/`([^`]+)`/g, '$1')
    .replace(/^#{1,3} /gm, '')
    .replace(/^[-*•] /gm, '')
    .replace(/^\d+\. /gm, '')
    .replace(/^-{3,}$/gm, '')
    .replace(/\n+/g, ' ')
    .trim();
  if (!plain) return;

  if (currentAudio) { currentAudio.pause(); URL.revokeObjectURL(currentAudio._url); currentAudio = null; }

  try {
    const res = await fetch('/api/tts', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: plain })
    });
    if (!res.ok) { console.error('TTS error:', res.status); return; }

    const blob = await res.blob();
    const url  = URL.createObjectURL(blob);
    const audio = new Audio(url);
    audio._url  = url;
    currentAudio = audio;
    if (voiceCallMode) setVcStatus('speaking');
    audio.onended = () => {
      URL.revokeObjectURL(url);
      currentAudio = null;
      if (voiceCallMode) {
        setVcStatus('listening');
        setTimeout(() => { if (voiceCallMode && !isRecording) startVoiceRecording(); }, 400);
      }
    };
    const p = audio.play();
    if (p) p.catch(e => console.error('Audio play blocked:', e));
  } catch(e) {
    console.error('TTS failed:', e);
  }
}
