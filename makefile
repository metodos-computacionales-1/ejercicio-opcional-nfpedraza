Logistic.png : Logistic.dat Logistic.py
	python Logistic.py
	

Logistic.dat : lm.out
	./lm.out

lm.out : Logistic.cpp
	c++ Logistic.cpp -o lm.out
	
clean : 
	rm lm.out Logistic.dat Logistic.png