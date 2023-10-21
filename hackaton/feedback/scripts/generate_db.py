import os, sys
sys.path.append('/home/windof/hakaton/Hackaton_MIET/hackaton')
os.environ['DJANGO_SETTINGS_MODULE'] = 'hackaton.settings'
import django
django.setup()
from feedback.models import Users
from feedback.models import Roles
from feedback.models import Feedbacks
from feedback.models import Notifications
import names
import random
from feedback.scripts.textblob_script import sentiment
from feedback.scripts.translator import translate_to_english

roles = [1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

Roles.objects.create(name='Director')
Roles.objects.create(name='Teamlead')
Roles.objects.create(name='Intern')
Users.objects.create(
  name='Boss Krovososs',
  username=f"{names.get_first_name()}_{random.randint(1, 1488)}",
  password=str(random.randint(1, 1000)),
  role=Roles.objects.get(name='Director')
)
for i in range(10):
  Users.objects.create(
    name=names.get_full_name(),
    username=f"{names.get_first_name()}_{random.randint(1, 1488)}",
    password=str(random.randint(1, 1000)),
    role=Roles.objects.get(name='Teamlead'),
    lead_user=Users.objects.get(name='Boss Krovososs')
  )
for i in range(50):
  lead = Roles.objects.get(name='Teamlead').users_set.all().order_by('?').first()
  Users.objects.create(
    name=names.get_full_name(),
    username=f"{names.get_first_name()}_{random.randint(1, 1488)}",
    password=str(random.randint(1, 1000)),
    role=Roles.objects.get(name='Intern'),
    lead_user=lead
  )
employee_reviews = [
    "Сотрудник отлично справляется с задачами и всегда приходит на помощь.",
    "Отличный коллега, всегда готов помочь и делать дополнительные усилия.",
    "Сотрудник демонстрирует выдающиеся навыки в работе и приносит большую пользу команде.",
    "Этот сотрудник всегда опаздывает и не выполняет свои обязанности вовремя.",
    "Качество работы оставляет желать лучшего, сотрудник часто делает ошибки.",
    "Взаимодействие с этим сотрудником приводит к проблемам и недовольству.",
    "С этим сотрудником приятно работать, он отлично выполняет свои обязанности.",
    "Сотрудник всегда принимает инициативу и предлагает креативные идеи.",
    "Очень надежный сотрудник, на него всегда можно полагаться.",
    "Коммуникация с этим сотрудником оставляет желать лучшего, он плохо слушает других.",
    "Сотрудник не всегда приходит на работу вовремя и не выполняет свои обязанности.",
    "Этот сотрудник проявляет инициативу и всегда приходит с креативными идеями.",
    "Сотрудник обладает выдающимися навыками и значительно улучшил рабочие процессы.",
    "Сотрудник не соответствует ожиданиям, его работа оставляет желать лучшего.",
    "Этот сотрудник всегда находит недостатки в работе других и часто критикует коллег.",
    "Сотрудник недостаточно ответственен и часто делает ошибки в работе.",
    "Сотрудник проявляет выдающийся профессионализм и всегда достигает высоких результатов.",
    "Работать с ним - большая удача, он всегда в хорошем настроении и готов помочь.",
    "Сотрудник принимает инициативу и приходит с интересными идеями для улучшения процессов.",
    "Этот сотрудник всегда надежен и ответственен, его коммуникация с коллегами превосходна.",
    "Сотрудник оправдывает все ожидания, его работа на высшем уровне и всегда своевременна.",
]*8

for i in range(100):
  user = Users.objects.filter(role= Roles.objects.filter(name='Intern').first()).order_by('?').first()
  Notifications.objects.create(
    comment='Оцени мою работку пж',
    user=user,
    lead=user.lead_user
  )

for text in employee_reviews:
  user = Users.objects.filter(role= Roles.objects.filter(name='Intern').first()).order_by('?').first()
  Feedbacks.objects.create(
    body=text,
    body_english=translate_to_english(text),
    stars=sentiment(text),
    user=user,
    from_user=user.lead_user
  )
