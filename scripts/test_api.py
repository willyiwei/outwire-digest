import os
import traceback
import anthropic

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
try:
    msg = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=10,
        messages=[{"role": "user", "content": "hi"}],
    )
    print("SDK OK:", msg.content[0].text)
except Exception:
    traceback.print_exc()
