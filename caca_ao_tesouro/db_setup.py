
from django.contrib.auth.models import User
User.objects.all().delete()

User.objects.create(username="bruna", password="123mudar", first_name="Bruna", last_name="Xavier")
User.objects.create(username="peri", password="123peri", first_name="Luiz", last_name="Pericolo")

print "{0} Users created!".format(User.objects.count())
