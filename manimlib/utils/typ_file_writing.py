from __future__ import annotations

import subprocess
import tempfile
from functools import lru_cache
from pathlib import Path

from manimlib.utils.cache import cache_on_disk


@lru_cache(maxsize=128)
def typst_to_svg(
    typst: str,
    show_message_during_execution: bool = True,
) -> str:
    """Convert Typst string to SVG string.

    Args:
        typst: Typst source code

    Returns:
        str: SVG source code

    Raises:
        TypstError: If Typst compilation fails
        NotImplementedError: If compiler is not supported
    """
    if show_message_during_execution:
        message = f"Writing {(typst)[:70]}..."
    else:
        message = ""

    header = "#set page(width: auto, height: auto, margin: 0pt, fill: none)"
    full_typst = f"{header}\n{typst}"
    return full_typ_to_svg(full_typst, message)


@cache_on_disk
def full_typ_to_svg(typ: str, message: str = ""):
    if message:
        print(message, end="\r")

    # Write intermediate files to a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        typ_path = Path(temp_dir, "working").with_suffix(".typ")
        svg_path = typ_path.with_suffix(".svg")

        # Write Typst file
        typ_path.write_text(typ)

        # Run Typst compiler
        command = ["typst", "compile", str(typ_path), str(svg_path)]
        process = subprocess.run(
            command,
            shell=True,
        )

        if process.returncode != 0:
            # Handle error
            raise TypstError("Typst compilation failed")

        svg_text = svg_path.read_text("utf-8")

        # Return SVG string
        result = svg_text

    if message:
        print(" " * len(message), end="\r")

    return result


class TypstError(Exception):
    pass
