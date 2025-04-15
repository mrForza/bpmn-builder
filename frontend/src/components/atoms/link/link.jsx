import * as React from 'react';
import { ListItemButton, ListItemText } from '@mui/material';

export const NavLinkComponent = ({ to, label }) => {
    return (
        <ListItemButton component="a" to={to}>
            <ListItemText primary={label} />
        </ListItemButton>
    );
}