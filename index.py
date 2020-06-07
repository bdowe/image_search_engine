from colordescriptor import ColorDescriptor
import argparse
import glob
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="Path to directory containing images to be indexed")
ap.add_argument("-i", "--index", required=True, help="Path to where computed index will be stored")
args = vars(ap.parse_args())

cd = ColorDescriptor(8, 12, 3)