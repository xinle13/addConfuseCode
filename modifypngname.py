#!/usr/bin/env python3
# coding=utf-8

#1遍历目录Assets.xcassets
#2查找不是Contents.json的文件夹
#3修改@2x @3x .png文件名，contents.json文件名

import os
import setFile

png_path = setFile.png_path

# os.renames('./Assets.xcassets/wojiubugaosuni.imageset/wojiubugaosuniabcc.png', './Assets.xcassets/wojiubugaosuni.imageset/wojiubugaosuniabcc123.png')
kLocalImageIndex = 0
def pngPrefixString():
	global kLocalImageIndex
	kLocalImageIndex = kLocalImageIndex + 1
	return 'isOrangeBlue' + str(kLocalImageIndex)

# for (root, dirs, files) in os.walk(png_path):
# 	for dirs_name in dirs:
# 		subpng_path = os.path.join(png_path, dirs_name)
# 		for (root2, subdirs,files2) in os.walk(subpng_path):
# 			for dirs_name2 in subdirs:
# 				subpng_path2 = os.path.join(subpng_path, dirs_name2)
# 				for (rot3, subdirs3, files3) in os.walk(subpng_path2):
# 					for fileName in files3:
# 						if fileName.endswith('.png'):
# 							print fileName
# 							newFileName = pngPrefixString()+fileName
# 							print os.path.join(subpng_path, fileName)
# 							os.renames(os.path.join(subpng_path2, fileName), os.path.join(subpng_path2, newFileName))
# 							with open(os.path.join(subpng_path2, 'Contents.json'), 'r+') as f4:
# 								s1 = f4.read().replace(fileName, newFileName)
# 								f4.seek(0)
# 								f4.write(s1)
# 								f4.truncate()
# 								f4.close()


def gci(filepath):
	files = os.listdir(filepath)
	for fi in files:
		fi_d = os.path.join(filepath,fi)
		if os.path.isdir(fi_d):
			gci(fi_d)
		else:
			if fi.endswith('.png'):
				print fi_d
				newFileName = pngPrefixString()+fi
				os.renames(fi_d, os.path.join(filepath, newFileName))
				with open(os.path.join(filepath, 'Contents.json'), 'r+') as f4:
					s1 = f4.read().replace(fi, newFileName)
					f4.seek(0)
					f4.write(s1)
					f4.truncate()
					f4.close()
def modifyPngName():
	gci(png_path)
