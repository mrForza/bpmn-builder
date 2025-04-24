import axios from 'axios'

export const uploadAudioFile = async (audioFile) => {
    try {
        const file = new File([audioFile], 'test.mp3')
        return await axios.post(
            'http://localhost:8000/voice',
            {audio_file: file},
            {
                headers: {
                    'Content-Type': `multipart/form-data`,
                },
            }
        );
    } catch (err) {
        console.log(err)
        return ''
    }
}

export const getVoiceText = async () => {
    try {
        const response = await axios.post('http://localhost:8000/text');
        return response;
    } catch (err) {
        console.log(err)
    }
}