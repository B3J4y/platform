from django.contrib import admin

from review.models import Role, Position, Notification, Person, Institution

# Register your models here.
admin.site.register(Institution)
admin.site.register(Notification)
admin.site.register(Person)
admin.site.register(Role)
admin.site.register(Position)
