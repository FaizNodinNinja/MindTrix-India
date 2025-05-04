
    // Text options
    const subtitles = [
        "Empowering Your Digital Future",
        "Transforming Businesses with AI",
        "Leading the Future of Automation"
    ];

    const titles = [
        "Innovative Solutions for Modern Businesses",
        "Smart Solutions for a Smarter World",
        "AI-Driven Success Starts Here"
    ];

    let index = 0;

    function changeText() {
        const subtitleElement = document.getElementById("changing-subtitle");
        const titleElement = document.getElementById("changing-title");

        // Apply fade + slide out effect
        subtitleElement.classList.add("fade-slide-out");
        titleElement.classList.add("fade-slide-out");

        setTimeout(() => {
            // Change text after animation completes
            index = (index + 1) % subtitles.length;
            subtitleElement.textContent = subtitles[index];
            titleElement.textContent = titles[index];

            // Remove old classes and add slide-in effect
            subtitleElement.classList.remove("fade-slide-out");
            titleElement.classList.remove("fade-slide-out");
            subtitleElement.classList.add("fade-slide-in");
            titleElement.classList.add("fade-slide-in");

            // Remove slide-in class after animation to reset for next cycle
            setTimeout(() => {
                subtitleElement.classList.remove("fade-slide-in");
                titleElement.classList.remove("fade-slide-in");
            }, 800);
        }, 800); // Wait for fade-slide-out to complete
    }

    // Change text every 5 seconds
    setInterval(changeText, 5000);


//faq----- <!-- Custom Toggle Script Start -->
document.querySelectorAll('.accordion-button').forEach(function(button) {
  button.addEventListener('click', function(e) {
    var target = document.querySelector(this.getAttribute('data-bs-target'));
    var collapseInstance = bootstrap.Collapse.getInstance(target);

    if (collapseInstance) {
      collapseInstance.toggle();  // toggle karega open/close dono
    } else {
      new bootstrap.Collapse(target, {toggle: true});
    }
    e.preventDefault();
  });
});
