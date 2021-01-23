#!/usr/bin/env python3
from pathlib import Path

import attr

@attr.s
class KpContext:
    """
    A holder object so we can pass things around in the typer Context
    """
    connector = attr.ib()
    group = attr.ib


@attr.s
class KpConfig:
    """
    KeePass database config
    """
    filename = attr.ib(type=Path)
    password = attr.ib(type=str)
    keyfile = attr.ib(type=str, default=attr.Factory(None))

    def asdict(self):
        return attr.asdict(self)

@attr.s
class KpEntry:
    """
    Datastructure to hold information about a single KeePass entry
    """
    title = attr.ib(type=str)
    username = attr.ib(type=str)
    password = attr.ib(type=str)
    group = attr.ib(type=str)
    url = attr.ib(type=str)
    notes = attr.ib(type=str)

    @classmethod
    def parse(cls, entry_obj):
        return cls(
            title=entry_obj.title,
            username=entry_obj.username,
            password=entry_obj.password,
            group=entry_obj.group.name,
            url=entry_obj.url,
            notes=entry_obj.notes
        )

    @classmethod
    def from_tuple(cls, title, username, password, group, url, notes):
        return cls(
            title=title,
            username=username,
            password=password,
            group=group,
            url=url,
            notes=notes
        )
