## PyCef-React-Boilerplate
use cefpython and React tools for desktop environment
[中文文档](./README-CN.md)
<div align=>
      <img src="./internals/img/show/show.png"/></a>
</div>
web part forked [electron-react-boilerplate:https://github.com/chentsulin/electron-react-boilerplate]   
python part inspired by [cefpython:https://github.com/cztomczak/cefpython]

### Why Not User Electron
Simple: Who want to use python as backend server logic not nodejs.
Nodejs as backend language is so fucked to use

### First Know
Not finish(Package and Tools Part)
Require Tools:
npm yarn pip python


### FrameWork
```html
   conf--
      webpack-> webpack package configuration
   web---
        render->
           components-> react components
           containers-> react page
           models->mbox
        template-> 
           app.html -> page template
   src---
      backend---(use web)  
         hello.py 
      framework---   
         libs --- include some tools for js system default provide
         qt --- include qt tools and framework    
         installer --include installer tools
         shell-- pyinstaller shell:
   resources---
      icon---
      static---
   pip.conf 
   package.json  
   boiler.py --the build tools
   babel.config.js --babel settings
   
```

### Usage
  1. build
  2. write code  
     -- package: write python code to src.backend 
  

### for XP

