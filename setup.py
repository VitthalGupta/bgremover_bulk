# setup for the application

from distutils.core import setup
import py2exe

setup(
    console=['main.py'],
    options={
        'py2exe': {
            'bundle_files': 1,
            'compressed': True,
            'optimize': 2,
            'dist_dir': 'dist',
            'dll_excludes': ['w9xpopen.exe'],
            'includes': ['encodings', 'encodings.*'],
            'excludes': ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email',
                            'pywin.debugger', 'pywin.debugger.dbgcon',
                            'pywin.dialogs', 'tcl', 'Tkconstants', 'Tkinter', 'tix',
                            'Tkinter', 'doctest', 'pdb', 'unittest', 'difflib',
                            'inspect', 'calendar', 'optparse', 'pickle', 'copy_reg',
                            'xml', 'xml.*', 'pydoc', 'pydoc_data', 'pyexpat', 'bz2',
                            'gzip', 'zipfile', 'zlib', 'pytz', 'dateutil', 'PIL',
                            'PIL.*', 'PIL._imagingtk', 'PIL._imagingmath',
                            'PIL._imaging', 'PIL._binary', 'PIL._imagingft',
                            'PIL._imagingcms', 'PIL._imagingmorph', 'PIL._imagingfilter',
                            'PIL._imagingmap', 'PIL._imagingtk', 'PIL._imagingmath',
            ]
        }
    }
)