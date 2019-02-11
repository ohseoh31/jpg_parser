# jpg_parser

This program parses the marker offset and marker information in the JPG image file.
</br>  
- 사용법
```  
  python main.py -i [path]
  python main.py -i img

```  

- 출력 내용
```  
  .\이미지_1.jpg
This File is JPEG : 0x2
[*] Find Info [*]
[-] Mark : 0xffe0(APP00)
[-] offset : 0x2

[*] Find Info [*]
[-] Mark : 0xffe1(APP01)
[-] offset : 0x14

[*] Find Info [*]
[-] Mark : 0xffe1(APP01)
[-] offset : 0x4f2

[*] Find Info [*]
[-] Mark : 0xffed(APP13)
[-] offset : 0xf01

[*] Find Info [*]
[-] Mark : 0xffc0(SOF00)
[-] offset : 0xf3b

[*] Find Info [*]
[-] Mark : 0xffc4(DHT)
[-] offset : 0xf4e

[*] Find Info [*]
[-] Mark : 0xffc4(DHT)
[-] offset : 0xf6f

[*] Find Info [*]
[-] Mark : 0xffc4(DHT)
[-] offset : 0x1026

[*] Find Info [*]
[-] Mark : 0xffc4(DHT)
[-] offset : 0x1047

[*] Find Info [*]
[-] Mark : 0xffdb(DQT)
[-] offset : 0x10fe

[*] Find Info [*]
[-] Mark : 0xffdb(DQT)
[-] offset : 0x1143

[*] Find Info [*]
[-] Mark : 0xffdd(DRI)
[-] offset : 0x1188

[*] Find Info [*]
[-] Mark : 0xffda(SOS)
[-] offset : 0x118e

[*] Find Info [*]
[-] Mark : 0xffda(SOS)
[-] offset : 0xca328
```  


