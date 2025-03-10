document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript Loaded!"); // Debugging line

    let button = document.getElementById("calculate-btn");

    if (button) {
        button.addEventListener("click", function () {
            console.log("Button Clicked!"); // Debugging line

            let birthdate = document.getElementById("birthdate").value;

            if (!birthdate) {
                document.getElementById("result").textContent = "Please enter your birthdate.";
                return;
            }

            fetch("/calculate_age", {
                method: "POST",
                body: new URLSearchParams({ "birthdate": birthdate }),
                headers: { "Content-Type": "application/x-www-form-urlencoded" }
            })
            .then(response => response.json())
            .then(data => {
                console.log("Response Data:", data); // Debugging line

                if (data.error) {
                    document.getElementById("result").textContent = "Error: " + data.error;
                } else {
                    document.getElementById("result").textContent = 
                        `Your age is ${data.years} years, ${data.months} months, and ${data.days} days.`;
                }
            })
            .catch(error => {
                console.error("Fetch Error:", error);
                document.getElementById("result").textContent = "An error occurred.";
            });
        });
    } else {
        console.error("Button element not found!");
    }
});
//document.getElementById("calculate-btn").click();