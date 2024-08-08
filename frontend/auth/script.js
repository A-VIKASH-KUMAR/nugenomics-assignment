const registerForm = document.getElementById('register-form');
const loginForm = document.getElementById('login-form');

registerForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const firstName = document.getElementById('first_name').value;
    const lastName = document.getElementById('last_name').value;
    const dateOfBirth = document.getElementById('dob').value;
    const response = await fetch('http://127.0.0.1:8000/auth/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Origin":"*"
        },
        body: JSON.stringify({ email, password, first_name:firstName, last_name:lastName, dob:dateOfBirth })
    });
    const data = await response.json();
    if (data.success) {
        window.location.href = 'register.html';
    } else {
        console.log(data.error);
    }
});

loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const response = await fetch('http://127.0.0.1:8000/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Origin":"*"
        },
        body: JSON.stringify({ email, password })
    });
    const data = await response.json();
    if (data.success) {
        console.log('Login successful');
        // Redirect to dashboard or home page
        window.location.href = 'login.html';
    } else {
        console.log(data.error);
    }
});