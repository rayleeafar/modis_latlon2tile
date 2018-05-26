import numpy as np
from shapely.geometry import Polygon,Point
import os
'''
Get Modis tile from lat long
only use sn_bound_10deg.txt will get multi tiles,but some are not correct
so,add sn_gring_10deg.txt to improve correctness
'''
class Modis2tile():

    def __init__(self):
        '''
        reference:
            https://modis-land.gsfc.nasa.gov/MODLAND_grid.html
            https://landweb.modaps.eosdis.nasa.gov/cgi-bin/developer/tilemap.cgi
        '''
        relative_dir = os.path.split(os.path.abs_file_path(__file__))[0]
        sn_bound_name = "sn_bound_10deg.txt"
        sn_gring_name = "sn_gring_10deg.txt" 
        self.data = np.genfromtxt(os.path.join(relative_dir, sn_bound_name),skip_header = 7,skip_footer = 2)
        self.data_polygon = np.genfromtxt(os.path.join(relative_dir, sn_gring_name),skip_header = 7,skip_footer = 2)
        self.len = len(self.data)

    def latlon2tile(self,latlon):
        '''
          input: latlon = [lat,lon]
		  output: [h,v]
		  if erro return None
		'''
        i = 0
        lat = latlon[0]
        lon = latlon[1]
        if lat > 90 or lat < -90 or lon > 180 or lon < -180:
            print( "latlon value error!")
            return None
        ret = []
        bounds = []
        while(i < self.len):
            try:
                if lat >= self.data[i, 4] and lat <= self.data[i, 5] and lon >= self.data[i, 2] and lon <= self.data[i, 3]:
                    vert = self.data[i, 0]
                    horiz = self.data[i, 1]
                    ret.append([horiz,vert])
                    bounds.append(Polygon([[self.data_polygon[i, 2],self.data_polygon[i, 3]],[self.data_polygon[i, 4],self.data_polygon[i, 5]],[self.data_polygon[i, 6],self.data_polygon[i, 7]],[self.data_polygon[i, 8],self.data_polygon[i, 9]]]))
                i += 1
            except Exception as e:
                print(e)
                return None

        tar_point = Point(lon,lat)
        for i in range(0,len(ret)):
            if bounds[i].disjoint(tar_point):
            	continue
            return ret[i]
        return None

    def getmodistiles(self,coordinates):
        '''
        input latlon points [
                    -106.2158203125,
                    31.50362930577303
                ],
                [
                    -82.2216796875,
                    30.600093873550072
                ]]
        output modis tiles ['h12v04', 'h09v05', 'h09v04', 'h10v04']
        '''
        lon_list = [x[0] for x in coordinates]
        lat_list = [x[1] for x in coordinates]

        left,top = min(lon_list),max(lat_list)
        right,bottom = max(lon_list),min(lat_list)

        ret = []
 
        while top > bottom:
            fleft = left
            while fleft < right:
                tmp = self.latlon2tile([top,fleft])
                ret.append(tmp)
                fleft = fleft + 4.9
            top = top - 4.9
        # print(ret)
        result = ["h"+str(int(x[0])).zfill(2)+"v"+str(int(x[1])).zfill(2) for x in ret]
        return list(set(result))

if __name__ == '__main__':
	lat = 47.015
	lon = -95.0
	mt = Modis2tile()
	print(mt.latlon2tile((lat, lon)))
	print(mt.getmodistiles([[
                    -106.2158203125,
                    31.50362930577303
                ],
                [
                    -82.2216796875,
                    30.600093873550072
                ]]))


