// script.js

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    form.addEventListener("submit", function (event) {
        // Example validation or functionality before form submission
        const ipAddress = document.getElementById("ip_address").value;
        const ports = document.getElementById("ports").value;

        // You can add any custom validation logic here
        console.log("Scanning IP:", ipAddress, "for ports:", ports);
    });
});
