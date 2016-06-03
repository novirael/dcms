from django.contrib import admin

from schedules.models import Term, Schedule


class TermAdmin(admin.ModelAdmin):
    list_display = ("date", "starts", "ends", "is_free")
    list_filter = ("date", "is_free")


class TermInLine(admin.TabularInline):
    model = Term
    exclude = ("is_free",)


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("created_date", "creator")
    readonly_fields = list_display
    list_filter = list_display
    inlines = [TermInLine]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        return super(ScheduleAdmin, self).save_model(request, obj, form, change)


admin.site.register(Term, TermAdmin)
admin.site.register(Schedule, ScheduleAdmin)
