SRCS = $(wildcard *.cpp)

PROGS = $(patsubst %.cpp,%.exe,$(SRCS))

all: $(PROGS)

%.exe: %.cpp
	g++.exe -static -DONLINE_JUDGE -lm -s -x c++ -Wl,--stack=268435456 -O2 -std=c++11 -D__USE_MINGW_ANSI_STDIO=0 -o $@ $<

