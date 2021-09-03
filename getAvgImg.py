from faceAvg import *

 # Dimensions of output image
w = 600
h = 600

def avgVector(path):
    """
    Return Avg Image using openCV vector (Numpy)
    """
    allPoints, images = getData(path)

    eyecornerDst = [ (np.int(0.3 * w ), np.int(h / 3)), (np.int(0.7 * w ), np.int(h / 3)) ]
    
    imagesNorm = []
    pointsNorm = []
    
    # Add boundary points for delaunay triangulation
    boundaryPts = np.array([(0,0), (w/2,0), (w-1,0), (w-1,h/2), ( w-1, h-1 ), ( w/2, h-1 ), (0, h-1), (0,h/2) ])
    
    # Initialize location of average points to 0s
    pointsAvg = np.array([(0,0)]* ( len(allPoints[0]) + len(boundaryPts) ), np.float32())
    
    n = len(allPoints[0])

    numImages = len(images)
    
    # Warp images and trasnform landmarks to output coordinate system,
    # and find average of transformed landmarks.
    
    for i in range(0, numImages):

        points1 = allPoints[i]

        # Corners of the eye in input image
        eyecornerSrc  = [ allPoints[i][36], allPoints[i][45] ] 
        
        # Compute similarity transform
        tform = similarityTransform(eyecornerSrc, eyecornerDst)
        
        # Apply similarity transformation
        img = cv2.warpAffine(images[i], tform, (w,h))

        # Apply similarity transform on points
        print(points1.shape)
        points2 = np.reshape(np.array(points1), (68,1,2))
        
        points = cv2.transform(points2, tform)
        
        points = np.float32(np.reshape(points, (68, 2)))
        
        # Append boundary points. Will be used in Delaunay Triangulation
        points = np.append(points, boundaryPts, axis=0)
        
        # Calculate location of average landmark points.
        pointsAvg = pointsAvg + points / numImages
        
        pointsNorm.append(points)
        imagesNorm.append(img)
    

    
    # Delaunay triangulation
    rect = (0, 0, w, h)
    dt = calculateDelaunayTriangles(rect, np.array(pointsAvg))

    # Output image
    output = np.zeros((h,w,3), np.float32())

    # Warp input images to average image landmarks
    for i in range(0, len(imagesNorm)) :
        img = np.zeros((h,w,3), np.float32())
        # Transform triangles one by one
        for j in range(0, len(dt)) :
            tin = []
            tout = []
            
            for k in range(0, 3) :                
                pIn = pointsNorm[i][dt[j][k]]
                pIn = constrainPoint(pIn, w, h)
                
                pOut = pointsAvg[dt[j][k]]
                pOut = constrainPoint(pOut, w, h)
                
                tin.append(pIn)
                tout.append(pOut)
            
            
            warpTriangle(imagesNorm[i], img, tin, tout)


        # Add image intensities for averaging
        output = output + img


    # Divide by numImages to get average
    output = output / numImages
    return output


def avgSave(path, savePath):
    """
    Saving Avg Image in savePath
    ---
    return True: Sucess, False: Fail
    """
    output = avgVector(path)
    cv2.imwrite(savePath, (output*255).astype(np.uint8))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--img_path", type=str, help="data directory"
    )
    parser.add_argument(
        "--output_path", type=str, help="data directory"
    )

    args = parser.parse_args()
    img_path = args.img_path
    output_path = args.output_path

    avgSave(img_path, output_path)
    