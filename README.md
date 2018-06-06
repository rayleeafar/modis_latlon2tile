# modis_latlon2tile
Get Modis tile from lat long

**a> from a point get tile hv**
  
*latlon2tile(self,latlon):*  
     
        
**b> fron a polygon get hv list**  

*getmodistiles(self,coordinates):*  
      
# use python module  
tilemap3.py _tilemap3.so   
**>>>import tilemap3
**>>>tilemap3.gethv(32.45,-102.56)
**905
**(h,v)<--->(905/100,905%100)

