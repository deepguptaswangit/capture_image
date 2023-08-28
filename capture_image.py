# import datatime and timedelta package
from datetime import datetime, timedelta
# import opencv, argparse and time package
import cv2, argparse, time
# Import mediapipe package
import mediapipe as mp
# import os
import os


# @author: Deep Gupta
# @Date  : 28/08/2023


# Create a class to Capture Image by source camera
class CaptureImage:
    # capture images from source camera and save it to directory
    def capture_image(self, time_till, image_path):
        """ calculate an end time to capture the images,
        it needs two parameters. 1: input_time: for how
        many times this script has to run 2: a path where
        images need to be stored
        """

        new_time = (datetime.now() + timedelta(seconds=int(time_till))).strftime("%H:%M:%S")

        count = 0

        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose()
        mp_draw = mp.solutions.drawing_utils

        cap = cv2.VideoCapture(0)

        while True:
            # full_time is using to add hour_minute_second of system in image file name
            full_time = "_".join((str(datetime.now().hour), str(datetime.now().minute),
                                  str(datetime.now().second)))
            suffix = '.jpg'
            base_filename = "image_" + full_time
            file_name = os.path.join(image_path, base_filename + suffix)
            # print(img_full_name)
            count = count + 1
            if datetime.now().strftime("%H:%M:%S") == new_time:
                print("Completed")
                break
            _, img = cap.read()
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = pose.process(img_rgb)
            # print(results.pose_landmarks)
            if results.pose_landmarks:
                mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                for _, lm in enumerate(results.pose_landmarks.landmark):
                    h, w, c = img.shape
                    # print(lm)
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
            cv2.imshow("Image", img)
            cv2.imwrite(filename=file_name, img=img)
            cv2.waitKey(1)
            time.sleep(1)


if __name__ == '__main__':
    # Give below parameters while calling the script
    par = argparse.ArgumentParser(description='Capture Images.')
    par.add_argument('-S', '--seconds', default=None, help='Please enter time in seconds')
    par.add_argument('-M', '--minutes', default=None, help='Please enter time in minutes')
    par.add_argument('-H', '--hours', default=None, help='Please enter time in hours')
    par.add_argument('-P', '--path', default=None, help='Enter The Path To Store the Image')
    args = par.parse_args()
    seconds = args.seconds
    minutes = args.minutes
    hours = args.hours
    path = args.path
    INPUT_TIME = None
    FLAG = True

    if seconds is not None and minutes is not None:
        print("Please enter seconds or minutes only")
        FLAG = False
    elif hours is not None and minutes is not None:
        print("Please enter hours or minutes only")
        FLAG = False
    elif hours is not None and seconds is not None:
        print("Please enter hours or seconds only")
        FLAG = False

    if seconds is not None:
        INPUT_TIME = seconds
    elif minutes is not None:
        INPUT_TIME = minutes
    elif hours is not None:
        INPUT_TIME = hours

    if INPUT_TIME is None or path is None:
        print("Please Give Time and Path in Argument")
        FLAG = False

    # Check whether the specified path exists or not
    is_exist = os.path.exists(path)
    if not is_exist:
        # Create a new directory because it does not exist
        os.makedirs(path)
        print("The new directory is created!")

    if FLAG:
        # creating PoseEstimation class object
        obj = CaptureImage()
        # calling function to start capturing the images
        obj.capture_image(INPUT_TIME, path)
