def authfunc(username, password):
    from django.conf import settings
    from django.apps import apps
    Users = apps.get_model('feedback', 'Users')
    for user in Users.objects.all():
        if username == user.username:
            if password == user.password:
                settings.CURRENT_USER = user
                if user.role.name == 'Director':
                    return 2 # Данные верны Босс
                elif user.role.name == 'Teamlead':
                    return 3 # Данные верны Тимлид
                elif user.role.name == 'Intern':
                    return 4 # Данные верны Сотрудник
            else:
                return 1 # Неверный пароль
    return 0 # Неверный пользователь