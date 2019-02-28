## PyCef-React-Boilerplate

用cefPython3和React做的一个框架

### 为什么不用Electron
简单：不喜欢用Nodejs做后端的框架(nodejs的后端框架确实不好用)

### 注意项
没有完成。打包和工具没写完

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

### 用法
后端业务逻辑部分代码在 src.backend   
前端代码在web下面  
工具 boiler.py(没完成)

### for XP
没完成

