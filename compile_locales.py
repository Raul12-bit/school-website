"""Собрать django.mo из django.po без установки GNU gettext (используется polib)."""
from pathlib import Path

import polib

BASE = Path(__file__).resolve().parent

for lang in ("kk", "ru", "en"):
    po_path = BASE / "locale" / lang / "LC_MESSAGES" / "django.po"
    if not po_path.is_file():
        continue
    mo_path = po_path.with_suffix(".mo")
    polib.pofile(str(po_path)).save_as_mofile(str(mo_path))
    print(f"OK {mo_path}")
