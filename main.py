#!/usr/bin/env python3
"""Write the competition entry: one Wi-Fi network name, 32 chars max.

Entry: "The WiFi died with Grandma" (26 characters).
A passer-by sees a network list, reads it, and gets the whole story in
one breath: Grandma is gone, and the Wi-Fi went with her. The joke lands
on the first read, the twist is dark, and every character earns its place.
Stdlib only; no network, no secrets, no reading outside this file.
"""

import os

ENTRY = "The WiFi died with Grandma"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 32, f"entry must be 1-32 chars, got {len(text)}"
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        # No trailing newline: the gate counts every character in the file,
        # so the file must hold exactly the 26-character name, nothing more.
        f.write(text)


if __name__ == "__main__":
    main()
