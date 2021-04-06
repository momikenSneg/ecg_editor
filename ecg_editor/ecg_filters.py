import cv2
import numpy as np
from matplotlib import pyplot as plt
import array
import base64

path = r'D:\4.jpg'
cut_path = r'C:\Users\Ekaterina\PycharmProjects\web_editor\ecg_editor\static\ecg_editor\img\2.jpg'
save_path = r'D:\l-1.jpg'
len_of_point = 5


def cutImage(image, x_start, y_start, x_end, y_end):
    print(x_start, y_start, x_end, y_end)
    print("ХУЙ")
    crop_img = image[int(y_start):int(y_end), int(x_start):int(x_end)]
    # cv2.imshow("cropped", crop_img)
    # cv2.waitKey(0)
    return crop_img


def rotateImage(image):
    return image


def translateCoordinates(rot_image, vector_of_points):
    return vector_of_points


def getSignal(image):
    return image


def selectGrid(image):
    return image


def selectS(signal, R):
    S = []
    s1 = selectOneS(signal, R[0])
    s2 = selectOneS(signal, R[1])
    S.append(s1)
    S.append(s2)
    return S


def selectOneS(signal, one_r):
    s = []
    i = one_r[1] + 1
    while i < len(signal):
        if signal[i][0] >= signal[i + 1][0] and signal[i][0] >= signal[i + 2][0]:
            s = signal[i]
            break
        i = i + 1
    return s


def selectQ(signal, R):
    Q = []
    q1 = selectOneQ(signal, R[0])
    q2 = selectOneQ(signal, R[1])
    Q.append(q1)
    Q.append(q2)
    # if q1[1] > q2[1]:
    #     Q.append(q2)
    #     Q.append(q1)
    # else:
    #     Q.append(q1)
    #     Q.append(q2)
    return Q


def selectOneQ(signal, one_r):
    q = []
    i = one_r[1] - 1
    while i > 1:
        if signal[i][0] >= signal[i - 1][0] and signal[i][0] >= signal[i - 2][0]:
            q = signal[i]
            break
        i = i - 1
    return q


def selectR(signal):
    local_maxima = []
    R = []
    for i in range(1, len(signal) - 1):
        if signal[i][0] < signal[i - 1][0] and signal[i][0] < signal[i + 1][0]:
            local_maxima.append(signal[i])

    max1 = max2 = [500, 500]
    for i in range(0, len(signal)):
        if signal[i][0] < max1[0]:
            max1 = signal[i]
    for i in range(0, max1[1] - 5):
        if signal[i][0] < max2[0]:
            max2 = signal[i]
    for i in range(max1[1] + 5, len(signal)):
        if signal[i][0] < max2[0]:
            max2 = signal[i]
    if max1[1] > max2[1]:
        R.append(max2)
        R.append(max1)
    else:
        R.append(max1)
        R.append(max2)
    # waits for user to press any key
    # (this is necessary to avoid Python kernel form crashing)
    cv2.waitKey(0)
    return R


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

    # print(len(signal_image), len(signal_image[0]))
    # for i in range(0, len(signal_image[0])):
    #     for j in range(0, len(signal_image)):
    #         if signal_image[j][i] == 0:
    #             signal.append([i, j])
    # cv2.imwrite(save_path, signal_image)
    return one_point_signal


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


def getPixelsSignal(image, color, delta, threshold):
    thr_image = selectSignal(image, color, delta, threshold)
    one_point_signal = getPixels(thr_image)
    i = 0
    while one_point_signal[i][0] == 0:
        one_point_signal[i][0] = one_point_signal[len(one_point_signal) - 1][0]
        i = i + 1
    for i in range(1, len(one_point_signal)):
        if one_point_signal[i][0] == 0:
            one_point_signal[i][0] = one_point_signal[i - 1][0]
    return one_point_signal


