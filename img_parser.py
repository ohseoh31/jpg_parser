import os
import getopt
import sys
import binascii
import struct

#파일을 불러오는 함수 구현
#TODO 마커 추적 
#해당 마커부터 다음 2byte를 읽어 길이를 파악하고 해당 2byte부터 size 만큼 이동

#FFD8 ~ FFD9


#1. input 특정 폴더
#2. 폴더내의 jpg 파일 읽기
#3. 파일중 JPEG 파일 확인
#4. output JPEG 파일

'''
	2. txt akzj, offset
'''
#4. endian
jpeg_marker = {
    #Start Of Frame markers, non differentail, Huffman coding
    '0xffc0' : 'SOF00',#Baseline DCT
    '0xffc1' : 'SOF01',#Extended sequential DCT
    '0xffc2' : 'SOF02',#Progressive DCT 
    '0xffc3' : 'SOF03',#Lossless (sequential)
    
    #Strat Of Frame markers, differentail, Huffman coding
    '0xffc5' : 'SOF05',#Differentail sequential DCT
    '0xffc6' : 'SOF06',#Differentail progressive DCT
    '0xffc7' : 'SOF07',#Differentail lossless (sequential)

    #Start Of Frame markers, non-differential, arithmetic coding
    '0xffc8' : 'JPG',  #Reserved for JPEG extensions
    '0xffc9' : 'SOF09',#Extended sequential DCT
    '0xffca' : 'SOF10',#Progressive DCT
    '0xffcb' : 'SOF11',#Lossless (sequential)

    #Start Of Frame markers, differential, arithmetic coding
    '0xffcd' : 'SOF13',#Differential sequential DCT
    '0xffce' : 'SOF14',#Differential progressive DCT
    '0xffcf' : 'SOF15',#Differential lossless (sequential)

    #Huffman table specification
    '0xffc4' : 'DHT',  #Define Huffman table(s)

    #Arithmetic coding conditionin specification
    '0xffcc' : 'DAC',  #Define arithmetic coding conditioning(s)

    #Restart interval termination
    '0xffd0' : 'RST',  #Restart with modulo 8 count "m"

    #Other markers
    '0xffd8' : 'SOI',  #Start of image
    '0xffd9' : 'EOI',  #End of image
    '0xffda' : 'SOS',  #Start of scan
    '0xffdb' : 'DQT',  #Define quantization table(s)
    '0xffdc' : 'DNL',  #Define number of lines
    '0xffdd' : 'DRI',  #Define restart interval
    '0xffde' : 'DHP',  #Define hierarchical progression
    '0xffdf' : 'EXP',  #Expand reference component(s)

    '0xffe0' : 'APP00',  #Reserved for application segments
    '0xffe1' : 'APP01',  #Reserved for application segments
    '0xffe2' : 'APP02',  #Reserved for application segments
    '0xffe3' : 'APP03',  #Reserved for application segments
    '0xffe4' : 'APP04',  #Reserved for application segments
    '0xffe5' : 'APP05',  #Reserved for application segments
    '0xffe6' : 'APP06',  #Reserved for application segments
    '0xffe7' : 'APP07',  #Reserved for application segments
    '0xffe8' : 'APP08',  #Reserved for application segments
    '0xffe9' : 'APP09',  #Reserved for application segments
    '0xffea' : 'APP10',  #Reserved for application segments
    '0xffeb' : 'APP11',  #Reserved for application segments
    '0xffec' : 'APP12',  #Reserved for application segments
    '0xffed' : 'APP13',  #Reserved for application segments
    '0xffee' : 'APP14',  #Reserved for application segments
    '0xffef' : 'APP15',  #Reserved for application segments
    
    '0xfff0' : 'JPG00',  #Reserved for JPEG extensions
    '0xfff1' : 'JPG01',  #Reserved for JPEG extensions
    '0xfff2' : 'JPG02',  #Reserved for JPEG extensions
    '0xfff3' : 'JPG03',  #Reserved for JPEG extensions
    '0xfff4' : 'JPG04',  #Reserved for JPEG extensions
    '0xfff5' : 'JPG05',  #Reserved for JPEG extensions
    '0xfff6' : 'JPG06',  #Reserved for JPEG extensions
    '0xfff7' : 'JPG07',  #Reserved for JPEG extensions
    '0xfff8' : 'JPG08',  #Reserved for JPEG extensions
    '0xfff9' : 'JPG09',  #Reserved for JPEG extensions
    '0xfffa' : 'JPG10',  #Reserved for JPEG extensions
    '0xfffb' : 'JPG11',  #Reserved for JPEG extensions
    '0xfffc' : 'JPG12',  #Reserved for JPEG extensions
    '0xfffd' : 'JPG13',  #Reserved for JPEG extensions
        
    '0xfffe' : 'COM',  #Comment

    #Reserved markers
    '0xff01' : 'TEM',    #For temporary private use in arithmetic coding    
    #'0xff02' ~ 0xffbf : 'RES',  #Resrved    
}


