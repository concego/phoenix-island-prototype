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


def make_grip() -> list[float]:
    """Contato curto de palma na casca, com fricção seca e grave suave."""
    rng = random.Random(71)
    duration = 0.25
    count = int(RATE * duration)
    lowpass = 0.0
    samples = []
    for index in range(count):
        t = index / RATE
        raw = rng.uniform(-1, 1)
        lowpass += 0.16 * (raw - lowpass)
        scratch = raw - lowpass
        attack = min(1.0, t / 0.012)
        fade = math.exp(-17 * t)
        thud = 0.25 * math.sin(2 * math.pi * 92 * t) * math.exp(-31 * t)
        rub_gate = max(0.0, min(1.0, (t - 0.025) * 38))
        samples.append((thud + scratch * 0.16 * rub_gate * fade) * attack)
    return samples


def make_climb_step(upward: bool) -> list[float]:
    """Duas batidas abafadas e um raspado curto de mão/pé na casca."""
    rng = random.Random(83 if upward else 97)
    duration = 0.31
    count = int(RATE * duration)
    lowpass = 0.0
    samples = []
    base_freq = 112 if upward else 82
    for index in range(count):
        t = index / RATE
        raw = rng.uniform(-1, 1)
        lowpass += 0.12 * (raw - lowpass)
        scratch = raw - lowpass
        scrape_env = max(0.0, min(1.0, (t - 0.025) * 28)) * max(0.0, min(1.0, (duration - t) * 8))
        scrape = scratch * (0.13 if upward else 0.10) * scrape_env
        taps = 0.0
        for start, strength in ((0.015, 0.22), (0.155, 0.15)):
            elapsed = t - start
            if elapsed >= 0:
                frequency = base_freq - (18 if upward else 12) * min(1.0, elapsed / 0.12)
                taps += strength * math.sin(2 * math.pi * frequency * elapsed) * math.exp(-25 * elapsed)
        samples.append(scrape + taps)
    return samples


def make_branch_settle() -> list[float]:
    """Rangido de galho que cede e volta, seguido de apoio macio."""
    rng = random.Random(109)
    duration = 0.34
    count = int(RATE * duration)
    lowpass = 0.0
    phase = 0.0
    samples = []
    for index in range(count):
        t = index / RATE
        raw = rng.uniform(-1, 1)
        lowpass += 0.08 * (raw - lowpass)
        scratch = raw - lowpass
        progress = t / duration
        frequency = 155 - 72 * progress
        phase += 2 * math.pi * frequency / RATE
        creak_env = math.sin(math.pi * min(1.0, progress)) ** 1.2
        creak = 0.15 * math.sin(phase) * creak_env
        thud_elapsed = t - 0.13
        thud = 0.0
        if thud_elapsed >= 0:
            thud = 0.20 * math.sin(2 * math.pi * 76 * thud_elapsed) * math.exp(-22 * thud_elapsed)
        samples.append(creak + scratch * 0.07 * creak_env + thud)
    return samples


def make_release() -> list[float]:
    """Atrito curto de mãos se desprendendo da casca."""
    rng = random.Random(127)
    duration = 0.2
    count = int(RATE * duration)
    lowpass = 0.0
    samples = []
    for index in range(count):
        t = index / RATE
        raw = rng.uniform(-1, 1)
        lowpass += 0.13 * (raw - lowpass)
        scratch = raw - lowpass
        envelope = math.sin(math.pi * t / duration) ** 1.4
        wood_resonance = math.sin(2 * math.pi * (98 - 25 * t / duration) * t) * 0.08 * envelope
        samples.append(scratch * 0.13 * envelope + wood_resonance)
    return samples


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    write_wav(ASSETS / "footstep.wav", make_footstep())
    write_wav(ASSETS / "slope-up.wav", make_beep(760, 0.17))
    write_wav(ASSETS / "slope-down.wav", make_beep(245, 0.2))
    write_wav(ASSETS / "boundary.wav", make_boundary())
    write_wav(ASSETS / "climb-grip.wav", make_grip())
    write_wav(ASSETS / "climb-up.wav", make_climb_step(upward=True))
    write_wav(ASSETS / "climb-down.wav", make_climb_step(upward=False))
    write_wav(ASSETS / "climb-settle.wav", make_branch_settle())
    write_wav(ASSETS / "climb-release.wav", make_release())
    print("Sons WAV gerados em:", ASSETS)


if __name__ == "__main__":
    main()
