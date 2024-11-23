document.querySelector('form').addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevent form from reloading the page

    const username = document.querySelector('input[name="username"]').value.trim();
    const password = document.querySelector('input[name="password"]').value.trim();

    if (!username || !password) {
        alert("Please fill in both fields.");
        return;
    }

    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json', // Ensure Content-Type is JSON
            },
            body: JSON.stringify({ username, password }), // Send JSON data
        });

        const result = await response.json();

        if (response.ok) {
            window.location.href = result.redirect; // Redirect on success
        } else {
            alert(result.message); // Display error message
        }
    } catch (error) {
        console.error("Error submitting form:", error);
        alert("An error occurred. Please try again.");
    }
});
