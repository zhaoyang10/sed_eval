#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Utilities
==================

Functions to handle event lists (list of event items), event rolls (event activity indicator matrix used in evaluation),
and scene lists.

Event list operations
---------------------

.. autosummary::
    :toctree: generated/

    event_list.unique_event_labels
    event_list.max_event_offset

.. autoclass:: EventList
    :members:

Event roll operations
---------------------

.. autosummary::
    :toctree: generated/

    event_roll.event_list_to_event_roll
    event_roll.pad_event_roll
    event_roll.match_event_roll_lengths

Scene list operations
---------------------

.. autosummary::
    :toctree: generated/

    scene_list.unique_scene_labels

.. autoclass:: SceneList
    :members:

"""

from .event_list import *
from .event_roll import *
from .scene_list import *

__all__ = [_ for _ in dir() if not _.startswith('_')]