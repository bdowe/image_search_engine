from colordescriptor import ColorDescriptor
import argparse
import glob
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="Path to directory containing images to be indexed")
ap.add_argument("-i", "--index", required=True, help="Path to where computed index will be stored")
args = vars(ap.parse_args())

cd = ColorDescriptor((8, 12, 3))

output = open(args["index"], "w")

# use glob to loop over image paths
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
	# extract image ID (unique filename) from image
	imageID = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)

	# describe image and extract features
	features = cd.describe(image)

	# write features to output file
	features = [str(f) for f in features]
	output.write("%s,%s\n" % (imageID, ",".join(features)))

output.close()

