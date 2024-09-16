
import sys,imgkit

html_filename=sys.argv[1]
img_filename=sys.argv[2]

def convert_html2img():
	imgkit.from_file(html_filename, img_filename)


#
# MAIN
# 

if __name__ == '__main__':
    convert_html2img()