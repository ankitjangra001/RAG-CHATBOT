const API = "http://127.0.0.1:8000";

const uploadBtn = document.getElementById("uploadBtn");
const pdfFile = document.getElementById("pdfFile");
const pdfName = document.getElementById("pdfName");
const uploadInfo = document.getElementById("uploadInfo");

const question = document.getElementById("question");
const sendBtn = document.getElementById("sendBtn");
const chatBox = document.getElementById("chatBox");

// Upload Button

uploadBtn.addEventListener("click", () => {

    pdfFile.click();

});

// File Selected

pdfFile.addEventListener("change", async function () {

    console.log("Change event fired");

    const file = this.files[0];

    console.log(file);

    if (!file) return;

    pdfName.textContent = "📄 " + file.name;

    console.log("PDF Name Changed:", pdfName.textContent);

    
});


// Send Question

sendBtn.addEventListener("click", askQuestion);

question.addEventListener("keypress", function (e) {

    if (e.key === "Enter") {

        askQuestion();

    }

});


async function askQuestion() {

    const q = question.value.trim();

    if (q === "") return;

    chatBox.innerHTML += `
        <div class="user">${q}</div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;

    question.value = "";

    try {

        const response = await fetch(API + "/chat", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                question: q

            })

        });

        const data = await response.json();

        chatBox.innerHTML += `
            <div class="bot">${data.answer}</div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

    }

    catch (error) {

        chatBox.innerHTML += `
            <div class="bot">
                Server Error
            </div>
        `;

    }

}