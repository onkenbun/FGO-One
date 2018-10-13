# combine some common used function from cv2

import cv2
import numpy as np


def location(sh, tmp, thd):
    img = cv2.imread(sh, 0)
    template = cv2.imread(tmp, 0)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    threshold = thd
    pos = []

    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        pos.append(pt)

    return pos


def position(sh, tmp, thd):
    res = cv2.matchTemplate(sh, tmp, cv2.TM_CCOEFF_NORMED)
    pos = []
    loc = np.where(res >= thd)
    for pt in zip(*loc[::-1]):
        pos.append(pt)
    return pos


def check(sh, tmp, thd):
    img = cv2.imread(sh, 0)
    template = cv2.imread(tmp, 0)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    threshold = thd

    if (res >= threshold).any():
        return 1


def analyze(sh, tmp, thd):
    res = cv2.matchTemplate(sh, tmp, cv2.TM_CCOEFF_NORMED)
    if (res >= thd).any():
        return 1
