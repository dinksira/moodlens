# mood.py

def interpret_mood(text: str) -> str:
    if not text:
        return "neutral"

    text = text.lower()

    mood_keywords = {
        "happy": ["happy", "joy", "excited", "great", "fun", "love"],
        "sad": ["sad", "down", "tired", "lonely", "upset", "depressed"],
        "angry": ["angry", "mad", "furious", "annoyed", "frustrated"],
        "calm": ["calm", "peaceful", "relaxed", "chill", "quiet"]
    }

    for mood, keywords in mood_keywords.items():
        for word in keywords:
            if word in text:
                return mood

    return "neutral"
