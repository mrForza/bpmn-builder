import * as React from 'react';
import { ButtonGroup } from '@mui/material';

export const ButtonsGroupComponent = ({buttons}) => {
    return (
        <ButtonGroup sx={{display: 'flex', justifyContent: 'center', boxShadow: 'none'}} variant="contained" color="primary" aria-label="group">
            {buttons.map((button) => (button))}
        </ButtonGroup>
    );
}