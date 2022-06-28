"""Functions to filter out activity data."""

# Authors: Grégory Hammad <gregory.hammad@uliege.be>
#
# License: BSD (3-clause)

# from . import filters

from .filters import FiltersMixin
from .utils import _create_inactivity_mask

__all__ = ["FiltersMixin", "_create_inactivity_mask"]
