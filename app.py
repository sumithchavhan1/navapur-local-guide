from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html") as f:
        return f.read()

@app.post("/ask-kiro")
async def ask_kiro(question: str = Form(...), category: str = Form(...)):
    response = generate_local_guide_response(question, category)
    return {"answer": response}

def generate_local_guide_response(question, category):
    """Generate response based on product.md knowledge base"""
    
    stalls_db = {
        "Anna Saheb Chai Tapri": {
            "location": "Bus Stand Circle",
            "items": "Cutting Chai (₹5), Vada Pav (₹15), Sabudana Vada (₹10)",
            "timing": "6AM-11PM",
            "note": "Always crowded evenings"
        },
        "Ramesh Misal Pav": {
            "location": "Main Bazaar",
            "items": "Misal Pav (₹25), Upma (₹15)",
            "timing": "7AM-2PM",
            "note": "Famous spicy misal"
        },
        "Suresh Bhaiya's Poha": {
            "location": "Station Road",
            "items": "Kanda Poha (₹20), Tea (₹7)",
            "timing": "8AM-1PM",
            "note": "Fresh poha with sev"
        },
        "Pinky Dabeli Stall": {
            "location": "Near Girls School",
            "items": "Dabeli (₹20), Bhel (₹25)",
            "timing": "4PM-10PM",
            "note": "Evening snack spot"
        },
        "Raju Bhai Sandwich": {
            "location": "Bus Stand",
            "items": "Veg Grill Sandwich (₹30), Cold Coffee (₹25)",
            "timing": "5PM-11PM",
            "note": "Late night option"
        }
    }
    
    q_lower = question.lower()
    
    # Street Food Recommendations
    if "evening" in q_lower or "snack" in q_lower or "spicy" in q_lower:
        return f"""Bhai, evening snack ke liye Navapur ka best option:

1. **Anna Saheb Chai Tapri** (Bus Stand)
   - Vada Pav ₹15, Sabudana Vada ₹10
   - 6AM-11PM | Always crowded evenings
   - Perfect chai pairing!

2. **Pinky Dabeli Stall** (Near Girls School)
   - Dabeli ₹20, Bhel ₹25 
   - 4PM-10PM | Evening snack spot
   - Fresh aur zada special!

3. **Raju Bhai Sandwich** (Bus Stand)
   - Veg Grill Sandwich ₹30
   - 5PM-11PM | Late night option

Cha paani ke liye Anna Saheb jaao bhai!"""
    
    elif "breakfast" in q_lower or "morning" in q_lower:
        return f"""Navapur morning ke liye best options:

1. **Suresh Bhaiya's Poha** (Station Road) ⭐
   - Kanda Poha ₹20 | Fresh sev wala!
   - 8AM-1PM | Most authentic
   - Local favorite sabhi log ka!

2. **Ramesh Misal Pav** (Main Bazaar)
   - Misal Pav ₹25
   - 7AM-2PM | Famous spicy
   - Tej masala ke liye famous!

3. **Anna Saheb Chai Tapri** (Bus Stand)
   - Cutting Chai ₹5, Vada Pav ₹15
   - 6AM-11PM | Always fresh
   - Garam chai aur salty vada!

Suresh Bhaiya ka poha try karna zaroori hai!"""
    
    elif "budget" in q_lower or "cheap" in q_lower or "under" in q_lower:
        return f"""Navapur mein budget ka kam budget hote hain:

1. **Anna Saheb Chai Tapri** (Bus Stand)
   - Cutting Chai SIRF ₹5! 🔥
   - Vada Pav ₹15
   - Best value for money

2. **Suresh Bhaiya's Poha** (Station Road)
   - Poha ₹20 (filling breakfast)
   - 8AM-1PM | Pocket-friendly

3. **Ramesh Misal Pav** (Main Bazaar)
   - Misal ₹25 | Filling lunch
   - 7AM-2PM

Chai pikar raste mein chal dena, pocket mein paisa rahe!"""
    
    else:
        return f"""Welcome to Navapur Local Guide! 🗺️

Ye lokde stalls Navapur mein famous hain:
- **Anna Saheb Chai Tapri** (Bus Stand) - Chai ₹5!
- **Ramesh Misal Pav** (Main Bazaar) - Spicy misal!
- **Suresh Bhaiya's Poha** (Station Road) - Fresh poha!
- **Pinky Dabeli Stall** (Girls School) - Evening snack!
- **Raju Bhai Sandwich** (Bus Stand) - Night time!

Kya chahiye? Evening snack? Breakfast? Spicy? Budget? Puche!"""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
