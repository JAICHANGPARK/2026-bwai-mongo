"""Hosted Gemma 4 hands-on with the Gemini API.

Run:
    cd hands-on/session-1/reference
    uv run python 01_gemini_api_gemma4.py
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


DEFAULT_MODEL = "gemma-4-26b-a4b-it"
DEFAULT_SYSTEM = (
    "You are a concise AI workshop assistant. "
    "Answer in Korean, use short examples, and keep the answer practical."
)
DEFAULT_PROMPT = (
    "Gemma 4를 Gemini API로 쓰는 장점과 로컬 Ollama로 쓰는 장점을 "
    "각각 2개씩 비교해 주세요."
)


def load_env() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        return

    # Load a script-local .env first, then allow the current shell/project env.
    load_dotenv(Path(__file__).with_name(".env"))
    load_dotenv()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Call hosted Gemma 4 through the Gemini API."
    )
    parser.add_argument(
        "--model",
        default=os.getenv("GEMINI_MODEL", DEFAULT_MODEL),
        help=f"Gemini API model name. Default: {DEFAULT_MODEL}",
    )
    parser.add_argument(
        "--prompt",
        default=DEFAULT_PROMPT,
        help="Prompt to send to Gemma 4.",
    )
    parser.add_argument(
        "--system",
        default=DEFAULT_SYSTEM,
        help="System instruction for the model.",
    )
    parser.add_argument(
        "--thinking",
        action="store_true",
        help='Enable Gemma thinking with thinking_level="high".',
    )
    return parser.parse_args()


def build_config(args: argparse.Namespace):
    # Import google-genai only when we are about to call the API.
    # This keeps `--help` usable before dependencies are installed.
    from google.genai import types

    thinking_config = (
        types.ThinkingConfig(thinking_level="high") if args.thinking else None
    )

    return types.GenerateContentConfig(
        system_instruction=args.system,
        thinking_config=thinking_config,
    )


def main() -> int:
    load_env()
    args = parse_args()

    # Stop before importing or calling the SDK if no API key is configured.
    if not (os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")):
        print(
            "GEMINI_API_KEY 또는 GOOGLE_API_KEY 환경 변수를 먼저 설정해 주세요.\n"
            "예: hands-on/session-1/reference/.env 파일에 GEMINI_API_KEY=YOUR_API_KEY",
            file=sys.stderr,
        )
        return 2

    from google import genai

    client = genai.Client()
    # generate_content sends the prompt and optional system/thinking settings.
    response = client.models.generate_content(
        model=args.model,
        contents=args.prompt,
        config=build_config(args),
    )

    print(f"\n[model] {args.model}")
    print(f"[prompt] {args.prompt}\n")
    print(response.text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
