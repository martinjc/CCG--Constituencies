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
#

import csv
from collections import defaultdict

data = {}

# extract information about clinical commissioning groups
# data from https://geoportal.statistics.gov.uk/geoportal/catalog/search/browse/browse.page
# https://geoportal.statistics.gov.uk/geoportal/catalog/search/resource/details.page?uuid=%7B15C3A07F-F5E1-4CE8-9CFD-24B3589C725B%7D
# Contains National Statistics data © Crown copyright and database right 2014
with open('OA11_CCG13_NHSAT_NHSCR_EN_LU.csv', 'r') as oa_to_cgc_file:
    reader = csv.DictReader(oa_to_cgc_file)
    for row in reader:
        if not data.get(row['CCG13CD']):
            data[row['CCG13CD']] = {'CCG13CD': row['CCG13CD'], 'CCG13NM': row['CCG13NM'], 'PCON11CD list': set(), 'PCON11NM list': set(), 'OA11CD list': set(),}
        data[row['CCG13CD']]['OA11CD list'].add(row['OA11CD'])


# extract information for output area to constituency lookup
oas = {}
pcon_nm = {}

# data from https://geoportal.statistics.gov.uk/geoportal/catalog/search/browse/browse.page
# https://geoportal.statistics.gov.uk/geoportal/catalog/search/resource/details.page?uuid=%7B441E0CBF-1421-4BF5-BBC9-5B7C0EA0FE44%7D
# Contains National Statistics data © Crown copyright and database right 2014
with open('OA11_PCON11_EER11_EW_LU.csv', 'r') as oa_to_pcon_file:
    reader = csv.DictReader(oa_to_pcon_file)
    for row in reader:
        oas[row['OA11CD']] = row['PCON11CD']
        pcon_nm[row['PCON11CD']] = row['PCON11NM']


# go through all the ccgs and lookup pcons from oas
for ccg, d in data.iteritems():

    for oa in d['OA11CD list']:
        d['PCON11CD list'].add(oas[oa])
        d['PCON11NM list'].add(pcon_nm[oas[oa]])

    del d['OA11CD list']

for d in data.values():

    d['PCON11CD list'] = ';'.join(d['PCON11CD list'])
    d['PCON11NM list'] = ';'.join(d['PCON11NM list'])

with open('output.csv', 'w') as out_file:
    writer = csv.DictWriter(out_file, ['CCG13CD', 'CCG13NM', 'PCON11CD list', 'PCON11NM list'])
    writer.writeheader()
    writer.writerows(data.values())

