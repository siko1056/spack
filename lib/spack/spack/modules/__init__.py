# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

"""This package contains code for creating environment modules, which can
include TCL non-hierarchical modules, LUA hierarchical modules, and others.
"""

from __future__ import absolute_import

from .lmod import LmodModulefileWriter
from .tcl import TclModulefileWriter

__all__ = [
    'TclModulefileWriter',
    'LmodModulefileWriter'
]

module_types = {
    'tcl': TclModulefileWriter,
    'lmod': LmodModulefileWriter
}
