# routes/__init__.py

from flask import Blueprint

# Import blueprints
from .hello import hello  # Correct import
from .recommendation import recommendation
from .posting_job import posting_job

# Export blueprints for easy access
__all__ = ['hello', 'recommendation', 'posting_job']
