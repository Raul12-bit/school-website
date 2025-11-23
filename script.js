



// ====== Переводы ======
const translations = {
    kk: {
        home: "Басты бет",
        about: "Мектеп туралы",
        schedule: "Сабақ кестесі",
        news: "Жаңалықтар",
        "hero-title": "Қош келдіңіз!",
        "hero-subtitle": "Білім мен жетістік жолындағы заманауи мектеп порталы",
        "card-about": "Мектеп туралы",
        "card-about-text": "Тарихы, мұғалімдер, жетістіктер.",
        "card-schedule": "Сабақ кестесі",
        "card-schedule-text": "Жаңартылған күнделікті сабақтар.",
        "card-news": "Жаңалықтар",
        "card-news-text": "Мектеп ішіндегі соңғы ақпараттар."
    },
    ru: {
        home: "Главная",
        about: "О школе",
        schedule: "Расписание",
        news: "Новости",
        "hero-title": "Добро пожаловать!",
        "hero-subtitle": "Современный школьный портал на пути знаний и успеха",
        "card-about": "О школе",
        "card-about-text": "История, учителя, достижения.",
        "card-schedule": "Расписание",
        "card-schedule-text": "Обновленное ежедневное расписание.",
        "card-news": "Новости",
        "card-news-text": "Последняя информация из школы."
    },
    en: {
        home: "Home",
        about: "About School",
        schedule: "Schedule",
        news: "News",
        "hero-title": "Welcome!",
        "hero-subtitle": "Modern school portal on the path of knowledge and success",
        "card-about": "About School",
        "card-about-text": "History, teachers, achievements.",
        "card-schedule": "Schedule",
        "card-schedule-text": "Updated daily schedule.",
        "card-news": "News",
        "card-news-text": "Latest information from the school."
    }
};

// ====== Theme Toggle ======
const themeToggle = document.getElementById("themeToggle");

function setTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    themeToggle.textContent = theme === "light" ? "🌙" : "☀️";
    localStorage.setItem("theme", theme);
}

// Инициализация темы при загрузке
window.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("theme") || "light";
    setTheme(savedTheme);
});

// Смена темы при клике
themeToggle.addEventListener("click", () => {
    const currentTheme = document.documentElement.getAttribute("data-theme");
    setTheme(currentTheme === "light" ? "dark" : "light");
});

// ====== Language Switch ======
const languageSelectors = document.querySelectorAll("#languageSelector");

function setLanguage(lang) {
    const elements = document.querySelectorAll("[data-key], [id]");
    elements.forEach(el => {
        const key = el.dataset.key || el.id;
        if (translations[lang] && translations[lang][key]) {
            el.textContent = translations[lang][key];
        }
    });
    languageSelectors.forEach(sel => sel.value = lang);
    localStorage.setItem("language", lang);
}

// Смена языка
languageSelectors.forEach(sel => {
    sel.addEventListener("change", (e) => {
        setLanguage(e.target.value);
    });
});

// Инициализация языка
window.addEventListener("DOMContentLoaded", () => {
    const savedLanguage = localStorage.getItem("language") || "kk";
    setLanguage(savedLanguage);
});
