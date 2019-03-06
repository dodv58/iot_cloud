import cv2
import sys
import matplotlib.pyplot as plt

def dhash(img, hashSize=8):
    resized = cv2.resize(img, (hashSize + 1, hashSize))
    #print resized
    diff = resized[:, 1:] > resized[:, :-1]
    return diff

def img_compare(img1, img2):
    hashed1 = dhash(img1, 128)
    hashed2 = dhash(img2, 128)
    count = 0
    for i in range(len(hashed1)):
        for j in range(len(hashed1[i])):
            if hashed1[i][j] == hashed2[i][j]:
                count += 1
    print count*1.0/(len(hashed1)*len(hashed1[0]))
    return 1 if count*1.0/(len(hashed1)*len(hashed1[0])) > 0.8 else 0 

if __name__ == "__main__":
    #img_compare(img1, img2)
    img1 = cv2.imread(sys.argv[1])
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    img2 = cv2.imread(sys.argv[2])
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    print img_compare(img1, img2)
