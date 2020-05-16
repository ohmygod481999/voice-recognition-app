const voiceRecorder = () => {
    return new Promise(resolve => {
      navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
          console.log(stream)
          const mediaRecorder = new MediaRecorder(stream);
          const audioChunks = [];
  
          mediaRecorder.addEventListener("dataavailable", event => {
            audioChunks.push(event.data);
          });
  
          const start = () => {
            mediaRecorder.start();
          };
  
          const stop = () => {
            return new Promise(resolve => {
              mediaRecorder.addEventListener("stop", () => {
                const audioBlob = new Blob(audioChunks, 
                  {
                    type: 'audio/wav'
                }
                );
                console.log(audioBlob)
                const audioUrl = URL.createObjectURL(audioBlob);
                console.log(audioUrl)
                const audio = new Audio(audioUrl);
                const play = () => {
                  audio.play();
                };
  
                resolve({ audioBlob, audioUrl, play });
              });
  
              mediaRecorder.stop();
            });
          };
  
          resolve({ start, stop });
        });
    });
  };