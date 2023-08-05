import cv2

def capture_image(event, x, y, flags, param):
    global captured_image, capturing

    if event == cv2.EVENT_LBUTTONDOWN:
        capturing = False
        captured_image = frame
        cv2.imshow("Captured Image", captured_image)

def main():
    global capturing, captured_image

    # Open the default camera (0) or provide the camera's index if you have multiple cameras
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Unable to access the camera.")
        return

    capturing = True
    captured_image = None

    print("Click anywhere in the camera feed to capture an image.")
    print("Press 'q' to quit.")

    while capturing:
        # Read a frame from the camera
        ret, frame = camera.read()

        if not ret:
            print("Error: Couldn't capture a frame.")
            break

        # Display the frame in a window named "Camera Feed"
        cv2.imshow("Camera Feed", frame)

        # Set the mouse callback to capture an image on click
        cv2.setMouseCallback("Camera Feed", capture_image)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
