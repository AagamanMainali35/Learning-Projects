<!-- <script>
    let time = Number(document.getElementById("timer").textContent);
let questions = [
    "The term 'app' in the context of mobile devices stands for?",
    "Who is the author of the 'Harry Potter' series?",
    "In which sport would you perform a slam dunk?",
    "How many UEFA Champions League titles has Ronaldo won in his career?"
];
let options = [
    ["Application", "Apparatus", "Appendix", "Apprehension"],
    ["Socrates", "Joe Biden", "Colleen Hoover", "J.K. Rowling"],
    ["Table Tennis", "Polo", "Football", "Basketball"],
    ["6", "3", "5", "2"]
];
let answers = [0, 3, 3, 2];
let currentQuestionIndex = 0;

let questionDOM = document.getElementById("question");
let result = document.getElementById("result");

const countdown = () => {
    if (time >= 1) {
        time--;
        document.getElementById("timer").textContent = time;
    } else if (time == 0) {
        document.querySelector(".container2").style.height = '420px';
        result.textContent = 'You lose the game!';
        result.style.color = 'red';
        result.style.fontSize = '20px';
        result.style.fontFamily = 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
};
const loadQuestion = () => {
    questionDOM.textContent = questions[currentQuestionIndex];
    document.getElementById("option1").textContent = options[currentQuestionIndex][0];
    document.getElementById("option2").textContent = options[currentQuestionIndex][1];
    document.getElementById("option3").textContent = options[currentQuestionIndex][2];
    document.getElementById("option4").textContent = options[currentQuestionIndex][3];
};
const checkAnswer = (selectedOptionIndex) => {
    if (selectedOptionIndex === answers[currentQuestionIndex]) {
        result.textContent = 'Correct!';
        result.style.color = 'green';
    } else {
        result.textContent = 'Wrong!';
        result.style.color = 'red';
    }
    result.style.fontSize = '20px';
    result.style.fontFamily = 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
};
document.getElementById("option1").addEventListener("click", () => checkAnswer(0));
document.getElementById("option2").addEventListener("click", () => checkAnswer(1));
document.getElementById("option3").addEventListener("click", () => checkAnswer(2));
document.getElementById("option4").addEventListener("click", () => checkAnswer(3));
setInterval(countdown, 1000);
loadQuestion();

 </script> -->