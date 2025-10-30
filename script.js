const data = {
    kk: {
        title: "№2 Орта Мектеп",
        subtitle: "Білім мен жетістік жолында!",
        "nav-about": "Мектеп туралы",
        "nav-schedule": "Сабақ кестесі",
        "nav-teachers": "Мұғалімдер",
        "nav-news": "Жаңалықтар",
        "nav-contacts": "Байланыс",
        "about-title": "Мектеп туралы",
        "about-text": "№2 орта мектеп — бұл 800-ден астам оқушы білім алатын заманауи білім ордасы. Мұнда білім, спорт және шығармашылық тең дамиды.",
        "schedule-title": "Сабақ кестесі",
        schedule: `
        <table border="1" cellpadding="8" cellspacing="0" style="width:100%; text-align:center; background-color:rgba(0,0,0,0.3); color:white; border-collapse:collapse;">
            <tr><th>Сынып</th><th>Дүйсенбі</th><th>Сейсенбі</th><th>Сәрсенбі</th><th>Бейсенбі</th><th>Жұма</th></tr>
            <tr><td>5 "А"</td><td>Математика</td><td>Қазақ тілі</td><td>Ағылшын</td><td>Дене шынықтыру</td><td>Информатика</td></tr>
            <tr><td>6 "Б"</td><td>Физика</td><td>Орыс тілі</td><td>Биология</td><td>География</td><td>Математика</td></tr>
        </table>`,
        "teachers-title": "Мұғалімдер және пәндер",
        teachers: [
            "Айман Сұлтанқызы — Қазақ тілі мен әдебиеті",
            "Ержан Бақытбекұлы — Математика",
            "Гүлжан Әлімбекова — Биология",
            "Марина Петровна — Орыс тілі",
            "John Adams — Ағылшын тілі"
        ],
        "news-title": "Жаңалықтар",
        news: [
            "1 қарашада мектепте күзгі концерт өтеді.",
            "5–11 сыныптар арасында спорт апталығы басталды.",
            "Жаңа информатика кабинеті ашылды!"
        ],
        "contacts-title": "Байланыс және әлеуметтік желілер",
        "contacts-text": `Мекенжай: Қазақстан, Алматы қ., Білім көшесі 12<br>
            Телефон: +7 (701) 123-45-67<br><br>
            Әлеуметтік желілер:<br>
            📘 <a href="#">Facebook</a> | 📸 <a href="#">Instagram</a> | 🎥 <a href="#">YouTube</a>`,
        "footer-text": "© 2025 №2 орта мектеп. Барлық құқықтар қорғалған."
    },
    ru: {
        title: "Средняя школа №2",
        subtitle: "На пути к знаниям и успеху!",
        "nav-about": "О школе",
        "nav-schedule": "Расписание",
        "nav-teachers": "Учителя",
        "nav-news": "Новости",
        "nav-contacts": "Контакты",
        "about-title": "О школе",
        "about-text": "Средняя школа №2 — современное учебное заведение, где обучается более 800 учеников. Здесь гармонично сочетаются знания, спорт и творчество.",
        "schedule-title": "Расписание уроков",
        schedule: `
        <table border="1" cellpadding="8" cellspacing="0" style="width:100%; text-align:center; background-color:rgba(0,0,0,0.3); color:white;">
            <tr><th>Класс</th><th>Понедельник</th><th>Вторник</th><th>Среда</th><th>Четверг</th><th>Пятница</th></tr>
            <tr><td>5 "А"</td><td>Математика</td><td>Русский язык</td><td>Английский</td><td>Физкультура</td><td>Информатика</td></tr>
            <tr><td>6 "Б"</td><td>Физика</td><td>Казахский язык</td><td>Биология</td><td>География</td><td>Математика</td></tr>
        </table>`,
        "teachers-title": "Учителя и предметы",
        teachers: [
            "Айман Султановна — Казахский язык и литература",
            "Ержан Бакытбекович — Математика",
            "Гульжан Алимбекова — Биология",
            "Марина Петровна — Русский язык",
            "John Adams — Английский язык"
        ],
        "news-title": "Новости",
        news: [
            "1 ноября в школе пройдет осенний концерт.",
            "Началась спортивная неделя среди 5–11 классов.",
            "Открылся новый кабинет информатики!"
        ],
        "contacts-title": "Контакты и социальные сети",
        "contacts-text": `Адрес: Казахстан, г. Алматы, ул. Білім 12<br>
            Телефон: +7 (701) 123-45-67<br><br>
            Социальные сети:<br>
            📘 <a href="#">Facebook</a> | 📸 <a href="#">Instagram</a> | 🎥 <a href="#">YouTube</a>`,
        "footer-text": "© 2025 Средняя школа №2. Все права защищены."
    },
    en: {
        title: "Secondary School No. 2",
        subtitle: "On the path to knowledge and success!",
        "nav-about": "About",
        "nav-schedule": "Schedule",
        "nav-teachers": "Teachers",
        "nav-news": "News",
        "nav-contacts": "Contacts",
        "about-title": "About the School",
        "about-text": "Secondary School No. 2 is a modern educational institution with more than 800 students. It combines knowledge, sports, and creativity.",
        "schedule-title": "Class Schedule",
        schedule: `
        <table border="1" cellpadding="8" cellspacing="0" style="width:100%; text-align:center; background-color:rgba(0,0,0,0.3); color:white;">
            <tr><th>Class</th><th>Monday</th><th>Tuesday</th><th>Wednesday</th><th>Thursday</th><th>Friday</th></tr>
            <tr><td>5A</td><td>Math</td><td>Kazakh</td><td>English</td><td>PE</td><td>Computer Science</td></tr>
            <tr><td>6B</td><td>Physics</td><td>Russian</td><td>Biology</td><td>Geography</td><td>Math</td></tr>
        </table>`,
        "teachers-title": "Teachers and Subjects",
        teachers: [
            "Aiman Sultan — Kazakh Language and Literature",
            "Yerzhan Bakytbek — Mathematics",
            "Gulzhan Alimbekova — Biology",
            "Marina Petrovna — Russian Language",
            "John Adams — English Language"
        ],
        "news-title": "News",
        news: [
            "Autumn concert will be held on November 1.",
            "Sports week among grades 5–11 has started.",
            "New computer lab opened!"
        ],
        "contacts-title": "Contacts and Social Media",
        "contacts-text": `Address: Kazakhstan, Almaty, Bilim Street 12<br>
            Phone: +7 (701) 123-45-67<br><br>
            Social media:<br>
            📘 <a href="#">Facebook</a> | 📸 <a href="#">Instagram</a> | 🎥 <a href="#">YouTube</a>`,
        "footer-text": "© 2025 Secondary School No. 2. All rights reserved."
    }
};

const langSelect = document.getElementById("langSelect");
langSelect.addEventListener("change", () => updateLang(langSelect.value));

function updateLang(lang) {
    const t = data[lang];
    for (let key in t) {
        const el = document.getElementById(key);
        if (el && typeof t[key] === "string") el.innerHTML = t[key];
    }
    document.getElementById("schedule-content").innerHTML = t.schedule;
    document.getElementById("teachers-list").innerHTML = t.teachers.map(i => `<li>${i}</li>`).join("");
    document.getElementById("news-list").innerHTML = t.news.map(i => `<li>${i}</li>`).join("");
    document.getElementById("contacts-text").innerHTML = t["contacts-text"];
}

// Устанавливаем язык по умолчанию
updateLang("kk");
