// Часы
function updateClock() {
    const now = new Date();
    const h = String(now.getHours()).padStart(2,'0');
    const m = String(now.getMinutes()).padStart(2,'0');
    const s = String(now.getSeconds()).padStart(2,'0');
    const clock = document.getElementById('clock');
    if(clock) clock.innerText = `Текущее время: ${h}:${m}:${s}`;
}
setInterval(updateClock, 1000);
updateClock();
