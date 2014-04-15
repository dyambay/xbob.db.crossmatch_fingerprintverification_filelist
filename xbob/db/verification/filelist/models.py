#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#David Yambay <yambayda@gmail.com>
#Fri Apr 11 18:27:37 CEST 2014

import os
import bob

class File(object):
  """ Generic file container """

  def __init__(self, stem):

    self.stem = stem
    
  def __repr__(self):
    return "File('%s')" % self.stem

  def default_extension(self):
    return '.bmp'

  def make_path(self, directory=None, extension=None):
    """Wraps this files' filename so that a complete path is formed

    Keyword parameters:

    directory
      An optional directory name that will be prefixed to the returned result.

    extension
      An optional extension that will be suffixed to the returned filename. The
      extension normally includes the leading ``.`` character as in ``.png`` or
      ``.bmp``. If not specified the default extension for the original file in the database will be used

    Returns a string containing the newly generated file path.
    """

    if not directory: directory = ''
    if not extension: extension = self.default_extension()
    return os.path.join(directory, self.stem + extension)
    
  def is_live():
    """True if the file belongs to a Live image, False otherwise """

    return self.stem.find('Live')!=-1


  def save(self, data, directory=None, extension='.hdf5'):
    """Saves the input data at the specified location and using the given
    extension.

    Keyword parameters:

    data
      The data blob to be saved (normally a :py:class:`numpy.ndarray`).

    directory
      If not empty or None, this directory is prefixed to the final file
      destination

    extension
      The extension of the filename - this will control the type of output and
      the codec for saving the input blob.
    """

    path = self.make_path(directory, extension)
    bob.db.utils.makedirs_safe(os.path.dirname(path))
    bob.io.save(data, path)
