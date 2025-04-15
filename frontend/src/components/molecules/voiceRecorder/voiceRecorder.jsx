import React, { useState, useRef } from 'react';

export const VoiceRecorder = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [audioUrl, setAudioUrl] = useState(null);
  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);

    const startRecording = async () => {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        const mediaRecorder = new MediaRecorder(stream);
        mediaRecorderRef.current = mediaRecorder;
        audioChunksRef.current = [];

        mediaRecorder.ondataavailable = (event) => {
            audioChunksRef.current.push(event.data);
        };

        mediaRecorder.onstop = () => {
            const blob = new Blob(audioChunksRef.current, { type: 'audio/wav' });
            const url = URL.createObjectURL(blob);
            setAudioUrl(url);
        };

        mediaRecorder.start();
        setIsRecording(true);
    };

    const stopRecording = () => {
        mediaRecorderRef.current.stop();
        setIsRecording(false);
    };

    return (
        <div>
            <button onClick={isRecording ? stopRecording : startRecording}>
                {isRecording ? 'Стоп' : 'Запись'}
            </button>

            {audioUrl && (
                <div>
                    <p>Результат:</p>
                    <audio src={audioUrl} controls />
                    <a href={audioUrl} download="recording.wav">Скачать</a>
                </div>
            )}
        </div>
    );
};
