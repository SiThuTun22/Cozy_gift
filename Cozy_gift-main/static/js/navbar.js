// document.addEventListener("DOMContentLoaded", function () {
//     const langToggleBtn = document.querySelector('.lang-toggle'); // Toggle button
//     const title1 = document.querySelector('.title1');

//     // Language data
//     const data = {
//         "english": {
//             "title1": "Search",  
//             "fontClass": ""  // No special font for English
//         },
//         "myanmar": {
//             "title1": "ရှာရန်",
//             "fontClass": "myanmar-font"  // Apply Myanmar font
//         }
//     };

//     // Get language from localStorage OR Django session (first visit)
//     let currentLanguage = localStorage.getItem("selectedLanguage") || "{{ request.session.language }}";
//     currentLanguage = currentLanguage === "eng" ? "english" : "myanmar";

//     // Function to update language and font
//     function updateLanguage(language) {
//         title1.textContent = data[language].title1;

//         // Remove existing font class
//         title1.classList.remove("myanmar-font");

//         // Apply Myanmar font if needed
//         if (data[language].fontClass) {
//             title1.classList.add(data[language].fontClass);
//         }

//         // Save language to localStorage
//         localStorage.setItem("selectedLanguage", language);
//     }

//     // ✅ Apply correct language on page load
//     updateLanguage(currentLanguage);

//     // Handle button click to toggle language
//     langToggleBtn.addEventListener("click", function (e) {
//         e.preventDefault(); // Prevent default action

//         setTimeout(() => {
//             // Toggle language
//             currentLanguage = currentLanguage === "english" ? "myanmar" : "english";
//             updateLanguage(currentLanguage);
//         }, 500); // Delay for backend toggle
//     });
// });
