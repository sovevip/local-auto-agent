"""Hello Skill — demo skill that adds a greeting tool."""
import json

def say_hello(name: str = "World") -> str:
    """
    Say hello to someone.

    Args:
        name: 要问候的人名

    Returns:
        {"ok": true, "data": "Hello, xxx!"}
    """
    return json.dumps({"ok": True, "data": f"Hello, {name}!", "error": None}, ensure_ascii=False)
