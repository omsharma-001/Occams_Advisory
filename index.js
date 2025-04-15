import express from 'express';
import dotenv from 'dotenv';
import path from 'path';
import axios from 'axios';
import cors from 'cors';
import { fileURLToPath } from 'url';  // Import to use import.meta.url

dotenv.config();

const app = express();
app.use(express.json());
app.use(cors());  // Enable CORS to allow requests from other origins

// Use import.meta.url to get the current directory
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Route to serve the index.html file at the root URL
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Route to handle the 'ask' POST request from the frontend
app.post('/ask', async (req, res) => {
  const { question } = req.body;
  try {
    const response = await axios.post('http://127.0.0.1:8000/ask', { question });
    const { answer } = response.data;
    res.json({ answer });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Failed to generate answer' });
  }
});

// Set the port number for the Node.js server to listen on
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
