

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