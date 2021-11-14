# Logo3D
3D Logo interpreter in Python using OpenGL

## Setup

**Read this entire section before you start running pip commands!**

This Python program uses [PyGame](https://www.pygame.org/news) and [openGL](https://www.opengl.org/) and was written and tested in Windows. PyGame can be installed easily enough with `pip`:

```
pip install pygame
```

In theory, it should also be possible to install openGL with pip:

```
pip install PyOpenGL PyOpenGL_accelerate
```

...*but*, this didn't work for me, and glancing at the similar number of problems I found on Google, it also doesn't work for a lot of users on Windows. According to several threads on [Stack Overflow](https://stackoverflow.com/questions/26700719/pyopengl-glutinit-nullfunctionerror) the easiest solution is to first remove PyOpenGL if you did run the previous commands:

```
pip uninstall PyOpenGL PyOpenGL_accelerate
```

...then visit [this site](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl) and download the appropriate .whl files for your Python version and OS. Since I am using Python 3.7 on Windows x86 I needed to download `PyOpenGL_accelerate-3.1.5-cp37-cp37m-win_amd64.whl` and `PyOpenGL-3.1.5-cp37-cp37m-win_amd64.whl` which could then be installed with the following:

```
pip install PyOpenGL_accelerate-3.1.5-cp37-cp37m-win_amd64.whl --force-reinstall
pip install PyOpenGL-3.1.5-cp37-cp37m-win_amd64.whl --force-reinstall
```

## Running

Once your environment is setup correctly, you should be able to run the main `Logo3D.py` file from your terminal:

```
python Logo3D.py source-file [options]
       [options] - /d         (debug mode)
       [options] - /r a:x:y:z (rotate at angle 'a' around '(x,y,z)')
                              (defaults to 1:1:1:1)

e.g. python Logo3D.py cude.lgo
```

The first parameter should be a Logo source code file.

The `/d` parameter can be used to specify debug-mode, and will cause the program to output additional information during the tokenising, parsing and executing phases. If your Logo script doesn't run, try enabling this flag to see where the syntax error is.

The `/r` parameter can be used to specify rotation angle and `(x,y,z)` location for performing rotations once the 3D model has been rendered.

## Logo Commands

The program supports the following commands:

Command | Meaning
------- | -------------
FD X | Move turtle forward X units
BK X | Move turtle forward X units
RT D | Turn turtle right D degrees
LT D | Turn turtle left D degrees
UT D | Turn turtle up D degrees
DT D | Turn turtle down D degrees
PENUP | Lift pen
PENDOWN | Drop pen
HOME | Return turtle to (0, 0, 0)
REPEAT N [ Commands ] | Repeat set of commands N times

So, for example, we can draw a square with the following:

```
FD 1 RT 90
FD 1 RT 90
FD 1 RT 90
FD 1 RT 90
```

We can be smarter and use a `REPEAT` loop:

```
REPEAT 4 [
    FD 1
    RT 90  
]
```

Both programs will produce an image that looks like this:

SCREENSHOT

We can use move in all three dimensions by adding the `UT` or `DT` commands:

```
FD 1 UT 90
FD 1 UT 90
FD 1 LT 90
```

The above program will draw the partial outline of a square:

SCREENSHOT

Once we have our 3D image rendered we can use the <kbd>←</kbd>, <kbd>→</kbd>, <kbd>↑</kbd> and <kbd>↓</kbd> buttons on our keyboard to pan, and use <kbd>-</kbd> and <kbd>=</kbd> to zoom in and out:

SCREENSHOT GIT