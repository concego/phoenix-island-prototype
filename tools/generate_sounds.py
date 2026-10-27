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


FOOTSTEP_PROFILES: tuple[dict[str, float], ...] = (
    # Compacto e macio: impacto baixo, pouco arrasto de folhas.
    {"duration": .19, "heel": .25, "heel_start": 76, "heel_end": 54, "heel_decay": 32,
     "toe_delay": .035, "toe": .08, "toe_hz": 100, "toe_decay": 42,
     "leaf": .12, "lowpass": .07, "surface_decay": 25, "surface_attack": 130,
     "scuff": 0, "scuff_delay": .07, "scuff_decay": 26},
    # Mais firme, com contato de ponta mais agudo e uma pequena escovada.
    {"duration": .215, "heel": .34, "heel_start": 96, "heel_end": 70, "heel_decay": 27,
     "toe_delay": .055, "toe": .13, "toe_hz": 136, "toe_decay": 32,
     "leaf": .24, "lowpass": .13, "surface_decay": 20, "surface_attack": 170,
     "scuff": .045, "scuff_delay": .085, "scuff_decay": 30},
    # Mais leve e rápido, com ruído vegetal mais nítido.
    {"duration": .20, "heel": .20, "heel_start": 108, "heel_end": 80, "heel_decay": 40,
     "toe_delay": .03, "toe": .15, "toe_hz": 152, "toe_decay": 45,
     "leaf": .30, "lowpass": .055, "surface_decay": 29, "surface_attack": 145,
     "scuff": .12, "scuff_delay": .065, "scuff_decay": 24},
    # Apoio mais pesado e abafado, seguido de arrasto curto na grama.
    {"duration": .235, "heel": .32, "heel_start": 68, "heel_end": 48, "heel_decay": 24,
     "toe_delay": .075, "toe": .10, "toe_hz": 88, "toe_decay": 31,
     "leaf": .19, "lowpass": .17, "surface_decay": 17, "surface_attack": 110,
     "scuff": .18, "scuff_delay": .09, "scuff_decay": 18},
)

WATER_STEP_PROFILES: tuple[dict[str, object], ...] = (
    {"duration": .22, "impact_hz": 82, "impact_level": .18, "impact_decay": 35,
     "lowpass": .20, "splashes": ((.003, .27, 32), (.065, .075, 48)),
     "bubble_delay": .035, "bubble_hz": 190, "bubble_level": .11, "bubble_decay": 24,
     "foam_mix": .20},
    {"duration": .235, "impact_hz": 96, "impact_level": .21, "impact_decay": 31,
     "lowpass": .15, "splashes": ((.004, .22, 28), (.035, .13, 38), (.095, .065, 52)),
     "bubble_delay": .06, "bubble_hz": 245, "bubble_level": .085, "bubble_decay": 27,
     "foam_mix": .14},
    {"duration": .215, "impact_hz": 72, "impact_level": .24, "impact_decay": 29,
     "lowpass": .25, "splashes": ((.006, .20, 35), (.078, .11, 35)),
     "bubble_delay": .025, "bubble_hz": 158, "bubble_level": .13, "bubble_decay": 21,
     "foam_mix": .28},
    {"duration": .23, "impact_hz": 108, "impact_level": .16, "impact_decay": 39,
     "lowpass": .12, "splashes": ((.003, .31, 34), (.052, .085, 58)),
     "bubble_delay": .075, "bubble_hz": 285, "bubble_level": .075, "bubble_decay": 30,
     "foam_mix": .12},
)

MUD_STEP_PROFILES: tuple[dict[str, float], ...] = (
    {"duration": .235, "impact_hz": 74, "impact": .19, "squelch": .23, "pull_delay": .075, "pull": .18, "filter": .18},
    {"duration": .25, "impact_hz": 88, "impact": .16, "squelch": .28, "pull_delay": .09, "pull": .14, "filter": .14},
    {"duration": .22, "impact_hz": 66, "impact": .23, "squelch": .18, "pull_delay": .055, "pull": .22, "filter": .23},
    {"duration": .245, "impact_hz": 98, "impact": .14, "squelch": .21, "pull_delay": .11, "pull": .19, "filter": .12},
)

