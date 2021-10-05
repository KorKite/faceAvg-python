# faceAvg-python
    It is Easy face average generator
    I modify errors when generate faces (multiple faces, no face etc)

# Codes
    getAvgImg.py 
    -->> Generator Code
    
    shape_predictor_68_face_landmarks.dat
    -->> Predictor File
    
    error_img.txt 
    -->> If there is more than 2 people in one image, program ignore such image and write log on here.

# How to use
    python3 getAvgImg.py --img_path [input files path] --output_path [output img path]

# Example
    python3 getAvgImg.py --img_path example-faces --output_path output.png

# Example Explanation
    "example-faces" folder has 63 number of images
    This python code generate average face of given images

<img src="https://github.com/KorKite/faceAvg-python/blob/main/output.png?raw=true" width="200">


## References
    Using FaceAverage from learnopencv
    https://github.com/spmallick/learnopencv/tree/master/FaceAverage

    Using Calculate Landmark of dlib
    https://velog.io/@choiiis/Python%EC%97%90%EC%84%9C-dlib%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%98%EC%97%AC-Facial-Landmark-%EA%B2%80%EC%B6%9C%ED%95%98%EC%97%AC-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC-json-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0
    
