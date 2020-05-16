const startBtn = document.getElementById('start-record')
const stopBtn = document.getElementById('stop-record')
const playBtn = document.getElementById('play-record')
const uploadServerBtn = document.getElementById('upload-server')
const statusElement = document.getElementById('status')
// const input = document.getElementById('input')
const content = document.getElementById('content')

var AudioContext = window.AudioContext || window.webkitAudioContext;
var audioContext //audio context to help us record

var gumStream; 						//stream from getUserMedia()
var rec; 							//Recorder.js object
var input; 							//MediaStreamAudioSourceNode we'll be recording

stopBtn.classList.add('disabled')
startBtn.classList.add('active')

startBtn.addEventListener("click", startRecording)
stopBtn.addEventListener("click", stopRecording)

function startRecording() {
    stopBtn.classList.replace("disabled", "active")
    startBtn.classList.replace("active", "disabled")
    statusElement.innerText = "Recording"
    navigator.mediaDevices.getUserMedia({
        audio: true,
        video: false
    })
        .then(function (stream) {
            console.log("stream created")

            audioContext = new AudioContext();
            document.getElementById("formats").innerHTML = "Format: 1 channel pcm @ " + audioContext.sampleRate + "Hz"

            gumStream = stream;

            input = audioContext.createMediaStreamSource(stream);

            console.log(input)

            rec = new Recorder(input, { numChannels: 1 })

            //start the recording process
            rec.record()

            console.log("Recording started");
        })
}


function stopRecording() {
    startBtn.classList.replace("disabled", "active")
    stopBtn.classList.replace("active", "disabled")
    statusElement.innerText = "Finished"
    console.log("stopButton clicked");

    //tell the recorder to stop the recording
    rec.stop();

    //stop microphone access
    gumStream.getAudioTracks()[0].stop();

    //create the wav blob and pass it on to createDownloadLink
    rec.exportWAV(createDownloadLink);
}


function createDownloadLink(blob) {
    console.log(blob)


    const formData = new FormData();
    formData.append('file', blob)
    fetch("/api", {
        method: "POST",
        body: formData,
        // body: JSON.stringify(data),
    }).then(res => {
        res.json().then(data => {
            console.log(data)
            content.innerText = "Từ của bạn: " + data.alternative[data.alternative.length - 1].transcript

        })
            .catch(err => alert('Some thing happen, try again'))
        // console.log("Request complete! response:", res.body);
    });
}