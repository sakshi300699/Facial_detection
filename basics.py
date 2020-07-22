import cv2

img1 = cv2.imread("BFS.png",0)
# cv2.imshow("Legend", img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

resized = cv2.resize(img1, (int(img1.shape[1]/2),int(img1.shape[0]/2)))
cv2.imshow("Legend", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(img1)
