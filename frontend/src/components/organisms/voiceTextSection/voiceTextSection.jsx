import Stack from '@mui/material/Stack';
import { TextFieldComponent } from '../../atoms/textField/textField.jsx'
import { VoiceRecorder } from '../../molecules/voiceRecorder/voiceRecorder.jsx'
import { useSelector } from 'react-redux';

export const VoiceTextSectionComponent = ({}) => {
    const voiceText = useSelector((state) => state.voiceText.value)

    return (
        <Stack sx={{width: '45%'}} spacing={2}>
            <TextFieldComponent
                label={voiceText === '' ? 'Текст для генерации BPMN диаграммы' : voiceText}
                defaultValue=''
                rows={4}
                cols={22}
                color=''
                onChangeHandler={() => {}}
                style={{}}
                size='medium'
            />
            <VoiceRecorder/>
        </Stack>
    );
}