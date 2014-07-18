all : main.py about.py tools.py

main.py : extras/main_window.ui
	pyuic4 extras/main_window.ui -o main.py

about.py : extras/about.ui
	pyuic4 extras/about.ui -o about.py

tools.py : extras/tools.ui
	pyuic4 extras/tools.ui -o tools.py

clean : 
	rm *.pyc