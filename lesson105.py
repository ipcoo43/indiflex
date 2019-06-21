import sys
sys.float_info.dig

import fractions
fractions.Fraction(1,10)
fractions.Fraction(1,10)+3
fractions.Fraction(1,10)+3.0

import decimal
decimal.Decimal('1.00001')*3
# decimal.Decimal('1.00001')+1.0 # 에러 발생

(1-1) and True
'' and True
0 and True
False and True
True and ''
True and 1+2+3*0
True and 'False'
result=1+3-3 and '값은 0이 아닙니다.'
result

1 or ''
0 or 1*2*3*0
False or 'False'

not 0
not 1
not 'False'

1 == 1
1 == 1.0
1 == '1'
'abc' == 'abc'
1 != 1.0
1 != '1'
'abcd' != 'abc'

id(1234567)
1 == 1.0
1 is 1.0

'ab' <'zb'
ord('a')
ord('z')
