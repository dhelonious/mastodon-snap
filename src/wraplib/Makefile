CFLAGS += -g -O0 -Wall -Wstrict-prototypes

all: wraplib.so

wraplib.so:
	${CC} ${CFLAGS} -fPIC -shared ${LDFLAGS} lib.c -o $@ -ldl

install: wraplib.so
	mkdir -p ${DESTDIR}/lib
	cp -f wraplib.so ${DESTDIR}/lib/wraplib.so

clean:
	rm -f wraplib.so
