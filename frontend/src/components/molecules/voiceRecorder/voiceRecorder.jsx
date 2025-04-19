import React, { useState, useRef } from 'react';
import { ButtonComponent } from '../../atoms/button/button.jsx'
import { ButtonsGroupComponent } from '../../molecules/buttonsGroup/buttonsGroup.jsx'
import { Stack } from '@mui/material';
import { useDispatch } from 'react-redux';
import { addDiagramm } from '../../../store/diagrammSlice.js';
import { uploadAudioFile } from '../../../api/voiceTextApi.js';

const diagramm = `
graph TB
    sq[Square shape] --> ci((Circle shape))

    subgraph A
        od>Odd shape]-- Two line<br/>edge comment --> ro
        di{Diamond with <br/> line break} -.-> ro(Rounded<br>square<br>shape)
        di==>ro2(Rounded square shape)
    end

    %% Notice that no text in shape are added here instead that is appended further down
    e --> od3>Really long text with linebreak<br>in an Odd shape]

    %% Comments after double percent signs
    e((Inner / circle<br>and some odd <br>special characters)) --> f(,.?!+-*ز)

    cyr[Cyrillic]-->cyr2((Circle shape Начало));

     classDef green fill:#9f6,stroke:#333,stroke-width:2px;
     classDef orange fill:#f96,stroke:#333,stroke-width:4px;
     class sq,e green
     class di orange
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
                        console.log(mediaRecorderRef)
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
                    clickHandler={async () => {
                        dispatcher(addDiagramm(diagramm))
                        console.log('!!!', await uploadAudioFile(audioChunksRef))
                    }}
                />,
            ]}/>
        </Stack>
    );
};
