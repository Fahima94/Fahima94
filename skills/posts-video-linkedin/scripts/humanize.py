#!/usr/bin/env python3
"""Humanizer FR : nettoie un texte et le note sur 5 contrôles (0-100).

Usage : python3 humanize.py texte.txt   (ou texte sur l'entrée standard)
Écrit le texte nettoyé puis le rapport de score.
"""
import json
import re
import statistics
import sys
from pathlib import Path

SLOP = json.loads((Path(__file__).parent.parent / "references" / "slop-fr.json").read_text(encoding="utf-8"))
INVISIBLES = re.compile("[​‌‍⁠﻿­]")
TYPO = {"—": ",", "–": "-", "“": '"', "”": '"', "‘": "'", "’": "'", "…": "..."}


def clean(text: str) -> tuple[str, int]:
    fixes = len(INVISIBLES.findall(text))
    text = INVISIBLES.sub("", text)
    for bad, good in TYPO.items():
        fixes += text.count(bad)
        text = text.replace(bad, good)
    for bad, good in SLOP["replace"].items():
        pattern = re.compile(re.escape(bad), re.IGNORECASE)
        fixes += len(pattern.findall(text))
        text = pattern.sub(good, text)
    text = re.sub(r" {2,}", " ", text)
    text = re.sub(r" ,", ",", text)
    text = re.sub(r"(^|[.!?]\s+|\n)([a-zàâéèêîôûç])", lambda m: m.group(1) + m.group(2).upper(), text.strip())
    return text, fixes


def sentences(text: str) -> list[str]:
    return [s for s in re.split(r"(?<=[.!?])\s+|\n+", text) if len(s.split()) > 0]


def score(original: str, text: str) -> dict:
    words = max(len(text.split()), 1)
    lengths = [len(s.split()) for s in sentences(text)]
    burst = statistics.pstdev(lengths) / max(statistics.mean(lengths), 1) if len(lengths) > 1 else 0
    specifics = len(re.findall(r"\d+|\b[A-ZÉÈ][a-zéèêàç]+\b", text)) / words * 100
    slop_left = sum(len(re.findall(re.escape(k), text, re.I)) for k in SLOP["replace"]) / words * 100
    fingerprint = (len(INVISIBLES.findall(original)) + sum(original.count(c) for c in TYPO)) / words * 100
    voice = len(re.findall(r"\b(je|j'|tu|t'|on|moi|toi)\b", text, re.I)) / words * 100
    checks = {
        "BURSTINESS (variété des phrases)": min(100, burst * 160),
        "SPECIFICITY (détails concrets)": min(100, specifics * 12),
        "SLOP DENSITY (tournures toutes faites)": max(0, 100 - slop_left * 50),
        "FINGERPRINT (traces typographiques IA, avant nettoyage)": max(0, 100 - fingerprint * 25),
        "VOICE (je / tu / on)": min(100, voice * 15),
    }
    values = list(checks.values())
    final = 0.6 * statistics.mean(values) + 0.4 * min(values)
    return {"checks": checks, "final": final}


def main() -> None:
    original = Path(sys.argv[1]).read_text(encoding="utf-8") if len(sys.argv) > 1 else sys.stdin.read()
    text, fixes = clean(original)
    result = score(original, text)
    print(text)
    print("\n" + "-" * 40)
    print(f"Corrections automatiques : {fixes}")
    for name, value in result["checks"].items():
        print(f"{name:<58} {value:5.1f}")
    verdict = "OK" if result["final"] >= 70 else "À REVOIR" if result["final"] >= 45 else "TROP IA"
    print(f"{'SCORE FINAL':<58} {result['final']:5.1f}  {verdict}")
    for pattern in SLOP["flag"]:
        for m in re.finditer(pattern, text, re.IGNORECASE):
            print(f"À juger toi-même : « {m.group(0)[:60]} »")


if __name__ == "__main__":
    main()
