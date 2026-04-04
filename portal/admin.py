from django.contrib import admin

from .models import NewsItem, ScheduleSlot, SchoolClass, Subject, Teacher

admin.site.site_header = "№2 Орта Мектеп — әкімшілік"
admin.site.site_title = "Мектеп порталы"
admin.site.index_title = "Басқару панелі"


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    search_fields = ["name", "name_ru", "name_en"]
    fields = ("name", "name_ru", "name_en")


class ScheduleInline(admin.TabularInline):
    model = ScheduleSlot
    extra = 0
    autocomplete_fields = ["subject", "teacher"]
    ordering = ["weekday", "lesson_number"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("short_name_display", "position", "phone", "email")
    search_fields = ("last_name", "first_name", "middle_name", "email")
    filter_horizontal = ("subjects",)
    fieldsets = (
        (None, {"fields": ("last_name", "first_name", "middle_name")}),
        (
            "Лауазым / переводы",
            {"fields": ("position", "position_ru", "position_en")},
        ),
        ("Байланыс", {"fields": ("email", "phone")}),
        ("Пәндер", {"fields": ("subjects",)}),
    )

    @admin.display(description="Аты-жөні")
    def short_name_display(self, obj):
        return str(obj)


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ("__str__", "slug")
    search_fields = ("letter", "slug")
    inlines = [ScheduleInline]


@admin.register(ScheduleSlot)
class ScheduleSlotAdmin(admin.ModelAdmin):
    list_display = ("school_class", "weekday", "lesson_number", "subject", "teacher", "room")
    list_filter = ("school_class", "weekday")
    autocomplete_fields = ["school_class", "subject", "teacher"]
    ordering = ("school_class", "weekday", "lesson_number")


@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at")
    search_fields = ("title", "title_ru", "title_en", "body", "body_ru", "body_en")
    date_hierarchy = "published_at"
    fieldsets = (
        ("Қазақша", {"fields": ("title", "body")}),
        ("Орыс / ағылшын", {"fields": ("title_ru", "body_ru", "title_en", "body_en")}),
        ("Күні", {"fields": ("published_at",)}),
    )
