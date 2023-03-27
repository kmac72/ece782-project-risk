
CC=gcc
CFLAGS=-I.
DEPS = privacy.h
OBJ = main.o privacy.o 

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

risk: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS) -lsqlite3

clean:
	rm *.o
	rm risk