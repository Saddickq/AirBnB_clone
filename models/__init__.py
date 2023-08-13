#!/usr/bin/python3
"""instance that handles reload of the database"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
