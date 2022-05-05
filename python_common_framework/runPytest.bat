echo ######################## Starting ########################
call pytest --alluredir reports -n 2 -s -v -rs -m regression --browser chrome --env prod --html="testresults.html"

REM call pytest --alluredir reports  -s -v -rs -m outlook --browser outlook --env windows
