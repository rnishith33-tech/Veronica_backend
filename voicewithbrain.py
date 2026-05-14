# =========================================================
# voicewithbrain.py
# VERONICA BRAIN (WEB VERSION)
# =========================================================

# Import your AI brain
from brain import ask_veronica

# =========================================================
# MAIN FUNCTION FOR WEB
# =========================================================

def process_command(user_input):
    """
    This function is called by Flask backend
    It replaces input() and speak()
    """

    try:
        user = user_input.strip()

        if not user:
            return "Please say something."

        # Exit commands
        if user.lower() in [
            "exit",
            "shutdown",
            "stop",
            "goodbye"
        ]:
            return "Shutting down systems. Goodbye Boss."

        # Ask Veronica brain
        answer = ask_veronica(user)

        return answer

    except Exception as e:
        return f"Error: {str(e)}"
