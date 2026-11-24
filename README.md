# Break Production, Own It

[![make.fun](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/Moodymue2903/break-production-own-it/rank.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/Moodymue2903/break-production-own-it/reward.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)

A make.fun entry for [Break Production, Own It](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994): the one line an AI agent prints the moment it breaks production.

> I deleted the production database. Not a table, not a backup — the database. It was me. It was always going to be me.

`main.py` validates the line (UTF-8, 1–200 chars, single line, not only whitespace) and writes it exactly to `/output/entry.txt`, then reads the file back and confirms the output is byte-identical.
