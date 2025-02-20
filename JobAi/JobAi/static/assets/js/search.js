document.addEventListener("DOMContentLoaded", function() {
    // Get references to elements.
    const searchInput = document.querySelector("input[name='search']");
    const locationInput = document.querySelector("input[name='location']");
    const searchButton = document.getElementById("search-btn");
    const tableBody = document.querySelector("tbody");
  
    if (!searchInput || !locationInput || !searchButton || !tableBody) {
      console.error("One or more required elements are missing.");
      return;
    }
  
    searchButton.addEventListener("click", function(event) {
      event.preventDefault(); // Prevent default behavior (if button is in a form)
  
      // Read input values.
      const searchValue = searchInput.value.trim();
      const locationValue = locationInput.value.trim();
  
      // Construct the URL using our URL pattern defined in urls.py.
      const url = `{%url 'search-job'%}?search=${encodeURIComponent(searchValue)}&location=${encodeURIComponent(locationValue)}`;
      console.log("AJAX request URL:", url);
  
      fetch(url, {
        headers: {
          "X-Requested-With": "XMLHttpRequest"  // Let the server know this is an AJAX call.
        }
      })
        .then(response => {
          if (!response.ok) {
            throw new Error("Network error: " + response.status);
          }
          return response.text();
        })
        .then(html => {
          console.log("Received HTML length:", html.length);
          // Parse the returned HTML.
          const parser = new DOMParser();
          const doc = parser.parseFromString(html, "text/html");
          const newTbody = doc.querySelector("tbody");
  
          if (newTbody) {
            tableBody.innerHTML = newTbody.innerHTML;
            console.log("Table updated successfully.");
          } else {
            console.error("Could not find <tbody> in the AJAX response.");
            console.log("Response snippet:", html.substring(0, 300));
          }
        })
        .catch(error => {
          console.error("Error during fetch:", error);
        });
    });
  });
  