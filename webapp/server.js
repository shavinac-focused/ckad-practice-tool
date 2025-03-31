const express = require('express');
const path = require('path');
const cors = require('cors');
const fs = require('fs').promises;

const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Serve questions
app.get('/api/questions', async (req, res) => {
    try {
        const questions = await fs.readFile(path.join(__dirname, 'data', 'questions.json'), 'utf8');
        res.json(JSON.parse(questions));
    } catch (error) {
        res.status(500).json({ error: 'Failed to load questions' });
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
