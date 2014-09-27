# CCG => Constituencies

Lookup conversion script to work out which Westminster Parliamentary Constituencies are contained within which NHS Clinical Commissioning Groups. Uses ONS lookup tables to carry out the lookup in a three step process:

1. Lookup which Output Areas (OA) are contained in each Clinical Commissioning Group (CCG)
2. Lookup which Westminster Parliamentary Constituency (WPC) covers each OA
3. Lookup which WPCs are contained in each CCG, based on the OAs covered by each

Created to provide an answer to a tweet by @JoeReddington: https://twitter.com/joereddington/status/511105946710716416

Uses data from https://geoportal.statistics.gov.uk/geoportal/catalog/search/browse/browse.page

----

Modified version includes 

PCT => Constituencies  

pctlookup uses files from OS OpenData http://parlvid.mysociety.org/os/ to work out which of the (now defunct) Primary Care Trusts would have been in which (modern) constituencies. pctInput.csv was created by removing all put the pct and constituency columns from the postcode database and then doing a unique sort. The relevent commands were: 

 cut -d , -f 18 -f 22  ONSPD_MAY_2014_UK.csv > pctCon.txt
 vim pctCon.txt 
 wc pctCon.txt
 sort -u pctCon.txt > 



