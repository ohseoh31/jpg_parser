################################################################################
# Copyright (Python) taegyu <https://github.com/ohseoh31>                      #
# @author taegue (ohseoh31@github.com) bob7 df                                 #
# @brief  [jpg, jpeg]file marker parser code with python                       #
# using command : python -i [filename]                                         #
################################################################################

from option import Option


if __name__ == "__main__":
    
    option = Option() 
    option.get_option()
    option.do_work()
