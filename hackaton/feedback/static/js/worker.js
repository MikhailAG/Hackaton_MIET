window.addEventListener('DOMContentLoaded', () => {

    const rows_emp = document.querySelectorAll(".products-row.employee");
    const rows_fb = document.querySelectorAll(".products-row.feedback");
    const btns_exit_emp = document.querySelectorAll(".btn-exit.employee")
    const btns_exit_fb = document.querySelectorAll(".btn-exit.feedback")

    rows_emp.forEach(row => {
        row.addEventListener("click", function() {
          document.querySelector(".app-content.employee").style.display = "none";
          document.querySelector(".employee-page").style.display = "block";
          document.querySelector(".employee-page").scrollTop = 0;
        });
    });
    rows_fb.forEach(row => {
      row.addEventListener("click", function() {
          document.querySelector(".app-content.feedback").style.display = "none";
          document.querySelector(".feedback-page").style.display = "block";
          document.querySelector(".feedback-page").scrollTop = 0;
      });
    });

    btns_exit_emp.forEach(btn => {
      btn.addEventListener("click", function() {
          document.querySelector(".app-content.employee").style.display = "flex";
          document.querySelector(".employee-page").style.display = "none";
      });
    });
    btns_exit_fb.forEach(btn => {
      btn.addEventListener("click", function() {
          document.querySelector(".app-content.feedback").style.display = "flex";
          document.querySelector(".feedback-page").style.display = "none";
      });
    });

    document.querySelector(".jsFilter").addEventListener("click", function () {
      document.querySelector(".filter-menu").classList.toggle("active");
    });
    document.querySelector(".mode-switch").addEventListener("click", function () {
      document.documentElement.classList.toggle("dark");
      document.documentElement.classList.toggle("light");
      document.querySelector(".mode-switch").classList.toggle("active");
      document.querySelector(".mode-switch.emp").classList.toggle("active");
    });

    document.querySelector(".jsFilter.emp").addEventListener("click", function () {
      document.querySelector(".filter-menu.emp").classList.toggle("active");
    });
    document.querySelector(".mode-switch.emp").addEventListener("click", function () {
      document.documentElement.classList.toggle("dark");
      document.documentElement.classList.toggle("light");
      document.querySelector(".mode-switch.emp").classList.toggle("active");
      document.querySelector(".mode-switch").classList.toggle("active");
    });

    document.querySelector(".sidebar-list-item.feedback").addEventListener("click", function () {
      document.querySelector(".sidebar-list-item.employee").classList.remove("active")
      document.querySelector(".sidebar-list-item.feedback").classList.add("active")
      document.querySelector(".app-content.employee").style.display = "none";
      document.querySelector(".app-content.feedback").style.display = "flex";
      document.querySelector(".employee-page").style.display = "none";
      document.querySelector(".feedback-page").style.display = "none";
    });
    document.querySelector(".sidebar-list-item.employee").addEventListener("click", function () {
      document.querySelector(".sidebar-list-item.employee").classList.add("active")
      document.querySelector(".sidebar-list-item.feedback").classList.remove("active")
      document.querySelector(".app-content.employee").style.display = "flex";
      document.querySelector(".app-content.feedback").style.display = "none";
      document.querySelector(".employee-page").style.display = "none";
      document.querySelector(".feedback-page").style.display = "none";
    });
});
