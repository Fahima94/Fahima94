# Claude Skills — Horizons Datas

Skills Claude de Fahima Behillil, cheffe de projet IA & automatisation.

## posts-video-linkedin
Transforme un vécu, un ressenti ou une note vocale brute en **post LinkedIn + script vidéo face caméra**, avec la méthode « détective des besoins » : demande exprimée vs besoin réel, prescrit vs pratiqué, travail au ticket.

7 angles : détective des besoins, prescrit vs pratiqué, Business Tech Bridge, coulisses au ticket, harnais agentique (série hebdo), conviction, effort & croyance. Chaque post suit l'arc « l'enquête » et se termine par un ticket de publication.

- `references/voice.md` : la voix, lue par le skill avant chaque écriture
- `references/slop-fr.json` : tournures toutes faites en français à retirer (à enrichir)
- `scripts/humanize.py` : nettoyage + score sur 5 contrôles

Principes : zéro invention (`{{à compléter}}` si une donnée manque), pas de vulgarité, et publication à la main uniquement.

Inspiré de la structure de [linkedin-agent-skill](https://github.com/Jakeschincariol/linkedin-agent-skill) (MIT).

## Installation
- **Claude Code** : `cp -r posts-video-linkedin ~/.claude/skills/`
- **App Claude** : zipper le dossier `posts-video-linkedin`, puis Personnaliser > Skills > + > Upload a skill
