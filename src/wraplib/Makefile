CFLAGS += -g -O0 -Wall -Wstrict-prototypes
INSTALL_DIR := ../install

all: wraplib.so

wraplib.so:
	${CC} ${CFLAGS} -fPIC -shared ${LDFLAGS} lib.c -o $@ -ldl

install: wraplib.so
	mkdir -p ${INSTALL_DIR}
	cp -f wraplib.so ${INSTALL_DIR}/wraplib.so

clean:
	rm -f ./wraplib.so
