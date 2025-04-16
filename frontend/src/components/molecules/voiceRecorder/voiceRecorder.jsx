import React, { useState, useRef } from 'react';
import { ButtonComponent } from '../../atoms/button/button.jsx'
import { ButtonsGroupComponent } from '../../molecules/buttonsGroup/buttonsGroup.jsx'
import { Stack } from '@mui/material';
import { useDispatch } from 'react-redux';
import { addDiagramm } from '../../../store/diagrammSlice.js';

const d = `
sequenceDiagram
  participant Alice
  participant Bob
  Alice->>Bob: Hello Bob, how are you?
  Bob-->>Alice: I am good thanks!
`

export const VoiceRecorder = () => {
    const [isRecording, setIsRecording] = useState(false);
    
    const [audioUrl, setAudioUrl] = useState(null);
    
    const mediaRecorderRef = useRef(null);
    
    const audioChunksRef = useRef([]);

    const [recordEnable, setRecordEnable] = useState(true)

    const [stopEnable, setStopEnable] = useState(false)

    const [downloadEnable, setDownloadEnable] = useState(false)

    const [generateEnable, setGenerateEnable] = useState(false)

    const dispatcher = useDispatch()

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
        <Stack direction={'row'}>
            <audio src={audioUrl} controls />

            <ButtonsGroupComponent buttons={[
                <ButtonComponent
                    color='success'
                    text='Запись'
                    style={{marginLeft: '10px'}}
                    enable={recordEnable}
                    clickHandler={() => {
                        setRecordEnable(false)
                        setStopEnable(true)
                        setDownloadEnable(false)
                        setGenerateEnable(false)
                        startRecording()
                    }}
                />,
                <ButtonComponent
                    color='success'
                    text='Стоп'
                    style={{marginLeft: '10px'}}
                    enable={stopEnable}
                    clickHandler={() => {
                        setRecordEnable(true)
                        setStopEnable(false)
                        setDownloadEnable(true)
                        setGenerateEnable(true)
                        stopRecording()
                    }}
                />,
                <ButtonComponent
                    color='success'
                    text='Скачать'
                    style={{marginLeft: '10px'}}
                    enable={downloadEnable}
                    href={audioUrl}
                    download="recording.wav"
                />,
                <ButtonComponent
                    color='success'
                    text='Сгенерировать текст'
                    style={{marginLeft: '10px'}}
                    enable={generateEnable}
                    clickHandler={() => {
                        dispatcher(addDiagramm(d))
                    }}
                />,
            ]}/>
        </Stack>
    );
};
