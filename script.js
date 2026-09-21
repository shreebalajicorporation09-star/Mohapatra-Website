function toggleMenu() {
    const nav = document.querySelector("nav");
    nav.classList.toggle("active");
}


document.getElementById("year").textContent =
    new Date().getFullYear();


function sendMessage(event) {

    event.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const subject = document.getElementById("subject").value;
    const message = document.getElementById("message").value;

    const emailAddress = "your@email.com";

    const mailSubject =
        encodeURIComponent(subject);

    const mailBody =
        encodeURIComponent(
            "Name: " + name +
            "\nEmail: " + email +
            "\n\nMessage:\n" + message
        );

    window.location.href =
        "mailto:" +
        emailAddress +
        "?subject=" +
        mailSubject +
        "&body=" +
        mailBody;
}