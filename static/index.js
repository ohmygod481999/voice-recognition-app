const startBtn = document.getElementById('start-record')
const stopBtn = document.getElementById('stop-record')
const playBtn = document.getElementById('play-record')
const uploadServerBtn = document.getElementById('upload-server')
const statusElement = document.getElementById('status')
const input = document.getElementById('input')
const content = document.getElementById('content')

const sleep = time => new Promise(resolve => setTimeout(resolve, time));

let audio = null;
playBtn.style.display = "none";

(async () => {
    let recorder
    startBtn.addEventListener('click', async function () {
        recorder = await voiceRecorder();
        audio = null
        playBtn.style.display = "none"
        recorder.start();
        statusElement.innerText = 'Recording...'
    })

    stopBtn.addEventListener('click', async function () {
        playBtn.style.display = ""
        audio = await recorder.stop();
        statusElement.innerText = 'Finished'
    })

    playBtn.addEventListener('click', function () {
        audio.play();
    })

})();

uploadServerBtn.addEventListener('click', function () {
    let file = audio.audioBlob;
    let data = { element: "cc" };
    
    const formData = new FormData();
    formData.append('file', file)
    fetch("/api", {
        method: "POST",
        body: formData,
        // body: JSON.stringify(data),
    }).then(res => {
        res.json().then(data => {
            content.innerText =  JSON.stringify(data)

        })
        console.log("Request complete! response:", res.body);
    });
})