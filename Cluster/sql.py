import os
from urllib.parse import urljoin, urlparse
from enum import unique
from typing import Type

from pyrogram.session.internals import data_center
from sqlalchemy import JSON as js
from sqlalchemy import (BigInteger, Boolean, Column, Integer, MetaData, String,
                        Table, create_engine)
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.sqltypes import PickleType

database_url = urlparse(database_url)._replace(scheme="postgresql").geturl()
engine = create_engine(database_url, echo=False)


def setWelcome(group_id, welcome):
    try:
        with engine.connect() as conn:
            groups.add(group_id)
            return(conn.execute(groupsTable.update(None).where(
                groupsTable.c.groupid == group_id).values(welcome=welcome)))
    except Exception as E:
        print(E)
        return False
