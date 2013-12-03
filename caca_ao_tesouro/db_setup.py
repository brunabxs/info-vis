
from caca_ao_tesouro.models import User

User.objects.all().delete()

User.objects.create(name="bruna", password="123mudar")
User.objects.create(name="peri", password="123peri")

print "{0} Users created!".format(User.objects.count())
