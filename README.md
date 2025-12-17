# Chess AI Analyzer

AI-powered chess position analyzer that can:
- Recognize chess positions from photos
- Calculate the best move using Stockfish
- Evaluate position with detailed analysis

## Live Demo
- Frontend: https://yourusername.github.io/chess-ai-analyzer
- Backend API: https://your-backend.onrender.com

## Features
- 📸 Photo upload for board recognition
- 🤖 AI-powered move analysis
- 📊 Position evaluation with visual feedback
- ♟️ Interactive chess board
- 📱 Responsive design

## Deployment

### Backend (Render/Heroku)
1. Fork this repository
2. Create account on [Render](https://render.com)
3. Create new Web Service
4. Connect your GitHub repository
5. Set build command: `pip install -r backend/requirements.txt`
6. Set start command: `gunicorn app:app`
7. Add environment variable: `PORT=10000`

### Frontend (GitHub Pages)
1. Go to repository Settings
2. Navigate to Pages section
3. Set source to main branch, folder: `/frontend`
4. Save and wait for deployment

## Local Development

### Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