SWIM_SURFACE_PROFILES: tuple[dict[str, object], ...] = (
    {"duration": .28, "impact_hz": 112, "impact": .18, "filter": .12,
     "splashes": ((.002, .29, 24), (.105, .09, 33)), "ripple": .055},
    {"duration": .30, "impact_hz": 95, "impact": .22, "filter": .18,
     "splashes": ((.006, .20, 25), (.055, .14, 30), (.15, .07, 38)), "ripple": .045},
    {"duration": .26, "impact_hz": 128, "impact": .14, "filter": .10,
     "splashes": ((.003, .32, 29), (.09, .12, 40)), "ripple": .065},
    {"duration": .29, "impact_hz": 82, "impact": .20, "filter": .22,
     "splashes": ((.004, .24, 22), (.08, .10, 46), (.17, .06, 42)), "ripple": .05},
)

SWIM_UNDERWATER_PROFILES: tuple[dict[str, object], ...] = (
    {"duration": .30, "filter": .26, "bubbles": ((.005, 148, .18, 21), (.105, 226, .11, 24))},
    {"duration": .32, "filter": .20, "bubbles": ((.008, 198, .15, 24), (.085, 278, .12, 27), (.17, 164, .07, 28))},
    {"duration": .29, "filter": .32, "bubbles": ((.004, 122, .20, 20), (.12, 188, .13, 22))},
    {"duration": .31, "filter": .23, "bubbles": ((.01, 242, .13, 28), (.105, 174, .15, 22), (.2, 296, .065, 32))},
)


def make_footstep(seed: int = 31, profile: dict[str, float] | None = None) -> list[float]:
    """Gera passos de grama com timbres e articulações distinguíveis, mas coerentes."""
    rng = random.Random(seed)
    profile = profile or FOOTSTEP_PROFILES[0]
    count = int(RATE * profile["duration"])
    lowpass = 0.0
    toe_start = profile["toe_delay"] + rng.uniform(-.004, .004)
    samples = []
    for index in range(count):
        t = index / RATE
        raw = rng.uniform(-1, 1)
        lowpass += profile["lowpass"] * (raw - lowpass)
        grit = raw - lowpass
        heel_progress = min(1.0, t / .09)
        heel_hz = profile["heel_start"] + (profile["heel_end"] - profile["heel_start"]) * heel_progress
        heel = profile["heel"] * math.sin(2 * math.pi * heel_hz * t) * math.exp(-profile["heel_decay"] * t)
        toe_elapsed = t - toe_start
        toe = 0.0
        if toe_elapsed >= 0:
            toe = profile["toe"] * math.sin(2 * math.pi * profile["toe_hz"] * toe_elapsed) * math.exp(-profile["toe_decay"] * toe_elapsed)
        surface_env = math.exp(-profile["surface_decay"] * t) * min(1.0, t * profile["surface_attack"])
        leafy_contact = grit * (profile["leaf"] + .04 * rng.random()) * surface_env
        scuff_elapsed = t - profile["scuff_delay"]
        scuff = 0.0
        if profile["scuff"] and scuff_elapsed >= 0:
            scuff_env = math.exp(-profile["scuff_decay"] * scuff_elapsed) * min(1.0, scuff_elapsed * 90)
            scuff = grit * profile["scuff"] * scuff_env
        samples.append(heel + toe + leafy_contact + scuff)
    rms = math.sqrt(sum(sample * sample for sample in samples) / len(samples))
    if rms:
        level_match = .064 / rms
        samples = [sample * level_match for sample in samples]
    return samples


