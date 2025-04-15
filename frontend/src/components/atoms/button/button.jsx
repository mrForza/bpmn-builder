import * as React from 'react';
import Button from '@mui/material/Button';

const DEFAULT_PROPS = new Map([
    ['text', 'Lorem']
])

export const ButtonComponent = ({style, href, variant, clickHandler, color, text, startIcon}) => {
    return (
        <Button
            style={style}
            variant={variant}
            href={href}
            onClick={clickHandler}
            color={color}
            startIcon={startIcon}>
            {text === undefined ? DEFAULT_PROPS.get('text') : text}
        </Button>
    )
}