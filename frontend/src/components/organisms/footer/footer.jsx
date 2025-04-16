import * as React from 'react';
import { Box, Typography, Container } from '@mui/material';

export const FooterComponent = ({}) => {
    return (
        <Box
            component="footer"
            sx={{
                py: 2,
                px: 1,
                mt: 'auto',
                backgroundColor: (theme) =>
                    theme.palette.mode === 'light' ? '#f5f5f5' : '#1a1a1a',
                textAlign: 'center',
                position: 'fixed',
                bottom: 0,
                width: '100%'
            }}
        >
            <Container maxWidth="md">
                <Typography variant="body2" color="text.secondary">
                    © {new Date().getFullYear()} BPMN-Builder. Все права защищены.
                </Typography>
            </Container>
        </Box>
    );
}