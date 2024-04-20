// EmailConfirmation.js

import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const EmailConfirmation = () => {
    const { uid, token } = useParams();
    const [confirmationMessage, setConfirmationMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    useEffect(() => {
        const confirmEmail = async () => {
            try {
                await axios.get(`http://localhost:8000/api/confirm-email/${uid}/${token}/`);
                setConfirmationMessage('Email confirmation successful! You can now log in.');
                setErrorMessage('');
            } catch (error) {
                setErrorMessage('Email confirmation failed. Please try again.');
                setConfirmationMessage('');
            }
        };

        confirmEmail();
    }, [uid, token]);

    return (
        <div>
            <h2>Email Confirmation</h2>
            {confirmationMessage && <p>{confirmationMessage}</p>}
            {errorMessage && <p>{errorMessage}</p>}
        </div>
    );
};

export default EmailConfirmation;
