let mediaRecorder;
let recordedBlobs;

document.querySelector('#start').addEventListener('click', async () => {
    const stream = await navigator.mediaDevices.getUserMedia({audio: true});
    mediaRecorder = new MediaRecorder(stream);
    recordedBlobs = [];
    mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
            recordedBlobs.push(event.data);
        }
    };
    mediaRecorder.start();
    document.querySelector('#start').disabled = true;
    document.querySelector('#stop').disabled = false;
});

document.querySelector('#stop').addEventListener('click', () => {
    mediaRecorder.stop();
    document.querySelector('#start').disabled = false;
    document.querySelector('#stop').disabled = true;
});

document.querySelector('#start').addEventListener('click', async () => {
    const stream = await navigator.mediaDevices.getUserMedia({audio: true});
    mediaRecorder = new MediaRecorder(stream);
    recordedBlobs = [];
    mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
            recordedBlobs.push(event.data);
        }
    };
    mediaRecorder.start();
    document.querySelector('#start').disabled = true;
    document.querySelector('#stop').disabled = false;

    mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
            recordedBlobs.push(event.data);
            const audioBlob = new Blob(recordedBlobs, {type: 'audio/webm'});
            const audioUrl = URL.createObjectURL(audioBlob);
            const audio = document.querySelector('#player');
            audio.src = audioUrl;
        }
    };
});
