import * as React from 'react';
import Button from '@mui/material/Button';
import SendIcon from '@mui/icons-material/Send';

const DEFAULT_PROPS = new Map([
    ['style', {}],
    ['href', '#'],
    ['variant', 'contained'],
    ['clickHandler', () => {}],
    ['color', 'success'],
    ['text', 'Text123'],
    ['endIcon', <SendIcon />],
])

export const setPropsItem = (name, propsItem) => {
    return propsItem === undefined ?
        DEFAULT_PROPS.get(name) : propsItem
}

export const ButtonComponent = ({style, href, variant, clickHandler, color, text, endIcon, enable, download}) => {
    return (
        <Button
            sx={setPropsItem('style', style)}
            variant={setPropsItem('variant', variant)}
            href={setPropsItem('href', href)}
            onClick={setPropsItem('clickHandler', clickHandler)}
            endIcon={setPropsItem('endIcon', endIcon)}
            color={setPropsItem('color', color)}
            size='small'
            disabled={!enable}
            download={download}>
            {setPropsItem('text', text)}
        </Button>
    )
}