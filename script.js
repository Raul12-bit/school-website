document.addEventListener("DOMContentLoaded", function() {
    const data = {
        kk: {
            title: "№2 Орта Мектеп",
            subtitle: "Білім мен жетістік жолында!",
            "nav-main": "Басты бет",
            "nav-about": "Мектеп туралы",
            "nav-schedule": "Сабақ кестесі",
            "nav-teachers": "Мұғалімдер",
            "nav-news": "Жаңалықтар",
            "nav-contacts": "Байланыс",
            "home-title": "Қош келдіңіз!",
            "home-text": "№2 орта мектеп сайтына қош келдіңіз. Мұнда мектеп жаңалықтары, сабақ кестесі және мұғалімдер туралы ақпарат таба аласыз.",
            "footer-text": "© 2025 №2 орта мектеп. Барлық құқықтар қорғалған."
        },
        ru: {
            title: "Средняя школа №2",
            subtitle: "На пути к знаниям и успеху!",
            "nav-main": "Главная",
            "nav-about": "О школе",
            "nav-schedule": "Расписание",
            "nav-teachers": "Учителя",
            "nav-news": "Новости",
            "nav-contacts": "Контакты",
            "home-title": "Добро пожаловать!",
            "home-text": "Добро пожаловать на сайт средней школы №2. Здесь вы найдете новости школы, расписание и информацию о учителях.",
            "footer-text": "© 2025 Средняя школа №2. Все права защищены."
        },
        en: {
            title: "Secondary School No. 2",
            subtitle: "On the path to knowledge and success!",
            "nav-main": "Main",
            "nav-about": "About",
            "nav-schedule": "Schedule",
            "nav-teachers": "Teachers",
            "nav-news": "News",
            "nav-contacts": "Contacts",
            "home-title": "Welcome!",
            "home-text": "Welcome to the website of Secondary School No. 2. Here you can find school news, class schedule, and information about teachers.",
            "footer-text": "© 2025 Secondary School No. 2. All rights reserved."
        }
    };

    const langSelect = document.getElementById("langSelect");

    function updateLang(lang) {
        const t = data[lang];
        for (let key in t) {
            const el = document.getElementById(key);
            if (el) el.innerHTML = t[key];
        }
    }

    const savedLang = localStorage.getItem("lang") || "kk";
    langSelect.value = savedLang;
    updateLang(savedLang);

    langSelect.addEventListener("change", () => {
        const lang = langSelect.value;
        localStorage.setItem("lang", lang);
        updateLang(lang);
    });

    // Ночной режим
    const themeToggle = document.getElementById('theme-toggle');
    if(localStorage.getItem('nightMode') === 'true'){
        document.body.classList.add('night');
        themeToggle.textContent = '☀';
    } else {
        themeToggle.textContent = '🌙';
    }

    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('night');
        if(document.body.classList.contains('night')){
            themeToggle.textContent = '☀';
            localStorage.setItem('nightMode', 'true');
        } else {
            themeToggle.textContent = '🌙';
            localStorage.setItem('nightMode', 'false');
        }
    });
});
