import re
import json

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

topic_ids = re.findall(r'topic\(\"([^\"]+)\",', content)
print("Found", len(topic_ids), "topics.")

# Create a master mapping for all topic resources
resources_map = {}

# We'll provide some generic resources based on the phase, and specific ones for high-priority topics.
for tid in topic_ids:
    if "python" in tid:
        resources_map[tid] = [
            {"type": "YouTube", "title": "Corey Schafer: Python Tutorials", "link": "https://youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU"},
            {"type": "Book", "title": "Python Crash Course (Ch 8-11)", "link": "https://nostarch.com/python-crash-course-3rd-edition"}
        ]
    elif "math" in tid or "linear-algebra" in tid or "calc" in tid:
        resources_map[tid] = [
            {"type": "YouTube", "title": "3Blue1Brown: Linear Algebra", "link": "https://youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab"},
            {"type": "Book", "title": "Mathematics for Machine Learning", "link": "https://mml-book.github.io/"}
        ]
    elif "sql" in tid:
        resources_map[tid] = [
            {"type": "Course", "title": "Kaggle: Intro to SQL", "link": "https://www.kaggle.com/learn/intro-to-sql"},
            {"type": "YouTube", "title": "Luke Barousse: SQL for Data Science", "link": "https://www.youtube.com/watch?v=7VixKNmSscw"}
        ]
    elif "ml" in tid or "scikit" in tid or "tree" in tid:
        resources_map[tid] = [
            {"type": "YouTube", "title": "StatQuest: Machine Learning", "link": "https://www.youtube.com/user/joshstarmer"},
            {"type": "Book", "title": "Hands-On ML (Ch 2-7)", "link": "https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/"}
        ]
    elif "dl" in tid or "pytorch" in tid or "cnn" in tid:
        resources_map[tid] = [
            {"type": "Course", "title": "fast.ai Deep Learning", "link": "https://course.fast.ai"},
            {"type": "YouTube", "title": "Andrej Karpathy: Neural Networks", "link": "https://www.youtube.com/watch?v=VMj-3S1tku0"}
        ]
    elif "llm" in tid or "rag" in tid or "transformer" in tid or "prompt" in tid:
        resources_map[tid] = [
            {"type": "Paper", "title": "Attention Is All You Need", "link": "https://arxiv.org/abs/1706.03762"},
            {"type": "YouTube", "title": "Andrej Karpathy: Let's build GPT", "link": "https://www.youtube.com/watch?v=kCc8FmEb1nY"},
            {"type": "Course", "title": "Hugging Face NLP Course", "link": "https://huggingface.co/learn/nlp-course"}
        ]
    elif "agent" in tid or "tool" in tid or "planning" in tid:
        resources_map[tid] = [
            {"type": "Documentation", "title": "LangGraph Docs", "link": "https://langchain-ai.github.io/langgraph/"},
            {"type": "Course", "title": "DeepLearning.AI: Agents", "link": "https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/"}
        ]
    elif "docker" in tid or "api" in tid or "cicd" in tid or "deploy" in tid:
        resources_map[tid] = [
            {"type": "Course", "title": "FastAPI Documentation", "link": "https://fastapi.tiangolo.com/"},
            {"type": "YouTube", "title": "TechWorld with Nana: Docker", "link": "https://www.youtube.com/watch?v=3c-iBn73dDE"}
        ]
    else:
        resources_map[tid] = [
            {"type": "YouTube", "title": "Stanford CS229 / CS231n", "link": "https://www.youtube.com/@stanfordonline"},
            {"type": "Book", "title": "Deep Learning Book", "link": "https://www.deeplearningbook.org"}
        ]

js_injection = f"""
    const allTopicResources = {json.dumps(resources_map, indent=2)};

    roadmapData.forEach(phase => {{
      phase.groups.forEach(group => {{
        group.topics.forEach(t => {{
          if (allTopicResources[t.id]) {{
            t.topicResources = allTopicResources[t.id];
          }}
        }});
      }});
    }});
"""

content = content.replace("bindEvents();\n    fullRender();", f"{js_injection}\n    bindEvents();\n    fullRender();")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Injected resources successfully.")
