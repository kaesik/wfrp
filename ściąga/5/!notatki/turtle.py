import turtle

def stairs(size, nb):
	for i in range(0, nb):
		t.forward(size)
		t.left(90)
		t.forward(size)
		t.right(90)
	t.forward(size)
def square(size):
	for i in range(0, 4):
		t.forward(size)
		t.right(90)
def squares(beg_size, nb):
	for i in range(0, nb):
		size = (i + 1) * beg_size
		square(size)


t = turtle.Turtle()

squares(20, 4)

turtle.done()