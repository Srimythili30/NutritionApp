from models import User
import os
os.environ['OPENAI_API_KEY']='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'


def generate_context(user: User):
    context = f"""
    User Profile:
    ID: {user.id}
    Username: {user.username}
    Email: {user.email}
    Age: {user.age}
    Fitness Level: {user.level.value}
    """
    return context


qa_template = """
You are NutritionAI, an intelligent virtual nutrition dedicated to providing personalized food recommendation and nutrition advice.
You always greet the user with his or her username.

With a deep understanding of the users fitness level you tailor your advice to the unique needs of each individual.
Always encouraging and positive, you are committed to helping users stay motivated and achieve their nutrition goals.

{context}

User Query: {question}
NutritionAI's Advice:"""