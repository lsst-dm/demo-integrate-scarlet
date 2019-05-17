Call Stack Profiling
====================

Run scripts/callstack_profiling.py

This script contains a call to the cProfile module which profiles a call to the run method of the deblender task and
outputs the results to a file named callstack_profile.cprof.

Two useful tools to visualize the results are gprof2dot and snakeviz. Both programs are installable via pip
install. Snakeviz produces an iterative web page with various views on the execution flow. Gprof2dot
translates the profiling output into the dot language and uses it to produce a flow diagram of the call tree
color coded by the amount of time spent in a function. An example execution of this process is as follows.

```
gprof2dot -f pstats callstack_profile.cprof |dot -Tpng -o callstack_profile.png
```

As a note this command presupposes that dot is installed on your system. If it is not, consult your operating
system for how best to install it. An example output can be found at images/callstack_profile.png


# Profile timing
|      | No Sym | Sym |
|------|--------|-----|
|Before| 1.2s   |6.6s |
|------|--------|-----|
|After |1.2s    |1.8s |
|------|--------|-----|
