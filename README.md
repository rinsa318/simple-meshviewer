# simple-meshviewer
PyOpenGL based simple mesh viewer

<div align="center">
  <img src="figure/usage.gif" width=300>
  <div style="text-align: center;">
    Figure1. Overview of this repo
  </div>
</div>


## Environment
Ubuntu 18.04  
Python3.6(Anaconda3-5.2.0)



## Dependency

+ PyOpenGL
+ sys
+ os
+ PIL
+ datetime


## Usage
```
$ python main.py argvs[1] argvs[2]

  argvs[1] : path to mash (.obj)
  argvs[2] : registered materials index
             --> see figure2

*/---------------------------- manual ----------------------------/*
  Drag with Left Mousebutton  :  move eye position
  Drag with right Mousebutton :  move down/up to zoom in/out
  Drag with middle Mousebutton:  move vertical/horizontal to
                                 translate the screen along y/x axis
            a / A             :  turn on/off axis 
            w / W             :  turn on/off wireframe 
              r               :  reset viewport 
              s               :  take a screenshot as .png 
              q               :  quit the program
*/----------------------------------------------------------------/*

```

<div align="center">
  <img src="figure/figure1.png" width=70%>
  <div style="text-align: center;">
    Figure2. List of registered materials
  </div>
</div>
