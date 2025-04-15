import Stack from '@mui/material/Stack';
import { TextFieldComponent } from '../../atoms/textField/textField.jsx'
import { ButtonComponent } from '../../atoms/button/button.jsx'
import { ButtonsGroupComponent } from '../../molecules/buttonsGroup/buttonsGroup.jsx'
import { VoiceRecorder } from '../../molecules/voiceRecorder/voiceRecorder.jsx'

export const VoiceTextSectionComponent = ({}) => {
    return (
        <Stack sx={{width: '45%'}} spacing={2}>
            <TextFieldComponent
                label='Текст для генерации BPMN диаграммы'
                defaultValue=''
                rows={4}
                cols={22}
                color=''
                onChangeHandler={() => {}}
                style={{}}
                size='medium'
            />
            <VoiceRecorder/>
            <ButtonsGroupComponent buttons={[
                <ButtonComponent color='success' text='Запись' style={{marginLeft: '10px'}}/>,
                <ButtonComponent color='success' text='Стоп' style={{marginLeft: '10px'}}/>,
                <ButtonComponent color='success' text='Скачать' style={{marginLeft: '10px'}}/>,
                <ButtonComponent color='success' text='Сгенерировать текст' style={{marginLeft: '10px'}}/>,
            ]}/>
        </Stack>
    );
}