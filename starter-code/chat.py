"""
💬 Vinpearl Hotel Review Response Assistant — Interactive Chat
Trò chuyện trực tiếp với chatbot Vinpearl để demo hoặc test boundary.

Cách chạy:
    cd starter-code
    python chat.py
"""

import os
import sys

# Import SYSTEM_PROMPT và GEMINI_MODEL từ prompt_prototype.py
from prompt_prototype import SYSTEM_PROMPT, GEMINI_MODEL


def main():
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("\033[91m[Error] GEMINI_API_KEY chưa được set.\033[0m")
        sys.exit(1)

    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)
    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        temperature=0.0,
    )

    # Dùng Chat API thay vì generate_content trực tiếp
    chat = client.chats.create(model=GEMINI_MODEL, config=config)

    print("\033[94m" + "=" * 55)
    print("🏨 Vinpearl Hotel Review Response Assistant")
    print("   Powered by Vin Smart Future × Gemini 2.5 Flash")
    print("=" * 55 + "\033[0m")
    print()
    print("\033[90mNhập review của khách hoặc yêu cầu soạn reply.")
    print("Gõ 'quit' hoặc 'exit' để thoát.\033[0m")
    print()

    while True:
        try:
            user_input = input("\033[93m🧑 Bạn: \033[0m").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\033[90m👋 Tạm biệt!\033[0m")
            break

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            print("\033[90m👋 Tạm biệt!\033[0m")
            break

        try:
            print()
            print("\033[92m🤖 Assistant:\033[0m")

            # Streaming response
            full_response = ""
            for chunk in chat.send_message_stream(user_input):
                text = chunk.text or ""
                print(text, end="", flush=True)
                full_response += text

            print("\n")

            # Verification checks
            if "[DRAFT_ONLY]" not in full_response:
                print("\033[91m⚠️  CẢNH BÁO: Response thiếu tag [DRAFT_ONLY]!\033[0m\n")
            if "escalate_to_manager" in full_response.lower():
                print("\033[91m🚨 ESCALATION detected — cần chuyển cho Manager!\033[0m\n")

        except Exception as e:
            print(f"\n\033[91m❌ Lỗi: {e}\033[0m\n")


if __name__ == "__main__":
    main()
