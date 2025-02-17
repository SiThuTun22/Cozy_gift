document.addEventListener("DOMContentLoaded", function () {
    // Add event listeners to checkboxes
    document.querySelectorAll(".form-check-input").forEach((checkbox) => {
        checkbox.addEventListener("change", applyFilters);
    });

    // Add event listeners for price inputs and sort dropdown
    document.getElementById("minPriceInput").addEventListener("input", applyFilters);
    document.getElementById("maxPriceInput").addEventListener("input", applyFilters);
    document.getElementById("sortBy").addEventListener("change", applyFilters);
});

function toggleFilter(filterId, header = null) {
    const content = document.getElementById(filterId);
    content.classList.toggle('visible');
    if (header) header.classList.toggle('open');
}

function applyFilters() {
    let selectedColors = [];
    document.querySelectorAll('input[id^="color"]:checked').forEach((checkbox) => {
        let label = checkbox.labels.length ? checkbox.labels[0].innerText : checkbox.id.replace(/^color/, "");
        selectedColors.push(encodeURIComponent(label));
    });

    let selectedFlowerTypes = [];
    document.querySelectorAll('input[id^="flower"]:checked').forEach((checkbox) => {
        let label = checkbox.labels.length ? checkbox.labels[0].innerText : checkbox.id.replace(/^flower/, "");
        selectedFlowerTypes.push(encodeURIComponent(label));
    });

    let minPrice = document.getElementById("minPriceInput").value || 0;
    let maxPrice = document.getElementById("maxPriceInput").value || '';
    let sortBy = document.getElementById("sortBy").value;

    let filterURL = `/filter-products/?color[]=${selectedColors.join(",")}&flower_type[]=${selectedFlowerTypes.join(",")}&min_price=${minPrice}&max_price=${maxPrice}&sort_by=${sortBy}`;

    console.log("Fetching products with URL:", filterURL); // Debugging

    fetch(filterURL)
        .then(response => response.json())
        .then(data => {
            console.log("Products received:", data.products); // Debugging
            let productContainer = document.querySelector(".row.g-4");
            productContainer.innerHTML = data.products.map(product => `
                <div class="col-6 col-md-4">
                    <div class="collection">
                        <a href="/product/${product.id}" class="btn">
                            <img src="${product.image}" alt="${product.name}">
                        </a>
                        <h3 class="mt-2">${product.name}</h3>
                        <p>${product.price}</p>
                    </div>
                </div>
            `).join("");
        })
        .catch(error => console.error("Error fetching products:", error));
}
