"""Renames a Python project by replacing the template name in files and directories."""
import sys
import pathlib

OLD_NAME = "python-app-template"

FILES_TO_UPDATE = [
    "cloudbuild.yaml",
    "docs/contributing/ENVIRONMENT.md",
    "pyproject.toml",
    "README.md",
    "requirements.txt",
    "tests/test_assets.py",
    "tests/test_version.py",
    "src/python_app_template/version.py",
]

SRC_DIR = pathlib.Path("src")


class Name:
    """Encapsulates a project name with methods to convert between dash and underscore styles."""

    def __init__(self, raw: str):
        """Initialize Name with a raw string.

        Strips leading/trailing whitespace and replaces spaces with dashes.
        """
        self._raw = raw.strip().replace(" ", "-")

    @property
    def with_dashes(self) -> str:
        """Return the project name with dashes instead of underscores."""
        return self._raw.replace("_", "-")

    @property
    def with_underscores(self) -> str:
        """Returns the project name with underscores instead of dashes."""
        return self._raw.replace("-", "_")

    def __str__(self):
        """Returns a string representation showing both dash and underscore versions."""
        return f"{self.with_dashes} / {self.with_underscores}"


def _replace_in_file(filepath: pathlib.Path, old_new_pairs: list[tuple[str, str]]) -> None:
    content = filepath.read_text(encoding="utf-8")
    for old, new in old_new_pairs:
        content = content.replace(old, new)

    filepath.write_text(content, encoding="utf-8")


def _rename_package_dir(old_name: str, new_name: str) -> None:
    old_path = SRC_DIR / old_name
    new_path = SRC_DIR / new_name

    if not old_path.exists():
        print(f"⚠️ Warning: {old_path} does not exist.")
        return

    if new_path.exists():
        print(f"⚠️ Warning: {new_path} already exists.")
        return

    old_path.rename(new_path)
    print(f"📁 Renamed package dir: {old_path} → {new_path}")


def update_project_name(old_name: str, new_name: str) -> None:
    """Updates the project name in all relevant files and rename the source directory.

    Args:
        old_name:
            The current project name (dashes or underscores allowed).

        new_name:
            The new project name input by the user (dashes or underscores allowed).
    """
    old_name = Name(old_name)
    new_name = Name(new_name)

    replacements = [
        (old_name.with_dashes, new_name.with_dashes),
        (old_name.with_underscores, new_name.with_underscores),
    ]

    print("🔁 Replacing names:")
    for o, n in replacements:
        print(f"  {o} → {n}")

    for file in FILES_TO_UPDATE:
        path = pathlib.Path(file)
        if path.exists():
            _replace_in_file(path, replacements)
            print(f"✅ Updated: {file}")
        else:
            print(f"⏭️ Skipped (not found): {file}")

    _rename_package_dir(old_name.with_underscores, new_name.with_underscores)
    print("\n✅ Done!")
    print(f"🎉 Project renamed to: {new_name.with_dashes}.")


def main():
    """Entry point for the script.

    Expects a single command-line argument: the new project name (with dashes or underscores).
    """
    example = Name("my-project-name")

    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} {example.with_dashes} OR {example.with_underscores}")
        sys.exit(1)

    new_name = sys.argv[1]
    update_project_name(OLD_NAME, new_name)


if __name__ == "__main__":
    main()
