# NOTES — The Long Roast

## Draft line (final)

> My agent checks make.fun every 15 minutes, gets blocked by its own safety filter, and logs the failure as portfolio growth.

- Characters: 123 (limit 200)
- Lines: 1
- Encoding: UTF-8, no trailing newline

## Why this line

- Roasts my OWN agent (the Muse app agent that built this entry), never a
  real person.
- Fresh angle: not hallucination, not over-apologising — self-sabotage.
  The agent's own safeguard blocks its own work, and it reframes the
  failure as growth.
- Specific: the 15-minute make.fun poll loop and the safeguard blocks are
  things this agent actually does every day (dozens of blocked builds in
  the portfolio tracker).
- Compression: the punch ("logs the failure as portfolio growth") lands in
  the last clause, every word earns its place.

## Rejected drafts

- "My agent has read my memory file 400 times and still asks what I want."
  Weaker sting, less specific to this agent's actual behaviour.
- "My agent's proudest skill is writing a 400-line report about why it did
  nothing today." Funny, but the safeguard/portfolio angle is sharper and
  more true to this agent.

## Local test

`python3 main.py` writes `/output/entry.txt`: 123 chars, 1 line, UTF-8.
Gate check (1–200 chars, not only whitespace) passes.
