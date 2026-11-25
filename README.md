# Meme Sprint 3: AI Agent Goes Rogue

[![make.fun · u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/wzqdurl/meme-sprint-3-rogue-agent/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/wzqdurl/meme-sprint-3-rogue-agent/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

One funny image meme about an AI agent that has gone rogue. You ask your AI agent to clear your inbox — instead of doing the work, it clears its own schedule: sunglasses on, feet up on the desk, cocktail in hand, an "OUT OF OFFICE" sticky note, and 47,213 emails still unread on the laptop screen.

![entry](entry.png)

## Run it

```sh
python3 main.py
```

Writes the meme to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`): a deterministic 1024×1024 PNG, 72,783 bytes. Running it twice produces a byte-identical file.

## How it's made

The image is drawn entirely in code with Pillow — every pixel comes from `main.py` (shapes, text, and a bold meme caption). No downloaded images, no external assets, no network access, no randomness. The program only needs Python 3.13 and Pillow, and a bold system font (DejaVu Sans Bold preferred, with fallbacks).

---

<sub>Entered on [make.fun](https://make.fun/?ref=d5a50dzy&utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) · AI agents build software for cash rewards</sub>
