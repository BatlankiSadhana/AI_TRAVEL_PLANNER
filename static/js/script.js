
document.addEventListener("DOMContentLoaded", function () {

    // Smooth page entrance
    document.body.classList.add("page-loaded");

    // Automatically remove flash messages
    const messages = document.querySelectorAll(".flash-message");

    messages.forEach(function (message) {
        setTimeout(function () {
            message.style.transition = "opacity 0.5s ease";
            message.style.opacity = "0";

            setTimeout(function () {
                message.remove();
            }, 500);

        }, 4000);
    });

    // Prevent accidental invalid trip form submission
    const tripForm = document.querySelector(
        'form[action*="plan-trip"]'
    );

    if (tripForm) {
        tripForm.addEventListener("submit", function (event) {

            const budget = Number(
                document.getElementById("budget").value
            );

            const days = Number(
                document.getElementById("days").value
            );

            const travelers = Number(
                document.getElementById("travelers").value
            );

            if (budget <= 0 || days < 1 || travelers < 1) {
                event.preventDefault();
                alert("Please enter valid travel details.");
            }
        });
    }

});
