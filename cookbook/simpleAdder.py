#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import decimal,re,operator
parse_input = re.compile(r'''(?x)
                    (\d+\.?\d*)
                    \s*
                    ([-+/*])
                    $''' )
oper = { '+':operator.add,'-':operator.sub,
            '*':operator.mul, '/':operator.truediv,
    }
total = decimal.Decimal('0')
def print_total():
    try:
        tape_
    
