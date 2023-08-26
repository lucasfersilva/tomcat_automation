var mediaRecorder;
var chunks = [];

navigator.mediaDevices.getUserMedia({audio: true})
.then(function(stream) {
    mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.ondataavailable = function(e) {
        chunks.push(e.data);
    }
});

function startRecording() {
    chunks = [];
    mediaRecorder.start();
}

function stopRecording() {
    mediaRecorder.stop();
    var blob = new Blob(chunks, {'type' : 'audio/wav'});
    var audioURL = window.URL.createObjectURL(blob);
    uploadAudio(audioURL);
}

function uploadAudio(audioURL) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload', true);
    xhr.setRequestHeader('Content-Type', 'audio/wav');
    xhr.send(audioURL);
}
