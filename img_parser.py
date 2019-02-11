
import binascii
import struct
import marker_setting 

class JpegParser:

    def __init__(self, file_path):
	'''
	    @param
		file_path : parsed img path
		parse_list : img marker info save
		counter  : marker offset
		flag : check last marker
	'''
        self.file_path = file_path
        self.parse_list = []
        self.counter = 0
        self.flag = 1

    def set_img_info(self):
	
        img_file_pointer = open(self.file_path,'rb')
        pointer = 0
        start_offset_2byte = img_file_pointer.read(2)
        self.counter +=2
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

                        for key, value in marker_setting.jpeg_marker.items():
                            if (hex(sig) == key):
                                if (key != '0xffda'):
                                    read_2byte = img_file_pointer.read(2)
                                    size = struct.unpack('>H', read_2byte)[0]
                                    data = img_file_pointer.read(size-2)
                                    self.parse_list.append([key, value, self.counter-2])
                                    self.counter +=size
                                    break
                                elif (key == '0xffda'):
                                    self.parse_list.append([key, value, self.counter-2])
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

                                break

                except Exception as e :
                        print (e)
                        break
        img_file_pointer.close()
    
    def print_marker(self, parse_info):

        print ("[*] Find Info [*]")
        print ("[-] Mark : %s(%s)" %(parse_info[0], parse_info[1]))
        print ("[-] offset : 0x%x\n" %(parse_info[2])) 

    def get_img_info(self):

        for par_li in self.parse_list :
            self.print_marker(par_li)

    def checK_endian(self):
        print("endian check")
