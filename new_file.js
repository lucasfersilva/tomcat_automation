window.startRecording = function() {
    chunks = [];
    mediaRecorder.start();
}

window.stopRecording = function() {
    mediaRecorder.stop();
    var blob = new Blob(chunks, {'type' : 'audio/wav'});
    var audioURL = window.URL.createObjectURL(blob);
    uploadAudio(audioURL);
}

window.uploadAudio = function(audioURL) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload', true);
    xhr.setRequestHeader('Content-Type', 'audio/wav');
    xhr.send(audioURL);
}
