#!/usr/bin/env python3
"""Performs pooling on images"""
import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """
    Performs pooling on images

    images is a numpy.ndarray with shape (m, h, w, c) containing
        multiple images
        m is the number of images
        h is the height in pixels of the images
        w is the width in pixels of the images
        c is the number of channels in the image
    kernel_shape is a tuple of (kh, kw) containing the kernel shape
        for the pooling
        kh is the height of the kernel
        kw is the width of the kernel
    stride is a tuple of (sh, sw)
        sh is the stride for the height of the image
        sw is the stride for the width of the image
    mode indicates the type of pooling
        max indicates max pooling
        avg indicates average pooling

    Returns: a numpy.ndarray containing the pooled images
    """
    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    oh = (h - kh) // sh + 1
    ow = (w - kw) // sw + 1

    output = np.zeros((m, oh, ow, c))

    for i in range(oh):
        for j in range(ow):
            y = i * sh
            x = j * sw
            region = images[:, y:y + kh, x:x + kw, :]
            if mode == 'max':
                output[:, i, j, :] = np.max(region, axis=(1, 2))
            elif mode == 'avg':
                output[:, i, j, :] = np.mean(region, axis=(1, 2))

    return output