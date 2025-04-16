import Stack from '@mui/material/Stack';
import { HeaderComponent } from '../../organisms/header/header.jsx'
import { FooterComponent } from '../../organisms/footer/footer.jsx'
import { VoiceTextSectionComponent } from '../../organisms/voiceTextSection/voiceTextSection.jsx'
import { WarningsSectionComponent } from '../../organisms/warningsSection/warningsSection.jsx'
import DiagramSectionComponent from '../../organisms/diagramSection/diagramSection.jsx'
import { useSelector } from 'react-redux';


export const MainPage = () => {
    const diagramm = useSelector((state) => state.diagramm.value);
    
    return (
        <Stack spacing={2}>
            <HeaderComponent/>
            <Stack sx={{display: 'flex', justifyContent: 'center', width: '100%'}} spacing={2} direction={'row'}>
                <VoiceTextSectionComponent/>
                <WarningsSectionComponent/>
            </Stack>
            <DiagramSectionComponent chart={diagramm}/>
            <FooterComponent/>
        </Stack>
    );
}