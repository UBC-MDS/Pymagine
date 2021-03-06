import os
import pytest

import matplotlib.pyplot as plt
from skimage.color import rgb2gray

from pymagine import edge_detection as ed

fname = os.path.join(
    os.path.dirname(__file__),
    '../tests/imgs/coronado_beach.jpeg')
bad_ftype = 'imgs/coronado_beach.csv'
url_fname = 'https://upload.wikimedia.org/wikipedia/Python-logo-notext.svg'


def test_inputs():
    """
    Runs tests to ensure edge_detection function is working properly.
    """
    with pytest.raises(TypeError):
        ed.edge_detection(True)  # Not a string for the file path
    with pytest.raises(TypeError):
        ed.edge_detection(bad_ftype)  # Filetype is not image
    with pytest.raises(TypeError):
        ed.edge_detection(url_fname)  # Filepath can't be URL
    # Invalid output file type
    with pytest.raises(TypeError):
        ed.edge_detection(fname, file_name=bad_ftype)


def test_outputs():
    """
    Applies tests to the function output
    """
    img = plt.imread(fname)
    test_array = rgb2gray(img)
    # verify output image is the same dimensions as the input image
    returned_arr_edge_detection = ed.edge_detection(fname)

    assert returned_arr_edge_detection.shape == test_array.shape
