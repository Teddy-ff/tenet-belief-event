document.addEventListener("DOMContentLoaded", function () {
    console.log("script.js is loaded successfully!");

    // Function to show the event modal
    function showEvent(title, description, url) {
        const modal = document.getElementById("event-modal");
        if (!modal) {
            console.error("Modal not found!");
            return;
        }
        document.getElementById("event-title").innerText = title;
        document.getElementById("event-description").innerText = description;
        document.getElementById("event-register").href = url;

        modal.classList.add("show"); // Show modal
    }

    // Function to close the event modal
    function closeModal() {
        const modal = document.getElementById("event-modal");
        if (modal) {
            modal.classList.remove("show");
        } else {
            console.error("Modal element not found!");
        }
    }

    // Assign click event to each event item
    document.querySelectorAll(".event-item").forEach((item) => {
        item.addEventListener("click", function () {
            let title = this.querySelector("h3").innerText;
            let description = "Join this exciting event!";
            let url = "#"; // Update with actual registration link

            showEvent(title, description, url);
        });
    });

    // Assign close event to ALL close buttons
    document.querySelectorAll(".close-btn").forEach((btn) => {
        btn.addEventListener("click", closeModal);
    });

    // Close modal when clicking outside the modal content
    window.addEventListener("click", function (event) {
        const modal = document.getElementById("event-modal");
        if (event.target === modal) {
            closeModal();
        }
    });
});

function closeModal() {
    const modal = document.getElementById("event-modal");
    if (modal) {
        modal.classList.remove("show");
    } else {
        console.error("Modal element not found!");
    }
}



