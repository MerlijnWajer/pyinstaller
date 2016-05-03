#-----------------------------------------------------------------------------
# Copyright (c) 2016, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


# SANE contains a lot of plugins. We need to collect them and bundle
# them.

import glob
import os

# FIXME: Hardcoded
plugin_path = '/usr/lib/x86_64-linux-gnu/sane/'

pattern = os.path.join(plugin_path, '*.so*')

binaries = [
    # TODO: Place them in the proper directory, not ''?
    # OTOH, LD_LIBRARY_PATH is set specifically so the root dir, possibly not to
    # other directories.
    (f, '')
    for f in glob.glob(pattern)
]

# Copy scanimage to bin/
binaries.append(('/usr/bin/scanimage', 'bin'))

# We will likely not need this, as it should be picked up automatically?
#binaries.append(('/usr/lib/x86_64-linux-gnu/libsane.so.1', ''))

# Copy over /etc/sane.d (config files)
data_files = []

for dirpath, dirnames, filenames in os.walk('/etc/sane.d'):
    for filename in filenames:
        data_files.append(os.path.join(dirpath, filename))

datas = [
    (f, 'sane')
    for f in data_files
]
