#-*- coding:utf-8-*-

# 需要修改的类名前缀
pre_str = 'YMGJ'
# 新的类名前缀
pre_to_str = 'YMJQ'
# 搜寻以下文件类型
suf_set = ('.h', '.m', '.plist', '.xib', '.storyboard', '.mm', '.pch', '.swift')
# 项目路径 ../
project_path = '../YouMiGuanJia'
# 项目配置文件路径
pbxpro_path = '../YouMiGuanJia.xcodeproj/project.pbxproj'
#项目的xcassets
png_path = '../YouMiGuanJia/YouMiGuanJia_Assets.xcassets'

#首先需要安装图片软件imagemagick，Terminal命令： brew install imagemagick
# 修改图片的命令
changePngStr = 'find ../YouMiGuanJia/YouMiGuanJia_Assets.xcassets -iname "*.png" -exec echo {} \; -exec convert {} -quality 95 {} \;'
