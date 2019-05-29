#!/usr/bin/env python3
# Copyright(C) 2019 <your-name and e-mail>
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Show a very generic usage of PyTest.

This module does not have any tested counter-part in the myproject module.
It just shows few use-cases on how to use PyTest.
"""

# Let's import pytest module for the pytest.raises() and parametrize used later:

import pytest


def test_not_equal():
    """Check that not-equal sign checks values correctly."""
    assert 1 != 0, "Zero is not equal to one"


def test_raise_exception():
    """Check if there is raised an exception on error state."""
    with pytest.raises(ValueError):
        raise ValueError("Value was not provided correctly")


@pytest.mark.parametrize("a,b,expected", [
    (0, 1, -1),
    (1, 0, 1),
    (1, .5, .5),
])
def test_sub(a, b, expected):
    """A simple test-case which shows how to parametrize tests."""
    diff = a - b
    assert diff == expected, "It looks like subtract does not work correctly!"
