
from django.contrib.auth.models import User
User.objects.all().delete()

user = User.objects.create(username="bruna", first_name="Bruna", last_name="Xavier")
user.set_password('123mudar')
user.save()

user = User.objects.create(username="peri", first_name="Luiz", last_name="Pericolo")
user.set_password('123peri')
user.save()

print "{0} Users created!".format(User.objects.count())
