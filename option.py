import os
import getopt
import sys
from img_parser import JpegParser

class Option :
    def __init__(self):

        self.input_img_path = ''

    def help():
        '''
			python main.py -i img
        '''

        print ("[-i][--input=] is input folder")
        print ("[usage] : python main.py -i [folderName]")

    def do_work(self):
    # 이미지 파일 찾기
        file_list = os.listdir(self.input_img_path)
        print (file_list)
        for file in file_list:
            ext = file.split(".")[-1]
            if (ext == 'jpg' or ext == 'jpeg'):
        
                print (self.input_img_path + '\\'+file)
                file_path = self.input_img_path + '\\'+file
            
                jpegParser = JpegParser(file_path)
                if (self.input_img_path != ''):
                    jpegParser.set_img_info()
                    jpegParser.get_img_info()

    def get_option(self):
        try:
        # 여기서 입력을 인자를 받는 파라미터는 단일문자일 경우 ':' 긴문자일경우 '='을끝에 붙여주면됨
            opts, args = getopt.getopt(sys.argv[1:],"i:f",["input=","help"])
        
        except getopt.GetoptError as err:
            print (str(err))
            self.help()
            sys.exit(1)
        
        if opts == [] :
            #noOption()
            self.help()
            sys.exit(1)

        for opt,arg in opts:

            if (opt == '-i' or opt =='--input'):
                self.input_img_path = arg

            elif ( opt == "-h") or ( opt == "--help"):
                help()
                sys.exit(1)