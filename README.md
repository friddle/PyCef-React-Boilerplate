##PyCef-React-Boilerplate

use cefpython and React tools for desktop environment

###Why
Because I hate the js as backend language. The so many library force use async and callback.
 the only matter callback should only be used in front ui update.    
the callback and async made the system is hard to debug and track. and js is not ok for organize 
for backend language.   


### FrameWork
```html
   src---
      web---
         App.js
         index.css
         hello.js 
      backend---(use web)  
         hello.py 
      framework---   
         jswrapper --- include js 2 python 2(provider mutiple thread pool)   
         qt --- include qt tools and framework    
         lib --- include some tools provide for js     
         installer --include installer tools
         shell-- pyinstaller shell:打包脚本
   resources---
      icon---
      static---
   pip.conf 
   package.json  (windows-build-tools:windows环境.webpack配置等) 
   tools.py --核心是这个
```

### Usage
Must use Qt5


### for XP
use pycef Version==

