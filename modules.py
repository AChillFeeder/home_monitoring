
import cv2
from datetime import datetime
import os


class Computer:

    class Camera:
        def __init__(self, camera_port = 0, snapshots_directory = 'snapshots'):
            self.camera_port = camera_port
            self.snapshots_directory = snapshots_directory
            self.camera = None
            self.last_picture = None

        def capture_snapshot(self, ramp_frames=30, x=1280, y=720):
            """
                Capture a snapshot and save it in the snapshots directory\n
                It is taken in HD by default (1280 x 720)
            """
            self.camera = cv2.VideoCapture(self.camera_port)

            # Set Resolution
            self.camera.set(3, x)
            self.camera.set(4, y)

            # Give camera enough time to adjust to the light
            for i in range(ramp_frames):
                temp = self.camera.read()

            retval, im = self.camera.read()

            # save the image in the specified directory
            image_filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.jpeg' 
            # example: 2020-12-04_00-05-50.jpeg
            self.last_picture = image_filename 
            cv2.imwrite("{0}\{1}".format(self.snapshots_directory, image_filename) ,im)
            
            # release camera to allow use from other apps
            del(self.camera)


    def __init__(self):
        self.camera = self.Camera(camera_port = 0)

    def execute(self, take_save_snapshot, display_last_picture, cmd_command):
        """
            Execute whatever commands the user asked for and return their completion status
        """

        # set null values in case these variables don't get values
        results = {
            "take_save_success": False,
            "last_picture_filename": False,
            "cmd_command_success": False,
        }

        if take_save_snapshot:
            try:
                self.camera.capture_snapshot()
                results["take_save_success"] = True
            except Exception as exc:
                results["take_save_success"] = False 
        
        if display_last_picture:
            results["last_picture_filename"] = False if not self.camera.last_picture else self.camera.last_picture
        
        if cmd_command:
            try:
                os.system("start cmd /k {}".format(cmd_command))  
            except Exception:
                results["cmd_command_success"] = False

        return results









