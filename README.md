# Four-Point-Invoice-Transform-with-OpenCV

forked from [KMKnation/Four-Point-Invoice-Transform-with-OpenCV](https://github.com/KMKnation/Four-Point-Invoice-Transform-with-OpenCV)

This code is inspired from <a href="https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/">[4 Point OpenCV getPerspective Transform Example]</a>

I have customized the code of <a href="https://twitter.com/PyImageSearch">Adrian</a> to find <b>4 points</b> of document or rectangle dynamically. Here i have added <I>findLargestCountours</I> and <I>convert_object</I>, where convert_object is our driver method which actually doing image processing and getting all 4 point rectangles from image. After getting all 4 point rectangle list <I>findLargestCountours<I> method finding  largest countour in list.

## Installation ##
`pip install image_to_scan`

## Run it ##
Before running the examples, create a virtual environment and install
dependencies with `make init`, this will also add an entry point
`image-to-scan` from which you can call the script.

Activate your virtualenv `source venv/bin/activate`.

### Sample2 ###

Run `image-to-scan tests/samples/02/original.png`

<Table>
    <tr>
        <th>Original Image</th>
        <th>Edge Detection</th>
        <th>Warped Image</th>
    </tr>
    <tr>
        <td><img src="https://raw.githubusercontent.com/FrancescElies/Four-Point-Invoice-Transform-with-OpenCV/master/tests/samples/02/original.png" alt="original" width="400" height="500" align="middle"/></td>
        <td><img src="https://raw.githubusercontent.com/FrancescElies/Four-Point-Invoice-Transform-with-OpenCV/master/tests/samples/02/screen.png" alt="Screen" width="400" height="500" align="middle"/></td>
        <td><img src="https://raw.githubusercontent.com/FrancescElies/Four-Point-Invoice-Transform-with-OpenCV/master/tests/samples/02/original-scanned.png" alt="Warped" width="400" height="500" align="middle"/></td>
    </tr>
</Table>

### Sample3 ###
Run `image-to-scan tests/samples/03/original.png`

<Table>
    <tr>
        <th>Original Image</th>
        <th>Edge Detection</th>
        <th>Warped Image</th>
    </tr>
     <tr>
        <td><img src="https://raw.githubusercontent.com/FrancescElies/Four-Point-Invoice-Transform-with-OpenCV/master/tests/samples/03/original.png" alt="original" width="400" height="500" align="middle"/></td>
        <td><img src="https://raw.githubusercontent.com/FrancescElies/Four-Point-Invoice-Transform-with-OpenCV/master/tests/samples/03/screen.png" alt="Screen" width="400" height="500" align="middle"/></td>
        <td><img src="https://raw.githubusercontent.com/FrancescElies/Four-Point-Invoice-Transform-with-OpenCV/master/tests/samples/03/original-scanned.png" alt="Warped" width="400" height="500" align="middle"/></td>
    </tr>
</Table>
