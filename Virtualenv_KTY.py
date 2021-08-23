import cv2
import matplotlib.pyplot as plt


def main():
    imgpath = "D:\\OpenCV\\Project\\images\\misc\\misc\\4.2.07.tiff"
    img = cv2.imread(imgpath, 0)

    plt.imshow(img, cmap='gray')
    plt.title('Gray Colormap')
    plt.xticks([])
    plt.yticks([])
    plt.show()

    plt.imshow(img)
    plt.title('Default Colormap')
    plt.xticks([])
    plt.yticks([])
    plt.show()


if __name__ == "__main__":
    main()