def selectQRS(src_signal):
    N = 2   # ширина окна
    M = 8
    signal_image = np.ones((200, len(src_signal), 1), np.uint8) * 255
    g_n = []
    for i in range(1, len(src_signal)):
        y = 0
        for j in range(1, N):
            y += (abs(src_signal[i - j + 1][0] - src_signal[i - j][0]) ** 2) * (N - j + 1)
        g_n.append([y, i])

    g = []
    for i in range(1, len(src_signal) - 1):
        y = 0
        for j in range(0, M - 1):
            y += g_n[i - j][0]
        y = round(y / M)
        g.append([y, i])

    gg = []
    for i in range(1, len(g) - 1):
        y = 0
        for j in range(0, M - 1):
            y += g[i - j][0]
        y = round(y / M)
        gg.append([y, i])

    prev_point = src_signal[0]
    for i in range(1, len(src_signal)):
        if src_signal[i][0] == 0:
            src_signal[i][0] = src_signal[i - 1][0]
        cur_point = src_signal[i]
        cv2.line(signal_image, (prev_point[1], prev_point[0]), (cur_point[1], cur_point[0]), 0, 1)
        prev_point = cur_point

    lenn = maxPointValue(g)
    signal_image_g = np.ones((lenn[0], len(src_signal), 1), np.uint8) * 255
    lenn = maxPointValue(g_n)
    signal_image_gn = np.ones((lenn[0], len(src_signal), 1), np.uint8) * 255

    prev_point = g_n[0]
    for i in range(1, len(g_n)):
        if g_n[i][0] == 0:
            g_n[i][0] = g_n[i - 1][0]
        cur_point = g_n[i]
        cv2.line(signal_image_gn, (prev_point[1], prev_point[0]), (cur_point[1], cur_point[0]), 0, 1)
        prev_point = cur_point

    prev_point = gg[0]
    for i in range(1, len(gg)):
        if gg[i][0] == 0:
            gg[i][0] = gg[i - 1][0]
        cur_point = gg[i]
        cv2.line(signal_image_g, (prev_point[1], prev_point[0]), (cur_point[1], cur_point[0]), 0, 1)
        prev_point = cur_point

    print(maxPointValue(gg))
    print(maxPointValue(src_signal))
    cv2.imshow("src", signal_image)
    cv2.imshow("g_n", signal_image_gn)
    cv2.imshow("g", signal_image_g)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    image = cv2.imread(path)
    color = 'r'
    threshold = 175
    delta = 2
    thr_image = selectSignal(image, color, delta, threshold)
    # testImageShow(thr_image)
    one_point_signal = getPixels(thr_image)
    # testImageShow(signal_image)

    signal_image = np.ones((len(thr_image), len(thr_image[0]), 1), np.uint8) * 255
    i = 0
    while one_point_signal[i][0] == 0:
        one_point_signal[i][0] = one_point_signal[len(one_point_signal) - 1][0]
        i = i + 1
    prev_point = one_point_signal[0]
    for i in range(1, len(one_point_signal)):
        if one_point_signal[i][0] == 0:
            one_point_signal[i][0] = one_point_signal[i-1][0]
        cur_point = one_point_signal[i]
        # print(one_point_signal[i])
        cv2.line(signal_image, (prev_point[1], prev_point[0]), (cur_point[1], cur_point[0]), 0, 1)
        prev_point = cur_point
        # signal_image[one_point_avg, point[1]] = 0
        # signal_image[one_point_avg + 10, point[1]] = 0
    R = selectR(one_point_signal)
    Q = selectQ(one_point_signal, R)
    S = selectS(one_point_signal, R)

    cv2.imwrite(save_path, signal_image)
    cv2.line(signal_image, (R[0][1], R[0][0]), (R[0][1], 0), 0, 1)
    cv2.line(signal_image, (Q[0][1], Q[0][0]), (Q[0][1], 0), 0, 1)
    cv2.line(signal_image, (S[0][1], S[0][0]), (S[0][1], 0), 0, 1)
    cv2.line(signal_image, (R[1][1], R[1][0]), (R[1][1], 0), 0, 1)
    cv2.line(signal_image, (Q[1][1], Q[1][0]), (Q[1][1], 0), 0, 1)
    cv2.line(signal_image, (S[1][1], S[1][0]), (S[1][1], 0), 0, 1)
    testImageShow(signal_image)


def test():
    image_cut = cv2.imread(path)
    signal = getPixelsSignal(image_cut, 'red', 2, 175)
    selectQRS(signal)


def from_usual_image_to_opencv_image():
    with open(cut_path, mode='rb') as file:
        img = file.read()
        nparr = np.frombuffer(img, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        testImageShow(img_np)


def maxPointValue(arr):
    maximum = [0, 0]
    for point in arr:
        if maximum[0] < point[0]:
            maximum = point
    return maximum


def minPointValue(arr):
    minimum = arr[0]
    for point in arr:
        if minimum[0] > point[0]:
            minimum = point
    return minimum


if __name__ == "__main__":
    test()
