REM installing the pipenv, pytest, selenium
echo  Starting installation
pip3 install pytest
timeout 1
pip3 -m pip install --upgrade pip
timeout 1
pip install selenium
timeout 1
pip3 install pytest-html
timeout 1
pip3 install pytest-xdist
timeout 1
pip install pytest-timeout
timeout 1
pip3 install requests
timeout 1
pip install jsonpath
timeout 1
pip install allure-pytest
timeout 1
pip install psycopg2
pip install unipath
echo  Installation Finished
