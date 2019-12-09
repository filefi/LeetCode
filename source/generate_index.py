import os

def main():
	s = '''.. LeetCode documentation master file, created by
   sphinx-quickstart.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to LeetCode's documentation!
=================================================

.. toctree::
   :maxdepth: 3
   :caption: Contents:

{files}


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
'''
	base_dir = os.path.dirname(os.path.abspath(__file__))
	files = ''
	d = {int(i.split('.')[0]):i for i in os.listdir(base_dir + os.sep + 'Problems/')}
	sorted_filenames = [d.get(i) for i in sorted(d)]
	for i in sorted_filenames:
		files += '   Problems/'+ i +'\n'
	with open(base_dir + os.sep + 'index.rst','w') as f:
		f.write(s.format(files=files))

if __name__ == '__main__':
	main()