# CCG => Constituencies

Lookup conversion script to work out which Westminster Parliamentary Constituencies are contained within which NHS Clinical Commissioning Groups. Uses ONS lookup tables to carry out the lookup in a three step process:

1. Lookup which Output Areas (OA) are contained in each Clinical Commissioning Group (CCG)
2. Lookup which Westminster Parliamentary Constituency (WPC) covers each OA
3. Lookup which WPCs are contained in each CCG, based on the OAs covered by each

Created to provide an answer to a tweet by @JoeReddington: https://twitter.com/joereddington/status/511105946710716416