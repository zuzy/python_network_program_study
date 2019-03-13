CTAGS = -M

OBJ := cJSON.o state_machine.o
LINK_LIB := -lm -lpthread
.PHONY: clean
all: state_machine

state_machine:$(OBJ)
	gcc -o state_machine $(OBJ) $(LINK_LIB)

clean:
	-rm *.o state_machine