def make_water_step(seed: int = 211, profile: dict[str, object] | None = None) -> list[float]:
    """Gera um passo curto de água rasa, com impacto molhado, respingo e pequeno redemoinho."""
    rng = random.Random(seed)
    profile = profile or WATER_STEP_PROFILES[0]
    duration = float(profile["duration"])
    count = int(RATE * duration)
    lowpass = 0.0
    samples = []
    for index in range(count):
        t = index / RATE
        raw = rng.uniform(-1, 1)
        lowpass += float(profile["lowpass"]) * (raw - lowpass)
        splash_noise = raw - lowpass

        impact_elapsed = t - .006
        impact = 0.0
        if impact_elapsed >= 0:
            frequency = float(profile["impact_hz"]) - 22 * min(1.0, impact_elapsed / .055)
            envelope = math.exp(-float(profile["impact_decay"]) * impact_elapsed)
            impact = float(profile["impact_level"]) * (
                math.sin(2 * math.pi * frequency * impact_elapsed)
                + .16 * math.sin(2 * math.pi * frequency * 2.13 * impact_elapsed)
            ) * envelope

        splash = 0.0
        for start, level, decay in profile["splashes"]:
            elapsed = t - float(start)
            if elapsed >= 0:
                envelope = math.exp(float(-decay) * elapsed) * min(1.0, elapsed * 130)
                wet_noise = splash_noise + float(profile["foam_mix"]) * lowpass
                splash += float(level) * wet_noise * envelope

        bubble_elapsed = t - float(profile["bubble_delay"])
        bubble = 0.0
        if bubble_elapsed >= 0:
            frequency = float(profile["bubble_hz"]) + 75 * min(1.0, bubble_elapsed / .12)
            envelope = math.exp(-float(profile["bubble_decay"]) * bubble_elapsed) * min(1.0, bubble_elapsed * 100)
            bubble = float(profile["bubble_level"]) * math.sin(2 * math.pi * frequency * bubble_elapsed) * envelope

        ripple_elapsed = t - .045
        ripple = 0.0
        if ripple_elapsed >= 0:
            ripple_env = math.exp(-21 * ripple_elapsed) * min(1.0, ripple_elapsed * 55)
            ripple = (.035 * splash_noise + .045 * lowpass) * ripple_env
        samples.append(impact + splash + bubble + ripple)

    rms = math.sqrt(sum(sample * sample for sample in samples) / len(samples))
    if rms:
        level_match = .058 / rms
        samples = [sample * level_match for sample in samples]
    return samples


def make_mud_step(seed: int = 251, profile: dict[str, float] | None = None) -> list[float]:
    """Passo curto e abafado na lama, com compressão úmida e pequena sucção ao retirar o pé."""
    rng = random.Random(seed)
    profile = profile or MUD_STEP_PROFILES[0]
    duration = profile["duration"]
    count = int(RATE * duration)
    lowpass = 0.0
    samples = []
    for index in range(count):
        t = index / RATE
        raw = rng.uniform(-1, 1)
        lowpass += profile["filter"] * (raw - lowpass)
        grit = raw - lowpass
        impact_elapsed = t - .004
        impact = 0.0
        if impact_elapsed >= 0:
            impact = profile["impact"] * math.sin(2 * math.pi * profile["impact_hz"] * impact_elapsed) * math.exp(-34 * impact_elapsed)
        squelch = 0.0
        if t >= 0:
            envelope = math.exp(-23 * t) * min(1.0, t * 110)
            squelch = (grit + .28 * lowpass) * profile["squelch"] * envelope
        pull_elapsed = t - profile["pull_delay"]
        pull = 0.0
        if pull_elapsed >= 0:
            envelope = math.exp(-29 * pull_elapsed) * min(1.0, pull_elapsed * 100)
            suction = math.sin(2 * math.pi * (58 - 20 * min(1.0, pull_elapsed / .12)) * pull_elapsed)
            pull = profile["pull"] * (suction + .22 * grit) * envelope
        samples.append(impact + squelch + pull)
    rms = math.sqrt(sum(sample * sample for sample in samples) / len(samples))
    if rms:
        samples = [sample * (.057 / rms) for sample in samples]
    return samples


