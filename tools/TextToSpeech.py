from __future__ import annotations
from pathlib import Path
from typing import TYPE_CHECKING
from openai import OpenAI
from pydub import AudioSegment
audio = AudioSegment.from_file("my_audio.mp3", format="mp3")


client = OpenAI()
speech_file_path = Path(__file__).parent / "speech.mp3"

with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="coral",
    input="Today is a wonderful day to build something people love!",
    instructions="Speak in a cheerful and positive tone.",
) as response:
    response.stream_to_file(speech_file_path)
{
                    "type": "function",
                    "function": {
                        "name": "text_to_speech",
                        "description": "Convert text to speech",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "text": {"type": "string"},
                                "voice": {"type": "string"},
                                "response_format": {"type": "string"}
                            },
                            "required": ["text", "voice", "response_format"]
                        }
                    }
                }
with client.chat.completions.create(   
    model="gpt-4o-mini",
    voice="coral",
    input="Today is a wonderful day to build something people love!",
    instructions="Speak in a cheerful and positive tone.",
    response_format="pcm",
) as response:
    audio = AudioSegment.from_file().play(response)
# Now you can print/use response
# ...existing code...
class LocalAudioPlayer:
    def __init__(self):
        pass
    def play(self, data: bytes):
        # implement playback
        ...
# ...existing code... 

if TYPE_CHECKING:
    def synthesize(player: LocalAudioPlayer): [[str], [None]]
    async def speak(text: str) -> None:
            # implement synthesis logic
        async def main():
            await LocalAudioPlayer().play(response)
            await synthesize.speak(text)

if __name__ == "__main__":
    import asyncio
    asyncio.run(())
print("Chat:", response.choices[0].message.content)
messages.append({"role": "assistant", "content": response.choices[0].message.content})