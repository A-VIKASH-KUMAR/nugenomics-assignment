const loginForm = document.getElementById("login-form");

loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const email = document.getElementById("login-email").value;
    const password = document.getElementById("login-password").value;
    const response = await fetch("http://127.0.0.1:8000/auth/login", {
      method: "POST",
      mode: "cors",
      referrerPolicy: "no-referrer",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
      },
      body: JSON.stringify({ email:email, password:password }),
    }).catch((error) => console.error(error));
    const data = await response.json();
    if (data[1] === 200) {
      console.log("Login successful");
      // Redirect to dashboard or home page
      window.location.href = `index.html?message=${data[0].message}`;
      const urlParams = new URLSearchParams(window.location.search);
      const message = urlParams.get("message");
  
      // Display the message
      if (message) {
        const body = document.body;
        const msgDiv = document.createElement("div");
        msgDiv.innerHTML = message;
        body.appendChild(msgDiv);
      }
    } else {
      console.log(data.error);
    }
  });