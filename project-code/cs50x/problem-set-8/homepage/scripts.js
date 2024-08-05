document.addEventListener('DOMContentLoaded', (event) => {
    const questions = [
        {
            question: "What is the capital of France?",
            choices: ["Paris", "London", "Berlin", "Madrid"],
            answer: "Paris"
        },
        {
            question: "What is 2 + 2?",
            choices: ["3", "4", "5", "6"],
            answer: "4"
        },
        {
            question: "What is the chemical symbol for water?",
            choices: ["HO", "H2O", "O2", "HO2"],
            answer: "H2O"
        },
    ];

    const triviaQuestionsElement = document.getElementById('trivia-questions');
    const submitButton = document.getElementById('submit-button');
    const resetButton = document.getElementById('reset-button');
    const resultElement = document.getElementById('result');
    let currentQuestions = [];

    function getRandomQuestions() {
        let shuffled = questions.sort(() => 0.5 - Math.random());
        return shuffled.slice(0, 3);
    }

    function displayQuestions() {
        currentQuestions = getRandomQuestions();
        triviaQuestionsElement.innerHTML = '';
        currentQuestions.forEach((q, index) => {
            const questionCard = document.createElement('div');
            questionCard.className = 'card mb-4';
            questionCard.innerHTML = `
                <div class="card-body">
                    <h5 class="card-title">Question ${index + 1}</h5>
                    <p class="card-text">${q.question}</p>
                    ${q.choices.map((choice, i) => `
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="question${index}" id="q${index}c${i}" value="${choice}">
                            <label class="form-check-label" for="q${index}c${i}">
                                ${choice}
                            </label>
                        </div>
                    `).join('')}
                </div>
            `;
            triviaQuestionsElement.appendChild(questionCard);
        });
    }

    function checkAnswers() {
        let score = 0;
        currentQuestions.forEach((q, index) => {
            const selectedOption = document.querySelector(`input[name="question${index}"]:checked`);
            if (selectedOption && selectedOption.value === q.answer) {
                score++;
            }
        });
        resultElement.innerHTML = `<h4>Your score is: ${score} out of ${currentQuestions.length}</h4>`;
    }

    function resetTrivia() {
        displayQuestions();
        resultElement.innerHTML = '';
        submitButton.disabled = false;
        resetButton.disabled = true;
    }

    submitButton.addEventListener('click', () => {
        checkAnswers();
        submitButton.disabled = true;
        resetButton.disabled = false;
    });

    resetButton.addEventListener('click', resetTrivia);

    displayQuestions();
});
