import * as React from 'react';
import { TextField } from '@mui/material';

const DEFAULT_PROPS = new Map([
    ['style', {}],
    ['label', 'Label of text field'],
    ['rows', 4],
    ['cols', 20],
    ['color', 'secondary'],
    ['onChangeHandler', () => {}],
    ['placeholder', 'Placeholder of text field'],
])

export const setPropsItem = (name, propsItem) => {
    return propsItem === undefined ?
        DEFAULT_PROPS.get(name) : propsItem
}

export const TextFieldComponent = ({label, rows, cols, color, onChangeHandler, style, defaultValue, size}) => {
    return (
        <TextField
            id="outlined-multiline-static"
            label={setPropsItem('label', label)}
            size={setPropsItem('size', size)}
            multiline
            rows={setPropsItem('rows', rows)}
            cols={setPropsItem('cols', cols)}
            color={setPropsItem('color', color)}
            defaultValue={setPropsItem('defaultValue', defaultValue)}
            sx={setPropsItem('style', style)}
            onChange={setPropsItem('onChangeHandler', onChangeHandler)}
            style={setPropsItem('style', style)}
        />
    );
}