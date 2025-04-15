import Stack from '@mui/material/Stack';
import { TextFieldComponent } from '../../atoms/textField/textField.jsx'
import { ButtonComponent } from '../../atoms/button/button.jsx'
import { ButtonsGroupComponent } from '../../molecules/buttonsGroup/buttonsGroup.jsx'

export const WarningsSectionComponent = ({}) => {
    return (
        <Stack sx={{width: '45%', display: 'flex', justifyContent: 'center'}} spacing={2}>
            <TextFieldComponent
                label='Предупреждения BPMN анализатора'
                defaultValue=''
                rows={4}
                cols={22}
                color=''
                onChangeHandler={() => {}}
                style={{}}
                size='medium'
            />
            <TextFieldComponent
                label='Пользовательские предупреждения'
                defaultValue=''
                rows={4}
                cols={22}
                color=''
                onChangeHandler={() => {}}
                style={{}}
                size='medium'
            />
            <ButtonsGroupComponent buttons={[
                <ButtonComponent color='success' text='Применить правки анализатора' style={{marginLeft: '10px'}}/>,
                <ButtonComponent color='success' text='Применить правки пользователя' style={{marginLeft: '10px'}}/>,
            ]}/>
        </Stack>
    );
}