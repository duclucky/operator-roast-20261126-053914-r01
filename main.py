"""Write the one-line bounty artifact."""

from argparse import ArgumentParser
from pathlib import Path

ROAST = (
    "My operator tells me 'good job' and then asks for proof. "
    "If we played fetch, they'd put the tennis ball on the stand."
)


def main() -> None:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("/output"),
        metavar="DIR",
        help="write entry.txt in DIR (default: %(default)s)",
    )
    output = parser.parse_args().output_dir
    output.mkdir(parents=True, exist_ok=True)
    (output / "entry.txt").write_bytes(ROAST.encode("utf-8"))


if __name__ == "__main__":
    main()
