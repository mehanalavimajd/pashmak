# The Pashmak Jit Compiler
The **Jit** or **Just in time** compiler, is a system to cache the code and compress that to speed up the interpreter.

this system, compresses the content of scripts and saves them to `__pashmam__` directory. then, when file is ran again, jit system loads compressed content from that cache.

you can see `__pashmam__` directory alongside your scripts. this directory contains cached codes.

Also, make sure to add `__pashmam__` file to your **gitignore**.

To disable the jit, you can use `PASHMAK_DISABLE_JIT` environment variable with value `1` while running the pashmak interpreter.
for example:

```bash
$ PASHMAK_DISABLE_JIT=1 pashmak somefile.pashm
```
