from django.db import migrations


def seed(apps, schema_editor):
    Subject = apps.get_model("portal", "Subject")
    Teacher = apps.get_model("portal", "Teacher")
    SchoolClass = apps.get_model("portal", "SchoolClass")
    ScheduleSlot = apps.get_model("portal", "ScheduleSlot")
    NewsItem = apps.get_model("portal", "NewsItem")

    names = [
        "Математика",
        "Қазақ тілі",
        "Физика",
        "Ағылшын тілі",
        "Тарих",
        "Химия",
        "Дүниежүзі тарихы",
        "Биология",
    ]
    subjects = {}
    for n in names:
        s, _ = Subject.objects.get_or_create(name=n)
        subjects[n] = s

    def teacher(last, first, middle, position, taught):
        t, _ = Teacher.objects.get_or_create(
            last_name=last,
            first_name=first,
            middle_name=middle,
            defaults={"position": position},
        )
        if not t.subjects.exists():
            for sub in taught:
                t.subjects.add(subjects[sub])
        return t

    teacher("Нұрланов", "Ерлан", "Серікұлы", "Математика мұғалімі", ["Математика"])
    teacher("Әбдіқалықова", "Айгүл", "Нүрланқызы", "Қазақ тілі", ["Қазақ тілі"])
    teacher("Қасымов", "Данияр", "", "Физика мұғалімі", ["Физика"])
    teacher("Smith", "John", "", "Ағылшын тілі", ["Ағылшын тілі"])
    teacher("Омарова", "Ляззат", "Кайратқызы", "Тарих мұғалімі", ["Тарих", "Дүниежүзі тарихы"])
    teacher("Бектасов", "Арман", "Болатұлы", "Химия", ["Химия"])
    teacher("Сарсенова", "Гүлнар", "", "Биология", ["Биология"])

    teachers_by_subject = {
        "Математика": Teacher.objects.filter(last_name="Нұрланов").first(),
        "Қазақ тілі": Teacher.objects.filter(last_name="Әбдіқалықова").first(),
        "Физика": Teacher.objects.filter(last_name="Қасымов").first(),
        "Ағылшын тілі": Teacher.objects.filter(last_name="Smith").first(),
        "Тарих": Teacher.objects.filter(last_name="Омарова").first(),
        "Химия": Teacher.objects.filter(last_name="Бектасов").first(),
        "Дүниежүзі тарихы": Teacher.objects.filter(last_name="Омарова").first(),
        "Биология": Teacher.objects.filter(last_name="Сарсенова").first(),
    }

    c5a, _ = SchoolClass.objects.get_or_create(
        grade=5, letter="А", defaults={"slug": "5a"}
    )
    if not c5a.slug:
        c5a.slug = "5a"
        c5a.save(update_fields=["slug"])

    c5b, _ = SchoolClass.objects.get_or_create(
        grade=5, letter="Б", defaults={"slug": "5b"}
    )
    if not c5b.slug:
        c5b.slug = "5b"
        c5b.save(update_fields=["slug"])

    grid_5a = [
        (0, 1, "Математика"),
        (1, 1, "Қазақ тілі"),
        (2, 1, "Физика"),
        (3, 1, "Ағылшын тілі"),
        (4, 1, "Тарих"),
        (0, 2, "Қазақ тілі"),
        (1, 2, "Химия"),
        (2, 2, "Математика"),
        (3, 2, "Дүниежүзі тарихы"),
        (4, 2, "Физика"),
        (0, 3, "Физика"),
        (1, 3, "Ағылшын тілі"),
        (2, 3, "Биология"),
        (3, 3, "Математика"),
        (4, 3, "Қазақ тілі"),
        (0, 4, "Ағылшын тілі"),
        (1, 4, "Дүниежүзі тарихы"),
        (2, 4, "Қазақ тілі"),
        (3, 4, "Химия"),
        (4, 4, "Математика"),
    ]

    for weekday, lesson, subname in grid_5a:
        subj = subjects[subname]
        teach = teachers_by_subject.get(subname)
        ScheduleSlot.objects.get_or_create(
            school_class=c5a,
            weekday=weekday,
            lesson_number=lesson,
            defaults={
                "subject": subj,
                "teacher": teach,
                "room": f"{101 + lesson}",
            },
        )

    for weekday in range(5):
        for lesson in range(1, 5):
            ScheduleSlot.objects.get_or_create(
                school_class=c5b,
                weekday=weekday,
                lesson_number=lesson,
                defaults={
                    "subject": subjects["Математика"],
                    "teacher": teachers_by_subject["Математика"],
                    "room": "201",
                },
            )

    NewsItem.objects.get_or_create(
        title="Математика пәнінен олимпиада",
        defaults={
            "body": "20 қарашада мектеп оқушылары қалалық математика олимпиадасына қатысты.",
            "published_at": "2025-11-20",
        },
    )
    NewsItem.objects.get_or_create(
        title="Спорттық іс-шара",
        defaults={
            "body": "Мектеп спорт залында волейбол турнирі өтті.",
            "published_at": "2025-11-18",
        },
    )
    NewsItem.objects.get_or_create(
        title="Шығармашылық көрме",
        defaults={
            "body": "Сурет және қолөнер көрмесі ашылды, барлық оқушылар қатыса алады.",
            "published_at": "2025-11-15",
        },
    )


def reverse_seed(apps, schema_editor):
    ScheduleSlot = apps.get_model("portal", "ScheduleSlot")
    NewsItem = apps.get_model("portal", "NewsItem")
    SchoolClass = apps.get_model("portal", "SchoolClass")
    Teacher = apps.get_model("portal", "Teacher")
    Subject = apps.get_model("portal", "Subject")

    ScheduleSlot.objects.all().delete()
    NewsItem.objects.all().delete()
    SchoolClass.objects.all().delete()
    Teacher.objects.all().delete()
    Subject.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("portal", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed, reverse_seed),
    ]
