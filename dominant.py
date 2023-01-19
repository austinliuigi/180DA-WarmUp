import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist

def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar

img = cv2.imread("shroomish.png")
width = img.shape[0]
height = img.shape[1]
center = (width/2, height/2)

# Get user input for portion of image
prompt = "Enter size of rect (" + str(width) + " " + str(height) + "): "
rect_size = list(map(int, input(prompt).split()))
tl = (int(center[0]-rect_size[0]/2), int(center[1]-rect_size[1]/2))
br = (int(center[0]+rect_size[0]/2), int(center[1]+rect_size[1]/2))

# Draw image with rectangle around selected region
img_rect = np.copy(img)
cv2.rectangle(img_rect, (tl[0], tl[1]), (br[0], br[1]), (0, 0, 255))
cv2.imshow("shroomish", img_rect)
cv2.waitKey(0)

# Get user input for portion of image
# prompt_tl = "Enter top-left coord (0 " + str(width) + "): "
# prompt_br = "Enter bottom-right coord (0 " + str(height) + "): "
# tl = list(map(int, input(prompt_tl).split()))
# br = list(map(int, input(prompt_br).split()))

# Draw image with rectangle around selected region
# img_rect = np.copy(img)
# cv2.rectangle(img_rect, (tl[0], tl[1]), (br[0], br[1]), (0, 0, 255))
# cv2.imshow("shroomish", img_rect)
# cv2.waitKey(0)

img_selection = img[tl[0]:br[0], tl[1]:br[1]]
img_selection = cv2.cvtColor(img_selection, cv2.COLOR_BGR2RGB)

# Convert from 2D matrix of 3-elem list to array of 3-elem list
img_selection = img_selection.reshape((img_selection.shape[0] * img_selection.shape[1], 3))
kmeans = KMeans(n_clusters=3) #cluster number
kmeans.fit(img_selection)

hist = find_histogram(kmeans)
bar = plot_colors2(hist, kmeans.cluster_centers_)

plt.axis("off")
plt.imshow(bar)
plt.show()
