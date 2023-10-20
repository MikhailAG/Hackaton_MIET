window.addEventListener('DOMContentLoaded', () => {
    document.querySelector(".jsFilter").addEventListener("click", function () { // Открывашка фильтра
      document.querySelector(".filter-menu").classList.toggle("active");
    });

    var modeSwitch = document.querySelector(".mode-switch"); // Смена темы
    modeSwitch.addEventListener("click", function () {
      document.documentElement.classList.toggle("dark");
      document.documentElement.classList.toggle("light");
      modeSwitch.classList.toggle("active");
    });
});
