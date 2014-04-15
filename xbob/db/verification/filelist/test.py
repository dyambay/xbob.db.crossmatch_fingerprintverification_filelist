#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# David Yambay <yambayda@gmail.com>
# Fri Apr 11 18:31:31 CET 2014
#
# Copyright (C) 2011-2012 Idiap Research Institute, Martigny, Switzerland
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""A few checks at the Crossmatch Fingerprint database.
"""

import os, sys
import unittest
from . import Database
import bob

class CrossmatchTestCase(unittest.TestCase):
  """Performs various tests on the LivDet 2013 fingerprint liveness database."""

  def test01_recognition(self):
    db = Database()
    f = db.objects(protocols='Recognition', groups='Train')
    self.assertEqual(len(f), 966) 
    f = db.objects(protocols='Recognition', Groups='Test')
    self.assertEqual(len(f), 966) 
