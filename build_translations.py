import os
import polib
from pathlib import Path

translations = {
    "FAQ": {"kk": "Жиі қойылатын сұрақтар", "en": "FAQ"},
    "Адрес": {"kk": "Мекенжай", "en": "Address"},
    "Альбомов пока нет.": {"kk": "Әзірге альбомдар жоқ.", "en": "No albums yet."},
    "Бейсенбі": {"kk": "Бейсенбі", "en": "Thursday"},
    "Будьте в курсе последних событий": {"kk": "Соңғы оқиғалардан хабардар болыңыз", "en": "Stay up to date with the latest events"},
    "В этом альбоме пока нет фото.": {"kk": "Бұл альбомда әзірге фотосуреттер жоқ.", "en": "No photos in this album yet."},
    "Ваше имя": {"kk": "Атыңыз", "en": "Your name"},
    "Ваше сообщение успешно отправлено!": {"kk": "Сіздің хабарламаңыз сәтті жіберілді!", "en": "Your message was sent successfully!"},
    "Войти в админку": {"kk": "Админ-панельге кіру", "en": "Login to Admin"},
    "Вперед": {"kk": "Алға", "en": "Next"},
    "Все награды": {"kk": "Барлық марапаттар", "en": "All awards"},
    "Все новости": {"kk": "Барлық жаңалықтар", "en": "All news"},
    "Все права защищены.": {"kk": "Барлық құқықтар қорғалған.", "en": "All rights reserved."},
    "Все предметы": {"kk": "Барлық пәндер", "en": "All subjects"},
    "Вы успешно зарегистрировались! Теперь вы можете войти в админ-панель. Для получения прав на редактирование обратитесь к главному администратору.": {"kk": "Сіз сәтті тіркелдіңіз! Енді сіз админ-панельге кіре аласыз. Өңдеу құқығын алу үшін бас әкімшіге хабарласыңыз.", "en": "You have successfully registered! Now you can log in to the admin panel. To get editing rights, contact the main administrator."},
    "Галерея": {"kk": "Галерея", "en": "Gallery"},
    "Главная": {"kk": "Басты бет", "en": "Home"},
    "Гордость нашей школы": {"kk": "Мектебіміздің мақтанышы", "en": "Pride of our school"},
    "Директор школы": {"kk": "Мектеп директоры", "en": "School Principal"},
    "Добро пожаловать в нашу школу": {"kk": "Біздің мектепке қош келдіңіз", "en": "Welcome to our school"},
    "Документы": {"kk": "Құжаттар", "en": "Documents"},
    "Документы пока не загружены.": {"kk": "Құжаттар әлі жүктелген жоқ.", "en": "Documents are not uploaded yet."},
    "Достижения пока не добавлены.": {"kk": "Жетістіктер әлі қосылмаған.", "en": "Achievements are not added yet."},
    "Дүйсенбі": {"kk": "Дүйсенбі", "en": "Monday"},
    "Жексенбі": {"kk": "Жексенбі", "en": "Sunday"},
    "Жұма": {"kk": "Жұма", "en": "Friday"},
    "Зарегистрироваться": {"kk": "Тіркелу", "en": "Register"},
    "Знания - сила!": {"kk": "Білім - күш!", "en": "Knowledge is power!"},
    "Информация о школе скоро появится.": {"kk": "Мектеп туралы ақпарат жақында шығады.", "en": "Information about the school will appear soon."},
    "Карта не настроена": {"kk": "Карта бапталмаған", "en": "Map is not configured"},
    "Классы пока не добавлены.": {"kk": "Сыныптар әлі қосылмаған.", "en": "Classes are not added yet."},
    "Ко всем альбомам": {"kk": "Барлық альбомдарға", "en": "To all albums"},
    "Ко всем новостям": {"kk": "Барлық жаңалықтарға", "en": "To all news"},
    "Контактная информация": {"kk": "Байланыс ақпараты", "en": "Contact information"},
    "Контакты": {"kk": "Байланыстар", "en": "Contacts"},
    "Моменты из нашей галереи": {"kk": "Біздің галереядағы сәттер", "en": "Moments from our gallery"},
    "Мы в соцсетях": {"kk": "Біз әлеуметтік желілердеміз", "en": "We are in social networks"},
    "Назад": {"kk": "Артқа", "en": "Back"},
    "Написать нам": {"kk": "Бізге жазу", "en": "Write to us"},
    "Наши достижения": {"kk": "Біздің жетістіктеріміз", "en": "Our achievements"},
    "Наши преподаватели": {"kk": "Біздің оқытушыларымыз", "en": "Our teachers"},
    "Наши учителя": {"kk": "Біздің мұғалімдер", "en": "Our teachers"},
    "Нет новостей.": {"kk": "Жаңалықтар жоқ.", "en": "No news."},
    "Нет предстоящих событий.": {"kk": "Алдағы оқиғалар жоқ.", "en": "No upcoming events."},
    "Новостей пока нет.": {"kk": "Әзірге жаңалықтар жоқ.", "en": "No news yet."},
    "Новости": {"kk": "Жаңалықтар", "en": "News"},
    "Новости школы": {"kk": "Мектеп жаңалықтары", "en": "School news"},
    "О нашей школе": {"kk": "Біздің мектеп туралы", "en": "About our school"},
    "О себе": {"kk": "Өзім туралы", "en": "About me"},
    "О школе": {"kk": "Мектеп туралы", "en": "About school"},
    "Остались вопросы?": {"kk": "Сұрақтарыңыз қалды ма?", "en": "Any questions left?"},
    "Ответы на самые популярные вопросы родителей и учеников": {"kk": "Ата-аналар мен оқушылардың ең танымал сұрақтарына жауаптар", "en": "Answers to the most popular questions from parents and students"},
    "Отправить сообщение": {"kk": "Хабарлама жіберу", "en": "Send message"},
    "Официальная документация школы": {"kk": "Мектептің ресми құжаттары", "en": "Official school documentation"},
    "Перейти в галерею": {"kk": "Галереяға өту", "en": "Go to gallery"},
    "Победы учеников и учителей": {"kk": "Оқушылар мен мұғалімдердің жеңістері", "en": "Victories of students and teachers"},
    "Подробнее о школе": {"kk": "Мектеп туралы толығырақ", "en": "More about the school"},
    "Пожалуйста, заполните все обязательные поля.": {"kk": "Барлық міндетті өрістерді толтырыңыз.", "en": "Please fill in all required fields."},
    "Последние новости": {"kk": "Соңғы жаңалықтар", "en": "Latest news"},
    "Посмотреть всех учителей": {"kk": "Барлық мұғалімдерді көру", "en": "See all teachers"},
    "Предметы": {"kk": "Пәндер", "en": "Subjects"},
    "Профессионалы своего дела, которые ежедневно вкладывают душу в обучение и воспитание детей.": {"kk": "Балаларды оқытуға және тәрбиелеуге күн сайын жанын салатын өз ісінің мамандары.", "en": "Professionals in their field who daily put their soul into the education and upbringing of children."},
    "Разделы": {"kk": "Бөлімдер", "en": "Sections"},
    "Расписание": {"kk": "Кесте", "en": "Schedule"},
    "Расписание для": {"kk": "Кестесі", "en": "Schedule for"},
    "Расписание уроков": {"kk": "Сабақ кестесі", "en": "Lesson schedule"},
    "Регистрация": {"kk": "Тіркелу", "en": "Registration"},
    "Режим работы": {"kk": "Жұмыс уақыты", "en": "Working hours"},
    "Свяжитесь с нами удобным для вас способом": {"kk": "Сізге ыңғайлы тәсілмен бізбен байланысыңыз", "en": "Contact us in a convenient way for you"},
    "Свяжитесь с нами, и мы с радостью ответим на все ваши вопросы и проведем экскурсию по школе.": {"kk": "Бізбен байланысыңыз, біз сіздің барлық сұрақтарыңызға қуана жауап береміз және мектеп бойынша экскурсия өткіземіз.", "en": "Contact us and we will gladly answer all your questions and give a tour of the school."},
    "Связаться с нами": {"kk": "Бізбен байланысу", "en": "Contact us"},
    "Сейсенбі": {"kk": "Сейсенбі", "en": "Tuesday"},
    "Сенбі": {"kk": "Сенбі", "en": "Saturday"},
    "Скачать": {"kk": "Жүктеп алу", "en": "Download"},
    "Слово директора": {"kk": "Директордың сөзі", "en": "Director's speech"},
    "События": {"kk": "Оқиғалар", "en": "Events"},
    "Создайте аккаунт для доступа к школьному порталу": {"kk": "Мектеп порталына кіру үшін аккаунт жасаңыз", "en": "Create an account to access the school portal"},
    "Сообщение": {"kk": "Хабарлама", "en": "Message"},
    "Список вопросов пока пуст.": {"kk": "Сұрақтар тізімі әзірге бос.", "en": "The list of questions is currently empty."},
    "Стаж:": {"kk": "Еңбек өтілі:", "en": "Experience:"},
    "Сәрсенбі": {"kk": "Сәрсенбі", "en": "Wednesday"},
    "Телефон": {"kk": "Телефон", "en": "Phone"},
    "Уже есть аккаунт?": {"kk": "Аккаунт бар ма?", "en": "Already have an account?"},
    "Узнать больше": {"kk": "Толығырақ білу", "en": "Learn more"},
    "Учителя": {"kk": "Мұғалімдер", "en": "Teachers"},
    "Учителя не найдены.": {"kk": "Мұғалімдер табылмады.", "en": "Teachers not found."},
    "Частые вопросы (FAQ)": {"kk": "Жиі қойылатын сұрақтар (FAQ)", "en": "Frequently Asked Questions (FAQ)"},
    "Читать далее": {"kk": "Әрі қарай оқу", "en": "Read more"},
    "Школа": {"kk": "Мектеп", "en": "School"},
    "Школьная жизнь": {"kk": "Мектеп өмірі", "en": "School life"},
    "Яркие моменты нашей школы": {"kk": "Мектебіміздің жарқын сәттері", "en": "Bright moments of our school"},
    "фото": {"kk": "фото", "en": "photo"},
    "№2 Орта Мектеп": {"kk": "№2 Орта Мектеп", "en": "Secondary School №2"},
    "English": {"kk": "English", "en": "English"},
    "Русский": {"kk": "Русский", "en": "Русский"},
    "Қазақша": {"kk": "Қазақша", "en": "Қазақша"}
}

