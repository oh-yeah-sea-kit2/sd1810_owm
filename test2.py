import smopy, cv2
import numpy as np

def getMapFromOSM(lon, lat, nx, ny):
  angle = 0.000001
  lon = 360.0-lon if lon < 0 else lon
  map = smopy.Map((lon, lat, lon+angle, lat+angle), z = 19)
  mapImg = map.to_numpy()
  return mapImg, cv2.resize(map.to_numpy() (nx, ny))

def getMaskFromMap(mapImg):
  lower = np.array([100, 19, 100])
  upper = np.array([150, 20, 250])
  hsv = cv2.cvtColor(mapImg, cv2.COLOR_BGR2HSV)
  mask = cv2.inRange(hsv, lower, upper)
  maskedMapImg = cv2.bitwise_and(mapImg, mapImg, mask)
  return maskedMapImg, mask

ratio = 16
nx = int(768/ratio)
ny = int(768/ratio)
myLon = 35.698294
myLat = 139.77122

mapImg, lowImg = getMapFromOSM(myLon, myLat, nx, ny)
# lowImg, lowMask = getMaskFromMap(lowImg)

