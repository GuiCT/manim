from __future__ import annotations

import re
from typing import TYPE_CHECKING

from manimlib.mobject.svg.string_mobject import StringMobject
from manimlib.utils.typ_file_writing import typst_to_svg

if TYPE_CHECKING:
    from typing import Optional

    from manimlib.typing import Selector, Self, Span


TEX_MOB_SCALE_FACTOR = 0.001


class Typ(StringMobject):
    """A MObject to handle SVG rendering from Typst strings."""

    def __init__(
        self,
        *typ_strings: str,
        font_size: int = 48,
        use_labelled_svg: bool = True,
        isolate: Selector = [],
        **kwargs
    ):
        # Combine multi-string arg, but mark them to isolate
        if len(typ_strings) > 1:
            if isinstance(isolate, (str, re.Pattern, tuple)):
                isolate = [isolate]
            isolate = [*isolate, *typ_strings]

        full_typ_string = (" ".join(typ_strings)).strip()
        self.typ_string = full_typ_string

        super().__init__(
            full_typ_string,
            use_labelled_svg=use_labelled_svg,
            isolate=isolate,
            **kwargs
        )

        self.scale(TEX_MOB_SCALE_FACTOR * font_size)
        self.font_size = font_size  # Important for this to go after the scale call

    def get_svg_string_by_content(self, content: str) -> str:
        return typst_to_svg(content)

    def _handle_scale_side_effects(self, scale_factor: float) -> Self:
        if hasattr(self, "font_size"):
            self.font_size *= scale_factor
        return self

    @staticmethod
    def get_command_matches(string: str) -> list[re.Match]:
        return []

    @staticmethod
    def get_command_flag(match_obj: re.Match) -> int:
        return 0

    @staticmethod
    def replace_for_content(match_obj: re.Match) -> str:
        return match_obj.group()

    @staticmethod
    def replace_for_matching(match_obj: re.Match) -> str:
        if match_obj.group("command"):
            return match_obj.group()
        return ""

    @staticmethod
    def get_attr_dict_from_command_pair(
        open_command: re.Match, close_command: re.Match
    ) -> dict[str, str] | None:
        if len(open_command.group()) >= 2:
            return {}
        return None

    def get_configured_items(self) -> list[tuple[Span, dict[str, str]]]:
        return []

    @staticmethod
    def get_command_string(
        attr_dict: dict[str, str], is_end: bool, label_hex: str | None
    ) -> str:
        return ""

    def get_content_prefix_and_suffix(
        self, is_labelled: bool
    ) -> tuple[str, str]:
        return ("", "")
