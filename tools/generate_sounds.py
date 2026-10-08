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


def make_footstep(seed: int = 31) -> list[float]:
    """Passo macio na grama: impacto abafado, contato da sola e ruído vegetal."""
    rng = random.Random(seed)
    duration = 0.205
    count = int(RATE * duration)
    lowpass = 0.0
    toe_start = .045 + rng.random() * .008
    samples = []
    for index in range(count):
        t = index / RATE
        raw = rng.uniform(-1, 1)
        lowpass += 0.075 * (raw - lowpass)
        grit = raw - lowpass
        heel = 0.0
        if t >= 0:
            heel = 0.25 * math.sin(2 * math.pi * (84 - 18 * min(1.0, t / .09)) * t) * math.exp(-31 * t)
        toe_elapsed = t - toe_start
        toe = 0.0
        if toe_elapsed >= 0:
            toe = 0.12 * math.sin(2 * math.pi * 116 * toe_elapsed) * math.exp(-36 * toe_elapsed)
        surface_env = math.exp(-20 * t) * min(1.0, t * 130)
        leafy_contact = grit * (.16 + .04 * rng.random()) * surface_env
        samples.append(heel + toe + leafy_contact)
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


def make_wood_pulse(frequency: float, duration: float, seed: int) -> list[float]:
    """Impacto curto de madeira, com ressonância e ataque de ruído filtrado."""
    rng = random.Random(seed)
    count = int(RATE * duration)
    lowpass = 0.0
    phase = 0.0
    samples = []
    for index in range(count):
        t = index / RATE
        raw = rng.uniform(-1, 1)
        lowpass += .19 * (raw - lowpass)
        phase += 2 * math.pi * (frequency - 24 * min(1.0, t / duration)) / RATE
        envelope = math.exp(-15 * t) * min(1.0, t * 150)
        resonance = .28 * math.sin(phase) + .065 * math.sin(phase * 2.31)
        attack_noise = (raw - lowpass) * .055 * math.exp(-52 * t)
        samples.append((resonance * envelope) + attack_noise)
    return samples


def make_boundary() -> list[float]:
    silence = [0.0] * int(RATE * 0.06)
    return make_wood_pulse(455, .15, 151) + silence + make_wood_pulse(325, .18, 157)


def make_slope_cue(upward: bool) -> list[float]:
    """Pista suave e ressonante; sobe em registro ou desce para indicar inclinação."""
    rng = random.Random(163 if upward else 167)
    duration = .24
    count = int(RATE * duration)
    lowpass = 0.0
    phase = 0.0
    samples = []
    start_frequency, end_frequency = (390, 610) if upward else (410, 255)
    for index in range(count):
        t = index / RATE
        progress = t / duration
        frequency = start_frequency + (end_frequency - start_frequency) * progress
        phase += 2 * math.pi * frequency / RATE
        raw = rng.uniform(-1, 1)
        lowpass += .11 * (raw - lowpass)
        filtered = raw - lowpass
        envelope = math.sin(math.pi * progress) ** 1.25
        resonance = .24 * math.sin(phase) + .055 * math.sin(phase * 1.98 + .2)
        texture = filtered * (.045 if upward else .035) * envelope
        samples.append(resonance * envelope + texture)
    return samples


def make_twig_harvest() -> list[float]:
    """Estalo seco de graveto, seguido por um breve roçar de folhas."""
    rng = random.Random(173)
    duration = .31
    count = int(RATE * duration)
    lowpass = 0.0
    samples = []
    for index in range(count):
        t = index / RATE
        raw = rng.uniform(-1, 1)
        lowpass += .12 * (raw - lowpass)
        high_noise = raw - lowpass
        first = t - .012
        second = t - .047
        snap = 0.0
        if first >= 0:
            snap += .18 * math.sin(2 * math.pi * 1280 * first) * math.exp(-95 * first)
            snap += .12 * math.sin(2 * math.pi * 510 * first) * math.exp(-55 * first)
            snap += high_noise * .22 * math.exp(-88 * first)
        if second >= 0:
            snap += .09 * math.sin(2 * math.pi * 760 * second) * math.exp(-72 * second)
            snap += high_noise * .11 * math.exp(-70 * second)
        rustle_start = max(0.0, t - .052)
        rustle_env = min(1.0, rustle_start * 42) * math.exp(-12 * rustle_start)
        rustle = high_noise * .065 * rustle_env
        samples.append(snap + rustle)
    return samples


def make_branch_step(seed: int = 181) -> list[float]:
    """Passo leve sobre madeira, distinto do contato abafado com a grama."""
    rng = random.Random(seed)
    duration = .22
    count = int(RATE * duration)
    lowpass = 0.0
    phase = 0.0
    samples = []
    for index in range(count):
        t = index / RATE
        raw = rng.uniform(-1, 1)
        lowpass += .16 * (raw - lowpass)
        grain = raw - lowpass
        hit = 0.0
        for start, frequency, strength in ((.004, 112, .22), (.058, 168, .1)):
            elapsed = t - start
            if elapsed >= 0:
                hit += strength * math.sin(2 * math.pi * frequency * elapsed) * math.exp(-34 * elapsed)
        progress = t / duration
        frequency = 188 - 48 * progress
        phase += 2 * math.pi * frequency / RATE
        creak = .045 * math.sin(phase) * math.sin(math.pi * progress) ** 1.2
        contact = grain * .035 * math.exp(-17 * t)
        samples.append(hit + creak + contact)
    return samples


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
    for variant, seed in enumerate((31, 47, 53, 59), start=1):
        filename = "footstep.wav" if variant == 1 else f"footstep-{variant}.wav"
        write_wav(ASSETS / filename, make_footstep(seed))
    write_wav(ASSETS / "slope-up.wav", make_slope_cue(upward=True))
    write_wav(ASSETS / "slope-down.wav", make_slope_cue(upward=False))
    write_wav(ASSETS / "boundary.wav", make_boundary())
    for variant, seed in enumerate((181, 193, 197), start=1):
        filename = "branch-step.wav" if variant == 1 else f"branch-step-{variant}.wav"
        write_wav(ASSETS / filename, make_branch_step(seed))
    write_wav(ASSETS / "twig-harvest.wav", make_twig_harvest())
    # Os efeitos de escalada já aprovados permanecem sem alteração.
    write_wav(ASSETS / "climb-grip.wav", make_grip())
    write_wav(ASSETS / "climb-up.wav", make_climb_step(upward=True))
    write_wav(ASSETS / "climb-down.wav", make_climb_step(upward=False))
    write_wav(ASSETS / "climb-settle.wav", make_branch_settle())
    write_wav(ASSETS / "climb-release.wav", make_release())
    print("Sons WAV gerados em:", ASSETS)


if __name__ == "__main__":
    main()
