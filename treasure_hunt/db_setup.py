# -*- coding: utf-8  -*-
from django.contrib.auth.models import User
User.objects.all().delete()

user = User.objects.create(username="bruna", first_name="Bruna", last_name="Xavier")
user.set_password('123mudar')
user.save()

user = User.objects.create(username="peri", first_name="Luiz", last_name="Pericolo")
user.set_password('123peri')
user.save()

print "{0} Users created!".format(User.objects.count())

from treasure_hunt.models import Object
from treasure_hunt.models import ObjectTip

obj = Object.objects.create(uid="g001", name=u"Vaso Grego Hércules", description=u"Um vaso grego que mostra os 12 trabalhos de Hércules em desenhos na sua superficie.")

ObjectTip.objects.create(text=u"Um item exposto que mostra os 12 trabalhos de Hércules.", difficulty_level=u"EASY", related_object=obj)
ObjectTip.objects.create(text=u"Um artigo de decoração que retrata feitos heróicos de um filho de Zeus.", difficulty_level=u"MEDIUM", related_object=obj)
ObjectTip.objects.create(text=u"Mostra o feitos de um famoso semi-deus.", difficulty_level=u"HARD", related_object=obj)

obj = Object.objects.create(uid="b001", name=u"Cocar do Cacique Raoni", description=u"O cocar festivo do Cacique Raoni utilizado logo após o seu rito de passagem para a vida adulta.")

ObjectTip.objects.create(text=u"Uma peça de vestimenta do Cacique Raoni.", difficulty_level=u"EASY", related_object=obj)
ObjectTip.objects.create(text=u"É composta por penas de aves e é usada por quem tem poder.", difficulty_level=u"MEDIUM", related_object=obj)
ObjectTip.objects.create(text=u"Peça de vestimenta étnica usada por um grande líder brasileiro.", difficulty_level=u"HARD", related_object=obj)

obj = Object.objects.create(uid="sg001", name=u"Veículo Anfíbio Higgens", description=u"Veículo anfíbio usado para o transporte de tropas terrestres até o litoral durante o Dia D.")

ObjectTip.objects.create(text=u"Veículo usado para o desembarque das tropas aliadas durante do Dia D.", difficulty_level=u"EASY", related_object=obj)
ObjectTip.objects.create(text=u"Veículo militar usado em um evento mundial impactante.", difficulty_level=u"MEDIUM", related_object=obj)
ObjectTip.objects.create(text=u"Veículo capaz de transpor distâncias na água.", difficulty_level=u"HARD", related_object=obj)
