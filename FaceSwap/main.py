import cv2
import dlib
import numpy as np

# Load the two input images
img1 = cv2.imread('image1.jpg')
img2 = cv2.imread('image2.jpg')

# Create a face detector using dlib
detector = dlib.get_frontal_face_detector()

# Create a facial landmark detector using dlib
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Detect faces in both images
faces1 = detector(img1)
faces2 = detector(img2)

# Loop over each face in the first image
for face1 in faces1:
    # Get the facial landmarks for the current face in the first image
    landmarks1 = predictor(img1, face1)

    # Loop over each face in the second image
    for face2 in faces2:
        # Get the facial landmarks for the current face in the second image
        landmarks2 = predictor(img2, face2)

        # Compute a transformation matrix that maps the landmarks from the first face to the second face
        M = cv2.estimateAffinePartial2D(np.array(landmarks1.parts()), np.array(landmarks2.parts()))

        # Apply the transformation matrix to the first face to align it with the second face
        aligned_face1 = cv2.warpAffine(img1, M[0], (img2.shape[1], img2.shape[0]))

        # Blend the aligned face with the second face using alpha blending
        mask = np.zeros(img2.shape[:2], dtype=np.float32)
        mask = cv2.fillConvexPoly(mask, np.int32(landmarks2.parts()), 1)
        mask = cv2.GaussianBlur(mask, (11, 11), 0)
        mask_stack = np.dstack([mask] * 3)
        mask_stack = mask_stack.astype('float32') / 255.0
        face_stack = np.dstack([aligned_face1] * 3)
        blended_face = (mask_stack * face_stack) + ((1 - mask_stack) * img2)

        # Display the result
        cv2.imshow('Face Swapper', blended_face)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
