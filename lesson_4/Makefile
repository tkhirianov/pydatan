6_fib.so: 6_fib.o
	$(CXX) -shared $^ -o $@ -Wl,--whole-archive -Wl,--no-whole-archive

6_fib.o : CXXFLAGS+=-fPIC
