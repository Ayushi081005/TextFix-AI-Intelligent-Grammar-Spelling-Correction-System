document.addEventListener("DOMContentLoaded", function () {

    console.log("TextFix AI JavaScript loaded");

    const textInput = document.getElementById("text");
    const characterCount = document.getElementById("characterCount");

    const fileInput = document.getElementById("file");
    const fileName = document.getElementById("fileName");

    const clearButton = document.getElementById("clearButton");
    const textForm = document.getElementById("textForm");
    const errorMessage = document.getElementById("errorMessage");

    const themeToggle = document.getElementById("themeToggle");


    // ==============================
    // CHARACTER COUNTER
    // ==============================

    if (textInput && characterCount) {

        textInput.addEventListener("input", function () {

            characterCount.textContent = this.value.length;

        });

    }


    // ==============================
    // FILE SELECTION
    // ==============================

    if (fileInput && fileName) {

        fileInput.addEventListener("change", function () {

            if (this.files.length > 0) {

                fileName.textContent =
                    "Selected: " + this.files[0].name;

            } else {

                fileName.textContent = "";

            }

        });

    }


    // ==============================
    // CLEAR BUTTON
    // ==============================

    if (clearButton) {

        clearButton.addEventListener("click", function () {

            textInput.value = "";
            fileInput.value = "";

            characterCount.textContent = "0";
            fileName.textContent = "";
            errorMessage.textContent = "";

        });

    }


    // ==============================
    // FORM VALIDATION
    // ==============================

    if (textForm) {

        textForm.addEventListener("submit", function (event) {

            const text = textInput.value.trim();
            const fileSelected = fileInput.files.length > 0;

            errorMessage.textContent = "";


            if (!text && !fileSelected) {

                event.preventDefault();

                errorMessage.textContent =
                    "Please enter text or upload a PDF/PPTX file.";

                return;

            }


            if (fileSelected) {

                const file = fileInput.files[0];

                const extension =
                    file.name.split(".").pop().toLowerCase();


                if (extension !== "pdf" && extension !== "pptx") {

                    event.preventDefault();

                    errorMessage.textContent =
                        "Only PDF and PPTX files are supported.";

                }

            }

        });

    }


    // ==============================
    // THEME TOGGLE
    // ==============================

    if (themeToggle) {

        themeToggle.addEventListener("click", function () {

            document.body.classList.toggle("dark-mode");

            if (document.body.classList.contains("dark-mode")) {

                themeToggle.textContent = "☀️";

            } else {

                themeToggle.textContent = "🌙";

            }

        });

    }

});