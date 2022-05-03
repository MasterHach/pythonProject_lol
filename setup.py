from setuptools import setup, find_packages

setup(name='funniest',
      version='0.2',
      py_modules=['pythonProject_lol'],
      packages=find_packages(),
      include_package_data=True,
      data_files=[("pythonProject_lol", ["pythonProject_lol/hmm.json",
                                         "pythonProject_lol/__init__.py",
                                         "prkt_3_5.py"])]
      )
