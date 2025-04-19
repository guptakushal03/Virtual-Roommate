import random

reminder_categories = {
    "hydration": {
        "interval_range": (1500, 2100),  # 25 - 35 mins
        "quotes": {
            "gremlin": [
                "Drink some water, dehydrated goblin!",
                "Sip sip, hydrate or diedrate.",
                "Water time! You ain’t a cactus."
            ],
            "zen": [
                "Take a moment and drink some water 💧",
                "Hydration is peace. Sip slowly.",
                "Inhale calm, exhale stress, drink water."
            ]
        }
    },
    "eyes": {
        "interval_range": (2400, 3000), # 40 - 50 mins
        "quotes": {
            "gremlin": [
                "Your eyeballs need a break, you screen zombie!",
                "Blink! Or are your eyes glued now?",
                "Look at a tree or something, jeez."
            ],
            "zen": [
                "Rest your eyes for a few moments 👁️",
                "Gaze into the distance and relax.",
                "Breathe and soften your gaze."
            ]
        }
    },
    "stretching": {
        "interval_range": (4800, 6000),  # 50 - 70 mins
        "quotes": {
            "gremlin": [
                "STRETCH! Or become one with your chair.",
                "Unfold those limbs, you keyboard gremlin!",
                "Stand up before I throw your chair!"
            ],
            "zen": [
                "Let’s stretch gently. Reach for the sky.",
                "Move with the breath. Feel the flow.",
                "Pause. Stretch. Refresh."
            ]
        }
    },
    "breathing": {
        "interval_range": (900, 1500),  # 15 - 25 mins
        "quotes": {
            "gremlin": [
                "Breathe, dummy! You forgot again, didn’t you?",
                "Inhale chaos, exhale chaos. Try it!",
                "Breathing’s free. Do it now."
            ],
            "zen": [
                "Close your eyes. Inhale. Hold. Exhale. ☁️",
                "Feel the breath calm your nerves.",
                "Breathe in peace, breathe out tension."
            ]
        }
    },
    "mindfulness": {
        "interval_range": (4800, 6000),  # 50 - 70 mins
        "quotes": {
            "gremlin": [
                "Unclench your jaw. I dare you.",
                "Cease the doomscrolling. Reflect instead.",
            ],
            "zen": [
                "Take a deep breath. In... and out...",
                "Unwind. The moment is now.",
            ]
        }
    },
    "posture": {
        "interval_range": (2400, 3000),  # 40 - 50 mins
        "quotes": {
            "gremlin": [
                "Unshrimp yourself 🦐",
                "Fix your spine before it becomes spaghetti!",
                "Sit up! You look like a boiled noodle."
            ],
            "zen": [
                "Gently align your back. Feel tall.",
                "Breathe into good posture.",
                "Let your spine lift you upward. 🌿"
            ]
        }
    }
}

def get_random_quote(category, personality="gremlin"):
    return random.choice(reminder_categories[category]["quotes"][personality])