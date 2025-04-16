import { createSlice } from '@reduxjs/toolkit'

export const voiceTextSlice = createSlice({
    name: 'voiceText',
    initialState: {
        value: ''
    },
    reducers: {
        addVoiceText: (state, action) => {
            state.value = action.payload;
        },
        removeVoiceText: (state) => {
            state.value = '';
        },
    },
})

export const {addVoiceText, removeVoiceText} = voiceTextSlice.actions;