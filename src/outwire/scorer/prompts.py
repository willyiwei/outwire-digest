from pathlib import Path

_PROMPTS_DIR = Path(__file__).parents[3] / "prompts"


def load_scoring_prompt() -> str:
    return (_PROMPTS_DIR / "scoring_system.md").read_text()


def load_editorial_prompt() -> str:
    return (_PROMPTS_DIR / "editorial_system.md").read_text()
