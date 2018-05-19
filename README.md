# modis_latlon2tile
Get Modis tile from lat long

**from a point get tile hv
  
*latlon2tile(self,latlon):
    input: latlon = [lat,lon]
    output: [h,v]
    if erro return None
      
**fron a polygon get hv list  

*getmodistiles(self,coordinates):
        input latlon points [
                    -106.2158203125,
                    31.50362930577303
                ],
                [
                    -82.2216796875,
                    30.600093873550072
                ]]
        output modis tiles ['h12v04', 'h09v05', 'h09v04', 'h10v04']
