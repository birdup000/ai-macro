import eel
import pyautogui
import time
from agixtsdk import AGiXTSDK, ChatCompletions

# Initialize AGiXT SDK
agxt = AGiXTSDK(base_uri="http://localhost:7437", api_key="YOUR_AGIXT_API_KEY")

# Initialize Eel and serve web files
eel.init("web")

# Expose functions to Javascript
@eel.expose
async def generate_text(prompt):
    chat_completion = ChatCompletions(
        model="YOUR_AGENT_NAME",  # Replace with your agent name
        messages=[
            {"role": "user", "content": prompt},
        ],
    )

    response = await agxt.chat_completions(
        prompt=chat_completion,
        async_func=lambda x: agxt.instruct(
            agent_name="YOUR_AGENT_NAME",  # Replace with your agent name
            user_input=x,
            conversation="-",
        ),
    )

    return response["choices"][0]["message"]["content"]

@eel.expose
def perform_game_action(action):
    if action == "jump":
        pyautogui.press("space")
    elif action == "move_left":
        pyautogui.keyDown("left")
        time.sleep(0.5)
        pyautogui.keyUp("left")
    # Add more game actions here

# Start Eel web server
eel.start("index.html", size=(800, 600))