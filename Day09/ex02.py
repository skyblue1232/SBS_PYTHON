
from config import _converter
import converter as cvt

# 파일일부(모듈),함수()
#
m1 = cvt.kilometer_to_miles(100)

# import converter as cvt
# as (별명) : 
m2 = cvt.kilometer_to_miles(200)

# 파일(모듈) 내부의 함수를 포함
from converter import kilometer_to_miles
from converter import gram_to_pound
from converter import kilometer_to_miles, gram_to_pound

# converter 모듈 안의 모든 함수를 포함
# * : 모든 항목
from converter import *