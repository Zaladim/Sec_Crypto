all:
	@cp src/challenge01.py challenge01
	@cp src/challenge02.py challenge02
	@cp src/challenge03.py challenge03
	@cp src/challenge04.py challenge04
	@cp src/challenge05.py challenge05
	@cp src/challenge06.py challenge06
	@cp src/challenge07.py challenge07
	@cp src/challenge08.py challenge08
	@cp src/challenge09.py challenge09
	@cp src/challenge10.py challenge10
	@cp src/challenge11.py challenge11
	@cp src/challenge12.py challenge12
	@cp src/challenge13.py challenge13
	@cp src/challenge14.py challenge14
	@chmod u+x challenge*

clean:
	rm challenge*

fclean: clean

re: fclean all