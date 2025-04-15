import * as React from 'react';
import { AppBar, Toolbar, Typography, Box } from '@mui/material';
import { ButtonComponent } from '../../atoms/button/button.jsx'

export const HeaderComponent = ({}) => {
    return (
        <AppBar position="static" color="primary">
            <Toolbar sx={{ justifyContent: 'space-between' }}>
                <Typography variant="h6" component="div">
                    BPMN-Builder
                </Typography>
                <Box sx={{ display: 'flex', gap: 5, justifyContent: 'right', flexGrow: 1 }}>
                    <ButtonComponent variant='outlined' color='-' text='Главная'/>
                    <ButtonComponent variant='outlined' color='-' text='История'/>
                </Box>
            </Toolbar>
        </AppBar>
    );
}