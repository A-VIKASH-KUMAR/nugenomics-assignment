const registerForm = document.getElementById("register-form");
const loginForm = document.getElementById("login-form");

registerForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const firstName = document.getElementById("first_name").value;
  const lastName = document.getElementById("last_name").value;
  const dateOfBirth = document.getElementById("dob").value;
  const response = await fetch("http://127.0.0.1:8000/auth/register", {
    method: "POST",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
    referrerPolicy: "no-referrer",
    body: JSON.stringify({
      email,
      password,
      first_name: firstName,
      last_name: lastName,
      dob: dateOfBirth,
    }),
  }).catch((error) => console.error(error));
  const data = await response.json();
  console.log("data", data);
  if (data[1] === 200) {
    window.location.href = `index.html?message=${data[0].message}`;
    // Get the query parameter
    const urlParams = new URLSearchParams(window.location.search);
    const message = urlParams.get("message");

    // Display the message
    if (message) {
      const body = document.body;
      const msgDiv = document.createElement("div");
      msgDiv.innerHTML = message;
      body.appendChild(msgDiv);
    }
    return { message: "successfully registered user" };
  } else {
    console.log(data.error);
  }
});