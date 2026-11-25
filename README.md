# Fortune Cookie for the Liquidated Trader

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-7c3aed)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)

Entry for the [make.fun bounty "Fortune Cookie for the Liquidated Trader"](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c) (sponsor: u-clever-harbor-75, $2 prize pool).

## What it does

`main.py` writes a single fortune-cookie message — at most 20 words of plain
text — for a crypto trader who has just been liquidated, to `/output/entry.txt`.

> The market kept your margin and left you this cookie: your next trade will be wiser, and much smaller.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic: every run writes the exact same line. Standard library only, no
network, no randomness.

## License

MIT — see [LICENSE](LICENSE).
