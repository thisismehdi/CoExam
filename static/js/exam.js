const csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value
// varibale from the file above codeExam
let time = 0;
// the timer div
let clock = document.getElementById('timer')
// the duration of th exam
let timeMax = 10
// the timer
function startTimer(){
    if(localStorage.getItem("clock") != null)
        time = parseInt(localStorage.getItem('clock'))
    second = time%60 < 10 ? `0${time%60}`:`${time%60}`
    minute = Math.floor(time/60) < 10 ? `0${Math.floor(time/60)}`:`${Math.floor(time/60)}`
    clock.innerHTML=`${minute}:${second}`
    time++
    localStorage.setItem('clock',time)
    if(time >=timeMax*60)
    {
        clearInterval(timer)
    }
}
// start the timer
let timer
// get the exam from the server
const getExams = ()=>{
    $.ajax({
        type:'GET',
        // id exam coming from the view
        url:`/get-exam/${idExam}`,
        success:function(response){
            console.log("succues")
            // we fetched the exam succesfully
            setTimeout(()=>{
                // get the elements from the dom
                const quizEl = document.getElementById('quiz')
                const spinner = document.querySelector('.spinner-border')
                quizEl.classList.remove('d-none')
                spinner.classList.add('d-none')
                clock.classList.remove('d-none')
                setInterval(startTimer,1000)
                timeMax = 20
                // quizData is array of questions
                const quizData = response.data;
                /////lets get started
                const quiz = document.getElementById('quiz')
                const answerEls = document.querySelectorAll('.answer')
                const questionEl = document.getElementById('question')
                const a_text = document.getElementById('a_text')
                const b_text = document.getElementById('b_text')
                const c_text = document.getElementById('c_text')
                const d_text = document.getElementById('d_text')
                const submitBtn = document.getElementById('submit')

                // current question
                let currentQuiz = 0
                // current score
                let score = 0
                // load the score from the local storage if the user refresh the page
                if(localStorage.getItem('score')!==null)
                {
                    score = parseInt(localStorage.getItem('score'))
                }
                // load the cuurentQuiz from the local storage if the user refresh the page
                if(localStorage.getItem('currentQuiz')!==null)
                {
                    currentQuiz = parseInt(localStorage.getItem('currentQuiz'))
                }
                loadQuiz()
                // load the quiz function isto show the question on the dom
                function loadQuiz() {
                    const currentQuizData = quizData[currentQuiz]
                    questionEl.innerText = currentQuizData.question
                    a_text.innerText = currentQuizData.a
                    b_text.innerText = currentQuizData.b
                    c_text.innerText = currentQuizData.c
                    d_text.innerText = currentQuizData.d
                }
                // deselcting all the asnwers
                function deselectAnswes(){
                    answerEls.forEach(answerEls => answerEl.checked = false)
                }

                function getSelected(){
                    let answer
                    
                    answerEls.forEach(answerEl => {
                        if(answerEl.checked) {
                            answer = answerEl.id
                        }
                    })
                    return answer
                }


                submitBtn.addEventListener('click', () => {
                    const answer = getSelected()
                    // if the anwser is null the the user click submit without checking anything
                    if(answer) {
                        if(answer === quizData[currentQuiz].correct){
                            score++
                            localStorage.setItem('score',score)
                        }
                        
                        currentQuiz++
                        localStorage.setItem('currentQuiz',currentQuiz)

                        if(currentQuiz < quizData.length) {
                            loadQuiz()
                        } else {
                            localStorage.removeItem('score')
                            localStorage.removeItem('clock')
                            localStorage.removeItem('currentQuiz')
                            quiz.innerHTML = `
                                <h2>click sur le button pour voir votre resultat</h2>

                                <a href="/listDesNotes/" class="btn">click ici</a>
                            `
                            if(noFace > 0.3*count && noFace < 0.5*count)
                            {
                                score = score/parseFloat(2)
                            }else if(multiFaces > 0.1*count){
                                score = score - score/parseFloat(3)
                            }else if(detectAnotherFace > 0.3*count){
                                score = 0;
                            }
                            $.ajax({
                                type:'POST',
                                url:`/creerNote/`,
                                data:{
                                    'csrfmiddlewaretoken':csrftoken,
                                    'idStudent':idStudent,
                                    'idExam':idExam,
                                    'note':score/parseFloat(quizData.length)
                                },
                                success:function(response){
                                    console.log('note created')
                                },
                                error:function(error){
                                    console.log("moxkiiil")
                                }
                            })
                            
                        }
                    }
                })
                
            },500)
        },
        error:function(error){
            console.log("error")
        }
    })
}
        