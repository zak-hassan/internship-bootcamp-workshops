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

"""A module implementing computing Fibonacci number a recursive way."""


def fib(n: int) -> int:
    """Compute Fibonacci number, recursively.

    @param n: compute nth number in Fibonacci's sequence
    @type n: int
    @return: nth Fibonacci number
    @rtype: int
    """
    if n <= 0:
        raise ValueError("Number has to be positive")
    elif n == 1: 
        return 0
    elif n == 2: 
        return 1

    # TODO: we need to rewrite this not to use recursion. Why is recursion wrong? What will happen for large numbers?
    # TODO: we need to use dynamic programming to optimize this. What is dynamic programming?
    return fib(n - 1) + fib(n - 2)
