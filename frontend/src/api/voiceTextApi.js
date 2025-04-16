import axios from 'axios'

export const sendVoiceFile = async (audioFile) => {
    try {
        const response = await axios.post('http://localhost:8080/voice', {audio: audioFile});
        return response;
    } catch (err) {
        console.log(err)
    }
}

export const getVoiceText = async () => {
    try {
        const response = await axios.post('http://localhost:8080/text');
        return response;
    } catch (err) {
        console.log(err)
    }
}