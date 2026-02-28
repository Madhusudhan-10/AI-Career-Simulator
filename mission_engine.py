import random

# -----------------------------------
# Rule-Based AI Mission Generator
# -----------------------------------

MISSIONS = {
    "frontend": {
        "beginner": [
            "Build a responsive landing page",
            "Create a login form with validation",
            "Design a simple portfolio homepage"
        ],
        "intermediate": [
            "Build a multi-page website with routing",
            "Implement dark/light mode toggle",
            "Create a small React app"
        ],
        "advanced": [
            "Build a full frontend dashboard",
            "Implement complex state management",
            "Optimize performance for large datasets"
        ]
    },

    "backend": {
        "beginner": [
            "Create a simple REST API",
            "Connect Flask to SQLite",
            "Build CRUD operations"
        ],
        "intermediate": [
            "Implement authentication system",
            "Design relational database schema",
            "Build role-based access control"
        ],
        "advanced": [
            "Design scalable microservices",
            "Implement caching layer",
            "Optimize database queries"
        ]
    },

    "ai": {
        "beginner": [
            "Build a simple ML model",
            "Train a classifier using scikit-learn",
            "Visualize dataset insights"
        ],
        "intermediate": [
            "Create a prediction API",
            "Fine-tune a pre-trained model",
            "Implement NLP text analyzer"
        ],
        "advanced": [
            "Deploy ML model to production",
            "Build recommendation system",
            "Optimize model performance"
        ]
    },

    "devops": {
        "beginner": [
            "Write a Dockerfile",
            "Containerize a Flask app",
            "Deploy to local server"
        ],
        "intermediate": [
            "Set up CI/CD pipeline",
            "Deploy to cloud VM",
            "Configure reverse proxy"
        ],
        "advanced": [
            "Design Kubernetes deployment",
            "Implement monitoring system",
            "Automate infrastructure provisioning"
        ]
    }
}


def generate_missions(track, level):
    """
    Generates 3 AI-style missions based on track and difficulty.
    """

    level_type = "beginner"

    if level >= 5:
        level_type = "intermediate"

    if level >= 10:
        level_type = "advanced"

    mission_list = MISSIONS.get(track, {}).get(level_type, [])

    selected = random.sample(mission_list, min(3, len(mission_list)))

    return selected