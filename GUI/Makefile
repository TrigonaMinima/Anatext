all : main.py about.py columns.py

main.py : extras/main_window.ui
	pyuic4 extras/main_window.ui -o main.py

about.py : extras/about.ui
	pyuic4 extras/about.ui -o about.py

columns.py : extras/columns.ui
	pyuic4 extras/columns.ui -o columns.py

clean : 
	rm *.pyc