import secrets

from django.contrib import admin
from django.contrib.auth.models import User

from review.models import Role, Position, Notification, Person, Institution


class PersonAdmin(admin.ModelAdmin):
    actions = [
        'create_demo_data',
    ]

    @admin.action(description='Create Demo Data to present a showcase')
    def create_demo_data(self, request, queryset):
        """ programmatically create new data to have platform with entities to show """
        person_names = ["Alan Turin", "Ada Lovelace", "Linus Tovalds", "Steve Jobs", "Joseph Weizenbaum", "Sophie Wilson"]
        institution_names = ["KIT", "UDE", "UP"]
        roles_names = ["Submitter", "Reviewer"]
        position_names = ["Junior Researcher", "Senior Researcher", "Professor"]

        institute_pks = []
        role_pks = []
        position_pks = []
        user_pks = []
        person_pks = []

        for institute_name in institution_names:
            institute = Institution(name=institute_name)
            institute.save()
            institute_pks.append(institute.pk)

        for role_name in roles_names:
            role = Role(name=role_name)
            role.save()
            role_pks.append(role.pk)

        for position_name in position_names:
            position = Position(name=position_name)
            position.save()
            position_pks.append(position.pk)

        for i in range(len(person_names)):
            username = "User" + str(i)
            user = User.objects.create_user(username, username + "@test.de", username)
            user.save()
            user_pks.append(user.pk)

        for person_name in person_names:
            random_institute = secrets.choice(list(range(0, len(institute_pks))))
            random_role = secrets.choice(list(range(0, len(role_pks))))
            random_position = secrets.choice(list(range(0, len(position_pks))))

            p_institution = Institution.objects.get(pk=institute_pks[random_institute])
            p_role = Role.objects.get(pk=role_pks[random_role])
            p_position = Position.objects.get(pk=position_pks[random_position])
            p_user = User.objects.get(pk=user_pks[person_names.index(person_name)])

            person = Person(name=person_name, user=p_user, position=p_position, institution=p_institution)
            person.save()
            person.roles.add(p_role)
            person.save()
            person_pks.append(person.pk)


        self.message_user(request, f"Created {len(institute_pks)} institutes, {len(role_pks)} roles, {len(position_pks)} positions, {len(user_pks)} users, {len(person_pks)} persons")


# Register your models here.

admin.site.register(Institution, PersonAdmin)
admin.site.register(Notification)
admin.site.register(Person, PersonAdmin)
admin.site.register(Role)
admin.site.register(Position)