def make_swim_stroke(seed: int, profile: dict[str, object], submerged: bool = False) -> list[float]:
    """Braçada curta; acima da água respinga, abaixo dela produz bolhas abafadas."""
    rng = random.Random(seed)
    duration = float(profile["duration"])
    count = int(RATE * duration)
    lowpass = 0.0
    samples = []
    for index in range(count):
        t = index / RATE
        raw = rng.uniform(-1, 1)
        lowpass += float(profile["filter"]) * (raw - lowpass)
        noise = raw - lowpass
        sound = 0.0
        if submerged:
            for start, frequency, strength, decay in profile["bubbles"]:
                elapsed = t - float(start)
                if elapsed >= 0:
                    envelope = math.exp(-float(decay) * elapsed) * min(1.0, elapsed * 95)
                    wobble = math.sin(2 * math.pi * float(frequency) * elapsed)
                    sound += float(strength) * (wobble + .20 * math.sin(2 * math.pi * float(frequency) * 1.72 * elapsed)) * envelope
                    sound += noise * float(strength) * .12 * envelope
        else:
            impact_elapsed = t - .006
            if impact_elapsed >= 0:
                sound += float(profile["impact"]) * math.sin(2 * math.pi * float(profile["impact_hz"]) * impact_elapsed) * math.exp(-28 * impact_elapsed)
            for start, level, decay in profile["splashes"]:
                elapsed = t - float(start)
                if elapsed >= 0:
                    envelope = math.exp(-float(decay) * elapsed) * min(1.0, elapsed * 105)
                    sound += float(level) * (noise + .18 * lowpass) * envelope
            ripple_elapsed = t - .055
            if ripple_elapsed >= 0:
                sound += float(profile["ripple"]) * (noise + .35 * lowpass) * math.exp(-19 * ripple_elapsed) * min(1.0, ripple_elapsed * 50)
        samples.append(sound)
    target_rms = .048 if submerged else .056
    rms = math.sqrt(sum(sample * sample for sample in samples) / len(samples))
    if rms:
        samples = [sample * (target_rms / rms) for sample in samples]
    return samples


def make_swim_transition(entering: bool) -> list[float]:
    """Confirmação de entrada/saída da natação, com respingo de volume controlado."""
    rng = random.Random(271 if entering else 277)
    duration = .29 if entering else .22
    count = int(RATE * duration)
    lowpass = 0.0
    samples = []
    pulses = ((.004, .28, 25), (.09, .09, 38)) if entering else ((.005, .18, 31), (.10, .055, 45))
    for index in range(count):
        t = index / RATE
        raw = rng.uniform(-1, 1)
        lowpass += .16 * (raw - lowpass)
        noise = raw - lowpass
        impact_elapsed = t - .005
        impact = .16 * math.sin(2 * math.pi * (102 if entering else 84) * impact_elapsed) * math.exp(-26 * impact_elapsed) if impact_elapsed >= 0 else 0.0
        splash = 0.0
        for start, level, decay in pulses:
            elapsed = t - start
            if elapsed >= 0:
                splash += level * (noise + .16 * lowpass) * math.exp(-decay * elapsed) * min(1.0, elapsed * 100)
        samples.append(impact + splash)
    rms = math.sqrt(sum(sample * sample for sample in samples) / len(samples))
    if rms:
        samples = [sample * (.055 / rms) for sample in samples]
    return samples


def make_swim_guide(upward: bool) -> list[float]:
    """Dois bipes simples em sequência ascendente ou descendente para orientação vertical."""
    frequencies = (470, 760) if upward else (760, 470)
    pulse_duration = .075
    gap = .035
    total = pulse_duration * 2 + gap
    samples = [0.0] * int(RATE * total)
    for pulse, frequency in enumerate(frequencies):
        start = pulse * (pulse_duration + gap)
        start_index = int(start * RATE)
        pulse_count = int(pulse_duration * RATE)
        for offset in range(pulse_count):
            t = offset / RATE
            attack = min(1.0, t / .008)
            release = min(1.0, (pulse_duration - t) / .018)
            envelope = max(0.0, min(attack, release))
            tone = math.sin(2 * math.pi * frequency * t) + .12 * math.sin(4 * math.pi * frequency * t)
            samples[start_index + offset] = .20 * tone * envelope
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
    """Confirmação curta em dois impactos, para não invadir o passo seguinte."""
    silence = [0.0] * int(RATE * 0.025)
    return make_wood_pulse(455, .045, 151) + silence + make_wood_pulse(325, .055, 157)


