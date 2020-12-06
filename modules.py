
import cv2
from datetime import datetime


class Computer:

    class Camera:
        def __init__(self, camera_port = 0, snapshots_directory = 'snapshots'):
            self.camera_port = camera_port
            self.snapshots_directory = snapshots_directory
            self.camera = None

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
            image_filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') # example: 2020-12-04_00-05-50.jpeg
            cv2.imwrite("{0}\{1}.jpeg".format(self.snapshots_directory, image_filename) ,im)
            
            # release camera to allow use from other apps
            del(self.camera)

            return im

        def command_line(self, stuff):
            pass

    def __init__(self) -> None:
        self.camera = self.Camera(camera_port = 0)




if __name__ == '__main__': # for testing purposes 
    print('Program starting...')
    pc = Computer()
    pc.camera.capture_snapshot()






