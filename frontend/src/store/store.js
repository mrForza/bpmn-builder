import { configureStore } from '@reduxjs/toolkit'
import { voiceTextSlice } from './voiceTextSlice'
import { diagrammSlice } from './diagrammSlice'

export const store = configureStore({
    reducer: {
        voiceText: voiceTextSlice.reducer,
        diagramm: diagrammSlice.reducer,
    },
})
