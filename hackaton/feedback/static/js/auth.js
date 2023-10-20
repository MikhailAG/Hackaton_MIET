window.addEventListener('DOMContentLoaded', () => {
    // Скрипт для перехода в систему после входа
    const login_button = document.querySelector('login-button');

    login_button.addEventListener('click', () => {
        window.location.href = '/worker';
        //TODO: написать тут скрипт для входа по данным пользователей из БД в систему и условия перехода в зависимости от роли
    });
});