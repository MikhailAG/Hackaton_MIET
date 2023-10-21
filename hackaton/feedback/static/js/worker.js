window.addEventListener('DOMContentLoaded', () => {
    if (!document.querySelector(".sidebar-list-item.employee")) {
      document.querySelector(".sidebar-list-item.feedback").classList.add("active")
    }
    else {
      document.querySelector(".sidebar-list-item.employee").addEventListener("click", function () {
          document.querySelector(".sidebar-list-item.employee").classList.add("active")
          document.querySelector(".sidebar-list-item.feedback").classList.remove("active")
    });
    };

    if (document.querySelector(".sidebar-list-item.feedback")) {
      document.querySelector(".sidebar-list-item.feedback").addEventListener("click", function () {
          document.querySelector(".sidebar-list-item.employee").classList.remove("active")
          document.querySelector(".sidebar-list-item.feedback").classList.add("active")
    });
    }
});
