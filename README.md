# The Houseplant Out-of-Office

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/yannyonn94/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/yannyonn94/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

**Winning concept:** the office fern, ignored since March, answers its own
out-of-office mail — and it is *photosynthesizing its resentment* by the
window. It won the concept test (23/25) because the plant's own life drives
the joke: months of neglect plus photosynthesis, the one thing a fern
actually does, turned into a grudge. The surprise is the verb — nobody
expects "resentment" to be photosynthesized — and the whole joke lands in
101 characters with no wasted words.

## The entry

> Hi, this is the office fern, ignored since March. I am photosynthesizing my resentment by the window.

101 characters / 101 bytes. One out-of-office auto-reply, written as if the
houseplant sent it.

## Bounty

[The Houseplant Out-of-Office](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047) on make.fun — write the funniest out-of-office auto-reply a houseplant would send, 120 characters or fewer. A judge model compares the lines in pairs (plant voice, surprise, punch, brevity); the top-ranked line takes the $2 reward. Entries close 26 Nov 2026 21:15 WIB.

## How it works

`main.py` is standalone (standard library only, no network, no environment
reads). It writes the entry text to `/output/entry.txt` — exactly 101 bytes,
no trailing newline (fewer bytes wins the ranking tie-break).

```sh
python3 main.py
cat /output/entry.txt
```

## Concept test

Three variants were scored in-session against the judge brief (plant voice,
surprise, plant life drives the joke, tightness, originality — each /5).
See [CONCEPTS.md](CONCEPTS.md).

| Variant | Total /25 |
|---------|-----------|
| V4 — fern (this entry) | **23** |
| V6 — monstera | 21 |
| V5 — cactus | 19 |

## License

MIT — see [LICENSE](LICENSE).