class JpegParser:

    def __init__(self, file_path):
        self.file_path = file_path
        self.parse_list = []
        self.counter = 0
        self.flag = 1

    def set_img_info(self):
        img_file_pointer = open(self.file_path,'rb')
        pointer = 0
        start_offset_2byte = img_file_pointer.read(2)
        self.counter +=2
        # pointer += 2
        sig = struct.unpack('>H', start_offset_2byte)[0]
        if (hex(sig) == '0xffd8'):
            print("This File is JPEG : 0x%x" %(self.counter))  
            while(True):
                try :
                    if (self.flag):
                        read_2byte = img_file_pointer.read(2)
                        self.counter +=2
                        if (not read_2byte):
                            break
                        sig = struct.unpack('>H', read_2byte)[0]

                        for key, value in jpeg_marker.items():
                            if (hex(sig) == key):
                                if (key != '0xffda'):
                                    read_2byte = img_file_pointer.read(2)
                                    size = struct.unpack('>H', read_2byte)[0]
                                    data = img_file_pointer.read(size-2)
                                    self.parse_list.append([key, value, self.counter-2])
                                    self.print_marker(key, value)
                                    self.counter +=size
                                    break
                                elif (key == '0xffda'):
                                    self.parse_list.append([key, value, self.counter-2])
                                    self.print_marker(key, value)
                                    self.flag = 0
                                    break
                    elif (not self.flag):
                        read_1byte = img_file_pointer.read(1)
                        self.counter +=1
                        if (not read_1byte):
                            break
                        sig = struct.unpack('>B', read_1byte)[0]
                        if (hex(sig) == '0xff'):
                            read_1byte = img_file_pointer.read(1)
                            self.counter +=1
                            sig = struct.unpack('>B', read_1byte)[0]
                            if (hex(sig) == '0xd9'):
                                self.parse_list.append([key, value, self.counter-2])
                                self.print_marker(key, value)
                                print ("[*] JPEG File Compile Finshed.")
                                break
                except Exception as e :
                        print (e)
                        break
        img_file_pointer.close()
    
    def print_marker(self, key, value):
        if (self.flag):
            print ("[*] Find Info [*]")
            print ("[-] Mark : %s" %(key))
            print ("[-] offset : 0x%x\n" %(self.counter-2))
        elif (not self.flag) : 
            print ("[*] Find Info [*]")
            print ("[-] Mark : 0xffd9")
            print ("[-] offset : 0x%x\n" %(self.counter-2))

    def get_img_info(self):
        #TODO setting This Section
        for par_li in self.parse_list :
            print (par_li)

def help():
	print ("[-i][--input=] is input folder")
	print ("[-o][--output=] is input folder")

def work(input_path, output_path):
# 이미지 파일 찾기
    file_list = os.listdir(input_path)
    print (file_list)
    for file in file_list:
        ext = file.split(".")[-1]
        if (ext == 'jpg' or ext == 'jpeg'):
        
            print (input_path + '\\'+file)
            file_path = input_path + '\\'+file
            
            jpegParser = JpegParser(file_path)
            jpegParser.set_img_info()
            jpegParser.get_img_info()
       
		
def main():
    try:
    # 여기서 입력을 인자를 받는 파라미터는 단일문자일 경우 ':' 긴문자일경우 '='을끝에 붙여주면됨
        opts, args = getopt.getopt(sys.argv[1:],"i:f:o",["input=","help","output="])
    
    except getopt.GetoptError as err:
        print (str(err))
        help()
        sys.exit(1)

    proxy_option = 0
    input_img_path = None
    out_img_path = None
    
    if opts == [] :
        #noOption()
        help()
        sys.exit(1)

    for opt,arg in opts:

        if (opt == '-i' or opt =='--input'):
            input_img_path = arg
        elif ( opt == "-h") or ( opt == "--help"):
            help()
            sys.exit(1)
    work(input_img_path, out_img_path)

if __name__ == "__main__":
    main()