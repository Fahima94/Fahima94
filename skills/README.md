# Claude Skills — Horizons Datas

Skills Claude de Fahima Behillil, cheffe de projet IA & automatisation.

## posts-video-linkedin
Transforme un ressenti ou un vécu en **post LinkedIn + script vidéo face caméra**, en 6 styles (coulisses, leçon apprise, coup de cœur, victoire, pédago express, reconversion).

- `references/voice.md` : la voix, lue par le skill avant chaque écriture
- `references/slop-fr.json` : tournures toutes faites en français à retirer (à enrichir)
- `scripts/humanize.py` : nettoyage + score sur 5 contrôles

Principes : zéro invention (`{{à compléter}}` si une donnée manque), pas de vulgarité, et publication à la main uniquement.

Inspiré de la structure de [linkedin-agent-skill](https://github.com/Jakeschincariol/linkedin-agent-skill) (MIT).

## Installation
- **Claude Code** : `cp -r posts-video-linkedin ~/.claude/skills/`
- **App Claude** : zipper le dossier `posts-video-linkedin`, puis Personnaliser > Skills > + > Upload a skill
