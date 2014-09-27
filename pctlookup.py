#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>


#
# created by Martin Chorley - @martinjc - http://www.martinjc.com
# modified by Joe Reddington - @joereddington - http://joereddington.com

import csv
from collections import defaultdict

data = {}
# extract information about clinical commissioning groups
with open('PCO names and codes EN as at 04_11.csv', 'r') as oa_to_cgc_file:
    reader = csv.DictReader(oa_to_cgc_file)
    for row in reader:
            data[row['PCO11CD']] =  row['PCO11NM']


# extract information for output area to constituency lookup
oas = {}
pcon_nm = {}

with open('OA11_PCON11_EER11_EW_LU.csv', 'r') as oa_to_pcon_file:
    reader = csv.DictReader(oa_to_pcon_file)
    for row in reader:
        oas[row['PCON11CD']] = row['PCON11CD']
        pcon_nm[row['PCON11CD']] = row['PCON11NM']

# go through all the ccgs and lookup pcons from oas
with open('pctInput.csv', 'r') as table:
    reader = csv.DictReader(table)
    for row in reader:
	print row['PCT'], ", ", data[row['PCT']], ",", row['Parl'], ", ",  pcon_nm[row['Parl']]


