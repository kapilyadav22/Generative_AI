import sys
from IPython.display import display, Markdown

def get_text(content) -> str:
    """Safely extracts text content whether payload is a string or a list of dicts."""
    if isinstance(content, str):
        return content
    elif isinstance(content, list):
        return "".join(
            part.get("text", "") if isinstance(part, dict) and part.get("type") == "text"
            else str(part) for part in content
        )
    return str(content)

def print_md(content):
    """Renders LLM response or markdown string beautifully in Jupyter Notebooks."""
    text = get_text(content)
    display(Markdown(text))
