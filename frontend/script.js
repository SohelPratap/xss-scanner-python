function fetchData(endpoint, resultElementId, buttonId) {
    const url = document.getElementById("urlInput").value;
    let button = document.getElementById(buttonId);
    if (!button) {
        console.error(`❌ Button with ID ${resultElementId}Btn not found!`);
        return;
    }

    if (!url && endpoint === "/crawl") {
        alert("Please enter a valid URL!");
        return;
    }

    console.log(`🚀 Sending request to: http://127.0.0.1:5000${endpoint} with URL:`, url); // Debugging log

    button.innerText = "Loading...";
    button.disabled = true;

    fetch("http://127.0.0.1:5000" + endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url })
    })
    .then(response => {
        console.log(`Response Status: ${response.status}`);
        return response.json();
    })
    .then(data => {
        console.log(`API Response (${endpoint}):`, data); // Debugging log

        let resultList = document.getElementById(resultElementId);
        resultList.innerHTML = ""; // Clear previous results

        if (data.error) {
            alert(data.error);
        } else {
            console.log("Received Data:", data);
            let items = [];

            if (endpoint === "/crawl") {
                if (!data.crawledEndpoints || !Array.isArray(data.crawledEndpoints.forms)) {
                    console.error("❌ Error: API did not return forms.");
                    resultList.innerHTML = "<li>⚠️ No forms found.</li>";
                    button.innerText = button.getAttribute("data-original-text");
                    button.disabled = false;
                    return;
                }
                items = data.crawledEndpoints.forms.map(f => `<li>🔗 <a href="${f.action}" target="_blank">${f.action}</a></li>`);
            }

            if (items.length === 0) {
                resultList.innerHTML = "<li>❌ No results found.</li>";
            } else {
                resultList.innerHTML = items.join("");  // Display forms properly
            }
        }

        button.innerText = button.getAttribute("data-original-text");
        button.disabled = false;
    })
    .catch(error => {
        console.error("Fetch Error:", error); // Debugging log
        alert("An error occurred. Please try again.");
        button.innerText = button.getAttribute("data-original-text");
        button.disabled = false;
    });
}

document.addEventListener("DOMContentLoaded", () => {
    console.log("✅ DOM fully loaded");

    setTimeout(() => { // Delay to ensure elements exist
          const crawlBtn = document.getElementById("crawlBtn");
          const identifyBtn = document.getElementById("identifyBtn");
          const testBtn = document.getElementById("testBtn");

          if (!crawlBtn || !identifyBtn || !testBtn) {
              console.error("❌ One or more buttons are missing from the DOM!");
              return;
          }

          console.log("✅ Buttons found. Adding event listeners...");

          crawlBtn.addEventListener("click", () => {
              console.log("🚀 Crawl button clicked!");
              fetchData("/crawl", "crawledDomains", "crawlBtn");
          });

          identifyBtn.addEventListener("click", () => {
              console.log("🔍 Identify button clicked!");
              fetchData("/identify", "injectionResults", "identifyBtn");
          });

          testBtn.addEventListener("click", () => {
              console.log("💥 Test button clicked!");
              fetchData("/test", "vulnerableEndpoints", "testBtn");
          });
      }, 1000); // Ensure DOM loads fully
});