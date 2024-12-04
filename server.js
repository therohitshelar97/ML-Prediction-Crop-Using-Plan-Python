
const express = require('express');
const fetch = require('node-fetch');
const cors = require('cors');
const path = require('path');

const app = express();
app.use(express.json());
app.use(cors());
app.use(express.static(path.join(__dirname, 'public')));

const API_URL = 'https://private.au-syd.ml.cloud.ibm.com/ml/v4/deployments/a8d5036b-9fea-4b62-97d7-585be56b36e7/predictions?version=2021-05-01';
const API_KEY = '<YOUR_API_KEY>';

// Proxy endpoint for prediction
app.post('/api/predict', async (req, res) => {
    const { PH, Temp, N, P, K } = req.body;

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${API_KEY}`
        },
        body: JSON.stringify({
            input_data: [{
                fields: ['PH', 'Temp', 'N', 'P', 'K'],
                values: [[PH, Temp, N, P, K]]
            }]
        })
    };

    try {
        const response = await fetch(API_URL, options);
        const data = await response.json();
        res.json(data);
    } catch (error) {
        console.error('Error:', error);
        res.status(500).send('Error calling prediction API');
    }
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
