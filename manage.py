#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import sys


def main() -> None:
    """Run administrative tasks."""
    from django.core.management import execute_from_command_line  # noqa: PLC0415

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
