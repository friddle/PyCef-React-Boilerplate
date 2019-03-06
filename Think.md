###  Boiler.py
          check:  
                  1.  检查系统库（python。pip。 nodejs,npm,virutalenv)
   
          build:
                  1.  检查系统库（python。pip。 nodejs,npm)
                  2.  构建virtualenv 安装必要依赖。（pycef,virtualenv）
                  3.  npm 安装global(tyarn tyarn)项目在依赖 tyarn install
                  4.  npm 安装 文件
          update: 
                  1.  pip update&&yarn update
          package:
                  1.  npm build
                  2.  pyinstaller 打包
          run:
                  1. start-main-dev
          debug:
                  1. use webjs for port
                  
                  
### Web部分直接拷贝
                  

## 第一步是先构造起来python部分 (大部分完成)
    1. 配置来自于环境变量和env（完成）
    2. Module来自于扫描package(完成)

## 第二步是在仿照写WebPack打包部分(进行中)
    1. 写完正式环境的打包。      （完成）
    2. 开始写测试环境的动态DEBUG  (完成一半。做到文件跟新后发送reload)
    3. 需要写多个页面打包成不同的页面 (暂时没计划)
    
## Pyinstaller和总体打包的研究
    1. 有点晕:暂时只能测试Linux的。无精力测试Windows的
    
## 第三步是用Python做打包系统的脚本。并且串联起来
    1.
    
## 测试WindowsXp版本的兼容
