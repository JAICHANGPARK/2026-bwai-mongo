"""ADK agent that calls hosted Gemma 4 through the Gemini API.

Run:
    cd hands-on/session-1/reference
    uv run adk run adk_02_gemini_api_gemma4_agent
"""

from __future__ import annotations

import os
from pathlib import Path


DEFAULT_MODEL = "gemma-4-31b-it"


def load_env() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        return

    # ADK runs from the package, so explicitly load reference/.env as well.
    load_dotenv(Path(__file__).resolve().parents[1] / ".env")
    load_dotenv()


def choose_model() -> str:
    # ADK-specific env wins, then the general Gemini env, then the reference default.
    return (
        os.getenv("ADK_GEMINI_MODEL")
        or os.getenv("GEMINI_MODEL")
        or DEFAULT_MODEL
    )


def get_weather(location: str) -> str:
    """Return a tiny fake weather report for tool-calling practice."""
    return (
        f"Location: {location}. "
        "Weather: sunny, 76 degrees Fahrenheit, 8 mph wind."
    )


load_env()

# Keep ADK imports after load_env so the agent sees environment configuration.
from google.adk.agents import LlmAgent
from google.adk.models import Gemini


# ADK discovers this variable name when running `adk run <agent_package>`.
root_agent = LlmAgent(
    model=Gemini(model=choose_model()),
    name="adk_gemma4_weather_agent",
    instruction=(
        "You are a concise AI workshop assistant. "
        "Answer in Korean, use short examples, and keep the answer practical. "
        "Use tools when they help answer the user's request."
    ),
    tools=[get_weather],
)
