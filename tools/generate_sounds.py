"""Gera sons provisórios em WAV para validar o protótipo Phoenix Island.

Uso: python3 tools/generate_sounds.py
Os arquivos são gravados em ../assets/.
"""
from __future__ import annotations

import math
import random
import struct
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
RATE = 24_000


def write_wav(path: Path, samples: list[float]) -> None:
    peak = max((abs(sample) for sample in samples), default=1.0) or 1.0
    scale = min(0.92 / peak, 1.0)
    pcm = b"".join(struct.pack("<h", int(max(-1, min(1, sample * scale)) * 32767)) for sample in samples)
    with wave.open(str(path), "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(RATE)
        output.writeframes(pcm)


def make_footstep() -> list[float]:
    rng = random.Random(31)
    duration = 0.16
    count = int(RATE * duration)
    samples = []
    for index in range(count):
        t = index / RATE
        envelope = math.exp(-25 * t) * min(1.0, t * 180)
        low_thump = math.sin(2 * math.pi * 82 * t) * 0.34
        gritty_surface = rng.uniform(-1, 1) * 0.48
        samples.append((low_thump + gritty_surface) * envelope)
    return samples


def make_beep(frequency: float, duration: float = 0.19) -> list[float]:
    count = int(RATE * duration)
    samples = []
    for index in range(count):
        t = index / RATE
        fade_in = min(1.0, t / 0.012)
        fade_out = min(1.0, (duration - t) / 0.035)
        envelope = max(0.0, min(fade_in, fade_out))
        fundamental = math.sin(2 * math.pi * frequency * t)
        harmonic = 0.12 * math.sin(2 * math.pi * frequency * 2 * t)
        samples.append((fundamental + harmonic) * envelope * 0.34)
    return samples


def make_boundary() -> list[float]:
    silence = [0.0] * int(RATE * 0.055)
    return make_beep(430, 0.11) + silence + make_beep(315, 0.14)


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    write_wav(ASSETS / "footstep.wav", make_footstep())
    write_wav(ASSETS / "slope-up.wav", make_beep(760, 0.17))
    write_wav(ASSETS / "slope-down.wav", make_beep(245, 0.2))
    write_wav(ASSETS / "boundary.wav", make_boundary())
    print("Sons WAV gerados em:", ASSETS)


if __name__ == "__main__":
    main()
