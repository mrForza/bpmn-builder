import { createSlice } from '@reduxjs/toolkit'

export const diagrammSlice = createSlice({
    name: 'diagramm',
    initialState: {
        value: ''
    },
    reducers: {
        addDiagramm: (state, action) => {
            state.value = action.payload;
        },
        removeDiagramm: (state) => {
            state.value = '';
        },
    },
})

export const {addDiagramm, removeDiagramm} = diagrammSlice.actions;