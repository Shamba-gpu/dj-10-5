import json, os

from django.core.management.base import BaseCommand
from school.models import Student, Teacher
from django.conf import settings


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR, 'school.json'), 'r') as json_file:
            data = json.load(json_file)

            for fields in data:
                model = fields['model']
                pk = fields['pk']
                field = fields['fields']

                if (model == 'school.teacher'):
                    name = field['name']
                    subject = field['subject']
                    Teacher.objects.create(id=pk, name=name, subject=subject)

                elif (model == 'school.student'):
                    name = field['name']
                    teacher = field['teacher']
                    group = field['group']
                    st = Student(id=pk, name=name,group=group)
                    st.save()
                    st.teacher.add(teacher)
                    # Student.objects.create(id=pk, name=name, teacher=teacher, group=group)