def make_slope_cue(upward: bool) -> list[float]:
    """Pista suave e ressonante; sobe em registro ou desce para indicar inclinação."""
    rng = random.Random(163 if upward else 167)
    duration = .11
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
    for variant, (seed, profile) in enumerate(zip((31, 47, 53, 59), FOOTSTEP_PROFILES), start=1):
        filename = "footstep.wav" if variant == 1 else f"footstep-{variant}.wav"
        write_wav(ASSETS / filename, make_footstep(seed, profile))
    for variant, (seed, profile) in enumerate(zip((211, 223, 227, 229), WATER_STEP_PROFILES), start=1):
        filename = "water-step.wav" if variant == 1 else f"water-step-{variant}.wav"
        write_wav(ASSETS / filename, make_water_step(seed, profile))
    for variant, (seed, profile) in enumerate(zip((251, 257, 263, 269), MUD_STEP_PROFILES), start=1):
        filename = "mud-step.wav" if variant == 1 else f"mud-step-{variant}.wav"
        write_wav(ASSETS / filename, make_mud_step(seed, profile))
    for variant, (seed, profile) in enumerate(zip((281, 283, 293, 307), SWIM_SURFACE_PROFILES), start=1):
        filename = "swim-surface.wav" if variant == 1 else f"swim-surface-{variant}.wav"
        write_wav(ASSETS / filename, make_swim_stroke(seed, profile))
    for variant, (seed, profile) in enumerate(zip((311, 313, 317, 331), SWIM_UNDERWATER_PROFILES), start=1):
        filename = "swim-underwater.wav" if variant == 1 else f"swim-underwater-{variant}.wav"
        write_wav(ASSETS / filename, make_swim_stroke(seed, profile, submerged=True))
    write_wav(ASSETS / "swim-enter.wav", make_swim_transition(entering=True))
    write_wav(ASSETS / "swim-exit.wav", make_swim_transition(entering=False))
    write_wav(ASSETS / "swim-guide-up.wav", make_swim_guide(upward=True))
    write_wav(ASSETS / "swim-guide-down.wav", make_swim_guide(upward=False))
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




def make_resource_locator(kind: str, seed: int) -> list[float]:
    """Gera uma pista mono curta e identificável para espacialização no jogo."""
    rng = random.Random(seed)
    duration = .24
    count = int(RATE * duration)
    low = 0.0
    samples = []
    for index in range(count):
        t = index / RATE
        noise = rng.uniform(-1, 1)
        low += .13 * (noise - low)
        high = noise - low
        def env(start: float, decay: float, attack: float = .004) -> float:
            elapsed = t - start
            if elapsed < 0:
                return 0.0
            return min(1.0, elapsed / attack) * math.exp(-decay * elapsed)
        value = 0.0
        if kind == 'collectible':
            # Clear pair of bright, rising glass/stone-like notes: object can be picked up as-is.
            value += .16 * math.sin(2 * math.pi * (760 + 360*t) * t) * env(.008, 17, .003)
            value += .14 * math.sin(2 * math.pi * (1040 + 260*t) * (t-.105)) * env(.105, 19, .003)
            value += .055 * high * env(.006, 75, .001)
        elif kind == 'extractable':
            # Lower, rougher double thump: source needs a tool or repeated extraction action.
            value += .17 * math.sin(2 * math.pi * (190 - 42*t) * t) * env(.006, 15, .002)
            value += .12 * math.sin(2 * math.pi * 270 * (t-.12)) * env(.12, 17, .002)
            value += .08 * high * env(.006, 82, .001)
        samples.append(value)
    return samples


def generate_resource_location_cues() -> None:
    """Gera apenas as pistas novas, sem regravar os outros sons do protótipo."""
    ASSETS.mkdir(parents=True, exist_ok=True)
    for kind, seed in (("collectible", 101), ("extractable", 107)):
        write_wav(ASSETS / f"locate-{kind}.wav", make_resource_locator(kind, seed))


if __name__ == "__main__":
    import sys
    if "--resource-locators-only" in sys.argv:
        generate_resource_location_cues()
        print("Pistas espaciais para fontes de recurso geradas em:", ASSETS)
    else:
        main()
