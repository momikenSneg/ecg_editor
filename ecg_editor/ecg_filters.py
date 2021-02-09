import cv2
import numpy as np
from matplotlib import pyplot as plt
import array

path = r'D:\10.jpg'
save_path = r'D:\l-10.jpg'
len_of_point = 5


def rotateImage(image):
    return image


def translateCoordinates(rot_image, vector_of_points):
    return vector_of_points


def getSignal(image):
    return image


def selectGrid(image):
    return image


def getPixels(thr_image):
    signal = []
    bad_signal = []
    signal_image = np.ones((len(thr_image), len(thr_image[0]), 1), np.uint8) * 255
    for i in range(0, len(thr_image[0])):
        # thr_image[100][i] = 0                    # горизонтальная линия
        points = []
        # for j in range(0, len(thr_image)):
        j = 0
        while j < len(thr_image):
            if thr_image[j][i] == 0:
                point = []
                while thr_image[j][i] == 0 and j < len(thr_image) - 1:
                    point.append([j, i])
                    j = j + 1
                points.append(point)
            j = j + 1
        bad_signal.append(points)

    one_point_signal = []
    for i in range(0, len(bad_signal)):
        if len(bad_signal[i]) == 1:
            if len(bad_signal[i][0]) < len_of_point:
                avg = 0
                for pix in bad_signal[i][0]:
                    avg = avg + pix[0]
                avg = avg / len(bad_signal[i][0])
                one_point_signal.append([round(avg), i])
            else:
                one_point_signal.append([0, i])
                # good_signal.append([bad_signal[i][0][len(bad_signal[i][0]) - 1][0], i])  верхняя точка в длинной точке
        else:
            one_point_signal.append([0, i])

    one_point_avg = 0
    one_point_count = 0
    for point in one_point_signal:
        if point[0] != 0:
            one_point_count = one_point_count + 1
            one_point_avg = one_point_avg + point[0]
    one_point_avg = round(one_point_avg / one_point_count)

    for i in range(0, len(bad_signal)):
        if len(bad_signal[i]) == 1:
            up = 0
            if len(bad_signal[i][0]) >= len_of_point:
                for pix in bad_signal[i][0]:
                    if pix[0] > one_point_avg:
                        up = up + 1
                if up == 0:
                    one_point_signal[i] = [bad_signal[i][0][up][0], i]
                else:
                    one_point_signal[i] = [bad_signal[i][0][up - 1][0], i]

    # for i in range(0, len(one_point_signal):
    #     if
    #
    for i in range(1, len(one_point_signal)):
        if one_point_signal[i][0] == 0:
            continue
        cur_point = one_point_signal[i]
        cv2.line(signal_image, (prev_point[1], prev_point[0]), (cur_point[1], cur_point[0]), 0, 1)
        prev_point = cur_point
        # signal_image[one_point_avg, point[1]] = 0
        # signal_image[one_point_avg + 10, point[1]] = 0

    cv2.imwrite(save_path, signal_image)
    return signal_image


def selectSignal(image, color, delta, threshold):  # Метод выделяет сигнал на изображении
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    local_maxima = []
    for i in range(1, 255):
        if hist[i] > hist[i - 1] and hist[i] > hist[i + 1]:
            local_maxima.append([hist[i], i])
    max1 = max2 = 0
    for i in range(0, len(local_maxima)):
        if local_maxima[i][0] > max2:
            max1 = max2
            max2 = local_maxima[i][0]
    thr1 = thr2 = 0
    for i in range(1, 255):
        if hist[i] == max1:
            thr1 = i
        if hist[i] == max2:
            thr2 = i

    # print(thr1, thr2)
    for x in range(0, len(image)):
        for y in range(0, len(image[0])):
            # if thr1 - delta < image[x][y][2] < thr1 + delta:
            if image[x][y][2] > thr1:
                # print(image[x][y][2])
                image[x][y] = [255, 255, 255]

    blur_image = cv2.GaussianBlur(image, (3, 3), 0)
    gray_image = cv2.cvtColor(blur_image, cv2.COLOR_BGR2GRAY)
    ret, thr_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)

    # for i in range(100, 150):
    #     thr_image[i][100] = 0

    # print()
    # plt.plot(hist, color=color)
    # plt.xlim([0, 256])
    # plt.show()
    return thr_image


def testImageShow(image):
    # Window name in which image is displayed
    window_name = 'image'
    # Using cv2.imshow() method
    # Displaying the image
    cv2.imshow(window_name, image)

    # waits for user to press any key
    # (this is necessary to avoid Python kernel form crashing)
    cv2.waitKey(0)

    # closing all open windows
    cv2.destroyAllWindows()


def main():
    image = cv2.imread(path)
    color = 'r'
    threshold = 175
    delta = 2
    thr_image = selectSignal(image, color, delta, threshold)
    testImageShow(thr_image)
    signal_image = getPixels(thr_image)
    testImageShow(signal_image)


if __name__ == "__main__":
    main()
