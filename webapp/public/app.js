let questions = [];
let currentQuestionIndex = 0;
let questionAnswered = false;

async function loadQuestions() {
  try {
    const response = await fetch("http://localhost:3000/api/questions");
    const data = await response.json();
    questions = data.questions; // Access the questions array from the JSON structure
    showQuestion(currentQuestionIndex);
  } catch (error) {
    console.error("Error loading questions:", error);
    document.getElementById("question-text").textContent =
      "Error loading questions. Please try again.";
  }
}

function showQuestion(index) {
  if (!questions || questions.length === 0) {
    document.getElementById("question-text").textContent =
      "No questions available.";
    return;
  }

  // Reset question state
  questionAnswered = false;

  const question = questions[index];
  const questionText = document.getElementById("question-text");
  const answersContainer = document.getElementById("answers-container");
  const nextButton = document.getElementById("next-btn");

  questionText.textContent = question.question;
  answersContainer.innerHTML = "";

  question.answers.forEach((answer, i) => {
    const button = document.createElement("button");
    button.className = "answer-btn";
    button.textContent = answer;
    button.onclick = () => selectAnswer(i);
    answersContainer.appendChild(button);
  });

  // Update next button state
  nextButton.disabled = index >= questions.length - 1;
}

function selectAnswer(answerIndex) {
  // Prevent selecting another answer if question is already answered
  if (questionAnswered) {
    return;
  }

  questionAnswered = true;
  const question = questions[currentQuestionIndex];
  const buttons = document.querySelectorAll(".answer-btn");

  buttons.forEach((button) => {
    button.style.backgroundColor = "";
    button.style.color = "";
    // Disable all buttons after selection
    button.disabled = true;
  });

  const selectedButton = buttons[answerIndex];
  if (answerIndex === question.correctAnswer) {
    selectedButton.style.backgroundColor = "#22c55e";
    selectedButton.style.color = "white";
  } else {
    selectedButton.style.backgroundColor = "#ef4444";
    selectedButton.style.color = "white";
    buttons[question.correctAnswer].style.backgroundColor = "#22c55e";
    buttons[question.correctAnswer].style.color = "white";
  }

  // Show explanation
  const explanationDiv = document.createElement("div");
  explanationDiv.className = "explanation";
  explanationDiv.textContent = question.explanation;
  document.getElementById("answers-container").appendChild(explanationDiv);
}

function nextQuestion() {
  if (currentQuestionIndex < questions.length - 1) {
    currentQuestionIndex++;
    showQuestion(currentQuestionIndex);
  }
}

// Add event listeners
document.addEventListener("DOMContentLoaded", loadQuestions);
document.getElementById("next-btn").addEventListener("click", nextQuestion);
