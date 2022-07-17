from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
from pathlib import Path

'''
works when running 'python myrunner.py' from tutorial/my-iris folder
metadata is ProjectMetadata(config_file=WindowsPath('D:/projects/kedro/tutorial/my-iris/pyproject.toml'), 
    package_name='my_iris', project_name='my_iris', project_path=WindowsPath('D:/projects/kedro/tutorial/my-iris'), 
    project_version='0.18.2', source_dir=WindowsPath('D:/projects/kedro/tutorial/my-iris/src'))
fails when running 'python my-iris\myrunner.py' from tutorial folder
metadata is ProjectMetadata(config_file=WindowsPath('D:/projects/kedro/tutorial/my-iris/pyproject.toml')
    Could not find the project configuration file 'pyproject.toml' in the current directory
=> runner needs to be same level toml file

switching to hardcoded name -> no module named 'None' => need bootstrap_project()

0. pip install kedro; kedro new --starter=pandas-iris
1. test deploy to AC (embedded data)
2. test deploy to AC (using dali and mdl data)
3. with pyspark
'''
metadata = bootstrap_project(Path.cwd())
with KedroSession.create(metadata.package_name) as session:
    # print('metadata is', metadata)
    session.run()
# with KedroSession.create('my_iris') as session:
#     print('metadata is', session.metadata)
#     session.run()
    