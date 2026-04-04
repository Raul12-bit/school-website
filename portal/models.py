from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Subject(models.Model):
    name = models.CharField("Пән атауы (қаз)", max_length=120)
    name_ru = models.CharField("Атауы (орыс)", max_length=120, blank=True)
    name_en = models.CharField("Атауы (ағыл.)", max_length=120, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Пән"
        verbose_name_plural = "Пәндер"

    def __str__(self):
        return self.name


class Teacher(models.Model):
    last_name = models.CharField("Тегі", max_length=80)
    first_name = models.CharField("Аты", max_length=80)
    middle_name = models.CharField("Әкесінің аты", max_length=80, blank=True)
    subjects = models.ManyToManyField(
        Subject,
        verbose_name="Пәндер",
        blank=True,
        related_name="teachers",
    )
    email = models.EmailField("Email", blank=True)
    phone = models.CharField("Телефон", max_length=32, blank=True)
    position = models.CharField("Лауазымы (қаз)", max_length=120, blank=True)
    position_ru = models.CharField("Лауазым (орыс)", max_length=120, blank=True)
    position_en = models.CharField("Должность (англ.)", max_length=120, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Мұғалім"
        verbose_name_plural = "Мұғалімдер"

    def __str__(self):
        parts = [self.last_name, self.first_name]
        if self.middle_name:
            parts.append(self.middle_name)
        return " ".join(parts)

    def short_name(self):
        initial = (self.first_name[:1] + ".") if self.first_name else ""
        return f"{self.last_name} {initial}".strip()


class SchoolClass(models.Model):
    grade = models.PositiveSmallIntegerField("Сынып (сан)")
    letter = models.CharField("Литер", max_length=4)
    slug = models.SlugField("Слаг (URL)", unique=True, help_text="мысалы: 5a, 9b")

    class Meta:
        ordering = ["grade", "letter"]
        verbose_name = "Сынып"
        verbose_name_plural = "Сыныптар"
        constraints = [
            models.UniqueConstraint(
                fields=["grade", "letter"],
                name="portal_schoolclass_grade_letter_uniq",
            )
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.grade}-{self.letter}", allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.grade}«{self.letter}»"


class ScheduleSlot(models.Model):
    WEEKDAY_CHOICES = [
        (0, _("Дүйсенбі")),
        (1, _("Сейсенбі")),
        (2, _("Сәрсенбі")),
        (3, _("Бейсенбі")),
        (4, _("Жұма")),
        (5, _("Сенбі")),
        (6, _("Жексенбі")),
    ]

    school_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.CASCADE,
        related_name="schedule_slots",
        verbose_name="Сынып",
    )
    weekday = models.PositiveSmallIntegerField("Апта күні", choices=WEEKDAY_CHOICES)
    lesson_number = models.PositiveSmallIntegerField("Сабақ №")
    subject = models.ForeignKey(
        Subject,
        on_delete=models.PROTECT,
        related_name="schedule_slots",
        verbose_name="Пән",
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="schedule_slots",
        verbose_name="Мұғалім",
    )
    room = models.CharField("Кабинет", max_length=32, blank=True)

    class Meta:
        ordering = ["school_class", "weekday", "lesson_number"]
        verbose_name = "Сабақ слоты"
        verbose_name_plural = "Сабақ кестесі"
        constraints = [
            models.UniqueConstraint(
                fields=["school_class", "weekday", "lesson_number"],
                name="portal_scheduleslot_class_day_lesson_uniq",
            )
        ]

    def __str__(self):
        return f"{self.school_class} — {self.get_weekday_display()} #{self.lesson_number}: {self.subject}"


class NewsItem(models.Model):
    title = models.CharField("Тақырып (қаз)", max_length=220)
    title_ru = models.CharField("Тақырып (орыс)", max_length=220, blank=True)
    title_en = models.CharField("Заголовок (англ.)", max_length=220, blank=True)
    body = models.TextField("Мәтін (қаз)")
    body_ru = models.TextField("Мәтін (орыс)", blank=True)
    body_en = models.TextField("Текст (англ.)", blank=True)
    published_at = models.DateField("Күні")

    class Meta:
        ordering = ["-published_at", "-id"]
        verbose_name = "Жаңалық"
        verbose_name_plural = "Жаңалықтар"

    def __str__(self):
        return self.title
