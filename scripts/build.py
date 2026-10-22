"""Waliduje skille wobec specyfikacji agentskills.io i pakuje każdy do dist/<name>.zip."""
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ALLOWED = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def frontmatter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise ValueError("brak frontmattera")
    fields, key = {}, None
    for line in m.group(1).splitlines():
        if line.startswith("  ") and key:
            continue  # zagnieżdżone pola metadata
        k, _, v = line.partition(":")
        key = k.strip()
        fields[key] = v.strip()
    return fields


def check(skill_dir: Path) -> list[str]:
    errors = []
    fm = frontmatter((skill_dir / "SKILL.md").read_text(encoding="utf-8"))
    name, desc = fm.get("name", ""), fm.get("description", "")
    if extra := set(fm) - ALLOWED:
        errors.append(f"niedozwolone klucze: {sorted(extra)}")
    if not (1 <= len(name) <= 64 and NAME_RE.match(name)):
        errors.append(f"zła nazwa: {name!r}")
    if name != skill_dir.name:
        errors.append(f"nazwa {name!r} różna od folderu {skill_dir.name!r}")
    if not 1 <= len(desc) <= 1024:
        errors.append(f"description ma {len(desc)} znaków")
    lines = (skill_dir / "SKILL.md").read_text(encoding="utf-8").count("\n")
    if lines > 500:
        errors.append(f"SKILL.md ma {lines} linii (>500)")
    return errors


def main() -> int:
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    failed = False
    for skill_dir in sorted((ROOT / "skills").iterdir()):
        errors = check(skill_dir)
        if errors:
            failed = True
            print(f"FAIL {skill_dir.name}: {'; '.join(errors)}")
            continue
        out = dist / f"{skill_dir.name}.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(skill_dir.rglob("*")):
                z.write(f, f.relative_to(skill_dir.parent))
        print(f"OK   {skill_dir.name} -> dist/{out.name}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
