from django.shortcuts import get_object_or_404, render

from .models import NewsItem, ScheduleSlot, SchoolClass, Teacher


def index(request):
    return render(request, "portal/index.html", {"nav": "home"})


def about(request):
    teachers = Teacher.objects.prefetch_related("subjects").all()
    return render(
        request,
        "portal/about.html",
        {"nav": "about", "teachers": teachers},
    )


def schedule(request, class_slug=None):
    classes = SchoolClass.objects.all()
    selected = None
    if class_slug:
        selected = get_object_or_404(SchoolClass, slug=class_slug)
    elif classes.exists():
        selected = classes.first()

    weekdays = list(range(5))
    weekday_labels = [
        dict(ScheduleSlot.WEEKDAY_CHOICES)[d] for d in weekdays
    ]

    slot_map = {}
    max_lesson = 0
    if selected:
        slots = selected.schedule_slots.select_related("subject", "teacher").all()
        for s in slots:
            if s.weekday in weekdays:
                slot_map[(s.weekday, s.lesson_number)] = s
                max_lesson = max(max_lesson, s.lesson_number)
        if max_lesson == 0:
            max_lesson = 6
    else:
        max_lesson = 6

    lesson_range = list(range(1, max_lesson + 1))

    schedule_rows = []
    for lesson in lesson_range:
        cells = [slot_map.get((day, lesson)) for day in weekdays]
        schedule_rows.append({"lesson": lesson, "cells": cells})

    return render(
        request,
        "portal/schedule.html",
        {
            "nav": "schedule",
            "classes": classes,
            "selected_class": selected,
            "weekday_labels": weekday_labels,
            "schedule_rows": schedule_rows,
        },
    )


def news_list(request):
    items = NewsItem.objects.all()[:50]
    return render(request, "portal/news.html", {"nav": "news", "news_items": items})
