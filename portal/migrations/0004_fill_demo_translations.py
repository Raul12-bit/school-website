from django.db import migrations


def fill_ru_en(apps, schema_editor):
    Subject = apps.get_model("portal", "Subject")
    NewsItem = apps.get_model("portal", "NewsItem")

    subs = {
        "Математика": ("Математика", "Mathematics"),
        "Қазақ тілі": ("Казахский язык", "Kazakh language"),
        "Физика": ("Физика", "Physics"),
        "Ағылшын тілі": ("Английский язык", "English"),
        "Тарих": ("История", "History"),
        "Химия": ("Химия", "Chemistry"),
        "Дүниежүзі тарихы": ("Всемирная история", "World history"),
        "Биология": ("Биология", "Biology"),
    }
    for s in Subject.objects.all():
        pair = subs.get(s.name)
        if not pair:
            continue
        ru, en = pair
        if not s.name_ru:
            s.name_ru = ru
        if not s.name_en:
            s.name_en = en
        s.save(update_fields=["name_ru", "name_en"])

    news = [
        (
            "Математика пәнінен олимпиада",
            "Олимпиада по математике",
            "Mathematics olympiad",
            "20 қарашада мектеп оқушылары қалалық математика олимпиадасына қатысты.",
            "20 ноября школьники приняли участие в городской олимпиаде по математике.",
            "In November, students took part in the city mathematics olympiad.",
        ),
        (
            "Спорттық іс-шара",
            "Спортивное мероприятие",
            "Sports event",
            "Мектеп спорт залында волейбол турнирі өтті.",
            "В школьном спортзале прошёл турнир по волейболу.",
            "A volleyball tournament was held in the school gym.",
        ),
        (
            "Шығармашылық көрме",
            "Творческая выставка",
            "Art exhibition",
            "Сурет және қолөнер көрмесі ашылды, барлық оқушылар қатыса алады.",
            "Открылась выставка рисунков и прикладного искусства, все ученики могут участвовать.",
            "An art and crafts exhibition opened; all students are welcome.",
        ),
    ]
    for title_kk, title_ru, title_en, body_kk, body_ru, body_en in news:
        n = NewsItem.objects.filter(title=title_kk).first()
        if not n:
            continue
        if not n.title_ru:
            n.title_ru = title_ru
        if not n.title_en:
            n.title_en = title_en
        if not n.body_ru:
            n.body_ru = body_ru
        if not n.body_en:
            n.body_en = body_en
        n.save(
            update_fields=["title_ru", "title_en", "body_ru", "body_en"]
        )


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("portal", "0003_newsitem_body_en_newsitem_body_ru_newsitem_title_en_and_more"),
    ]

    operations = [
        migrations.RunPython(fill_ru_en, noop),
    ]
