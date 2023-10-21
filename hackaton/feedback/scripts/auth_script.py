def authfunc(username, password):
    from django.conf import settings
    from django.apps import apps
    Users = apps.get_model('feedback', 'Users')
    for user in Users.objects.all():
        if username == user.username:
            if password == user.password:
                settings.CURRENT_USER = user
                if user.role_id == 1:
                    return 2 # Данные верны Босс
                elif user.role_id == 2:
                    return 3 # Данные верны Тимлид
                elif user.role_id == 3:
                    return 4 # Данные верны Сотрудник
            else:
                return 1 # Неверный пароль
    return 0 # Неверный пользователь