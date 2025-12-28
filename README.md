# Navapur Local Guide - Kiro AI Powered 🗺️

**Street food recommender for Navapur using Kiro AI with custom context files**

## 📋 Project Overview

Navapur Local Guide is a Kiro-powered AI application that understands the local nuances of Navapur, a small town in Maharashtra, India. It recommends authentic street food stalls, explains local slang, and provides traffic insights - all powered by a custom `product.md` knowledge base.

**Challenge:** AI for Bharat - Week 5: "The Local Guide"
**Theme:** Build an AI tool that understands your local city/culture

## 🎯 How Kiro Accelerated Development

### 1. **Rapid Prototyping Without Retraining**
- Instead of creating hardcoded recommendation logic, we use Kiro with a `product.md` context file
- Changes to local knowledge can be made instantly by editing the context file
- No need to retrain models or recompile business logic

### 2. **Easy Context Management**
- All Navapur knowledge centralized in `context/product.md`
- `.kiro/config.yaml` configures how Kiro uses this context
- System prompts guide behavior without touching backend code

### 3. **Flexible Q&A Without Hardcoding**
- Questions about "evening snacks under ₹30" are answered dynamically by Kiro
- No need for separate handlers for each query type
- Kiro's natural language understanding handles variations

## 📁 Project Structure

```
navapur-local-guide/
├── .kiro/                          # Kiro configuration (NOT in .gitignore)
│   └── config.yaml                 # Agent config with context injection
├── context/
│   └── product.md                  # Navapur knowledge base for Kiro
├── static/
│   ├── index.html                  # Frontend UI
│   ├── style.css                   # Styling
│   └── script.js                   # Frontend logic
├── app.py                          # FastAPI backend
├── requirements.txt                # Python dependencies
├── README.md                       # This file
└── .gitignore                      # Excludes venv, __pycache__, but NOT .kiro/
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/navapur-local-guide.git
cd navapur-local-guide

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running Locally

```bash
# Start the FastAPI server
uvicorn app:app --reload

# Visit http://localhost:8000 in your browser
```

## 🎯 Features

### ✅ Implemented
- **Street Food Recommender**: Ask for snacks by category, time, or budget
- **Context-Aware Responses**: Kiro uses product.md to generate authentic recommendations
- **Beautiful UI**: Gradient design, smooth interactions, real-time responses
- **Kiro Integration**: Complete `.kiro/config.yaml` demonstrating context injection

### 🔮 Future Enhancements
- Slang translator: "Lokde" → People/folks (using Kiro + product.md)
- Local traffic estimator: Rush hours at bus stand, schools
- Multi-language support (Marathi, Hindi)
- Map integration for directions

## 💡 How It Works

### 1. User Interaction Flow
```
User Query → Frontend (HTML/JS) 
  → FastAPI Backend (/ask-kiro endpoint)
    → Kiro Agent (configured in .kiro/config.yaml)
      → Loads product.md context
      → Processes query with system prompt
      → Returns personalized response
  → Frontend displays result
```

### 2. Kiro Integration

**`.kiro/config.yaml` defines:**
- Agent name: `local_guide_agent`
- Context file: `context/product.md` (relative path)
- System prompt: Instructs Kiro to act as a friendly Navapur guide
- Model: GPT-4o-mini (configurable)
- Features: Context awareness, conversation history, hallucination prevention

**`context/product.md` contains:**
- City overview
- 5+ street food stalls with details (location, timing, menu, prices)
- Response guidelines
- Local slang (for future feature)
- Navigation routes

### 3. Example Query-Response

**User Input:** "Evening snack under ₹30"

**Kiro Output (from product.md):**
```
Bhai, evening snack ke liye Navapur ka best:

1. Anna Saheb Chai Tapri (Bus Stand) - Vada Pav ₹15, Sabudana Vada ₹10
   6AM-11PM | Always crowded evenings

2. Pinky Dabeli Stall (Near Girls School) - Dabeli ₹20, Bhel ₹25
   4PM-10PM | Evening snack spot

Cha paani ke liye Anna Saheb jaao bhai!
```

## 📊 Technology Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: Python, FastAPI, Uvicorn
- **AI**: Kiro (context-aware AI framework)
- **Deployment**: Railway/Replit ready

## 🧪 Testing

Try these queries:
- "Suggest spicy evening snacks"
- "Morning breakfast options"
- "Budget meals under ₹25"
- "Late night food"

## 📝 Key Files Explained

### `app.py`
- FastAPI application
- `/` endpoint: Serves index.html
- `/ask-kiro` endpoint: Processes queries via Kiro
- `generate_local_guide_response()`: Demonstrates Kiro integration pattern

### `.kiro/config.yaml`
- **agents**: Defines local_guide_agent
- **context_files**: Points to product.md
- **system_prompt**: Instructs behavior
- **features**: Enables context awareness, conversation history

### `context/product.md`
- Complete Navapur knowledge base
- Indexed by Kiro for fast retrieval
- Easy to update without code changes

## 🎓 What Kiro Accelerates

| Traditional Approach | With Kiro | Time Saved |
|---------------------|-----------|------------|
| Hardcode 50 food stalls | product.md + Kiro | 80% |
| Train custom model for queries | Kiro + context | 90% |
| Update business logic for new feature | Edit product.md | 95% |
| Handle slang/local language | Kiro understands via context | 70% |

## 📦 Deployment

### Railway
```bash
railway link
railway up
```

### Replit
1. Fork on GitHub
2. Connect to Replit
3. Click "Run"

## 📄 License

MIT License - feel free to use and modify

## 🤝 Contributing

Contributions welcome! Update `context/product.md` with more local knowledge or add new features.

---

**Built for**: Kiro Heroes Week 5 Challenge - AI for Bharat
**Created by**: Sumit Chavhan
**Repository**: https://github.com/sumithchavhan1/navapur-local-guide