def build():
    base = Path(__file__).resolve().parent / "locale"
    
    with open('strings.txt', 'r', encoding='utf-8') as f:
        strings = [line.strip() for line in f if line.strip()]
        
    for lang in ['kk', 'ru', 'en']:
        lc_dir = base / lang / "LC_MESSAGES"
        lc_dir.mkdir(parents=True, exist_ok=True)
        po = polib.POFile()
        po.metadata = {
            'Project-Id-Version': '1.0',
            'Report-Msgid-Bugs-To': 'you@example.com',
            'POT-Creation-Date': '2023-10-10 10:00+0000',
            'PO-Revision-Date': '2023-10-10 10:00+0000',
            'Last-Translator': 'you <you@example.com>',
            'Language-Team': 'Language <your_email@example.com>',
            'Language': lang,
            'MIME-Version': '1.0',
            'Content-Type': 'text/plain; charset=utf-8',
            'Content-Transfer-Encoding': '8bit',
        }
        
        for s in strings:
            if lang == 'ru':
                translated = s
            else:
                translated = translations.get(s, {}).get(lang, s)
                
            entry = polib.POEntry(
                msgid=s,
                msgstr=translated,
            )
            po.append(entry)
            
        po_path = lc_dir / "django.po"
        po.save(str(po_path))
        print(f"Saved {po_path}")

if __name__ == '__main__':
    build()
