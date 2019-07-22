# Four-Point-Invoice-Transform-with-OpenCV

This code is inspired from <a href="https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/">[4 Point OpenCV getPerspective Transform Example]</a>

I have customized the code of <a href="https://twitter.com/PyImageSearch">Adrian</a> to find <b>4 points</b> of document or rectangle dynamically. Here i have added <I>findLargestCountours</I> and <I>convert_object</I>, where convert_object is our driver method which actually doing image processing and getting all 4 point rectangles from image. After getting all 4 point rectangle list <I>findLargestCountours<I> method finding  largest countour in list.

## Run it ##
Create a virtual environment and install dependencies with `make init`
before running the examples.

### Sample2 ###

Run `python four_point_object_extractor.py sample2/original.png`

<Table>
    <tr>
        <th>Original Image</th>
        <th>Edge Detection</th>
        <th>Warped Image</th>
    </tr>
    <tr>
        <td><img src="https://raw.githubusercontent.com/FrancescElies/Four-Point-Invoice-Transform-with-OpenCV/master/sample2/original.png" alt="original" width="400" height="500" align="middle"/></td>
        <td><img src="https://raw.githubusercontent.com/FrancescElies/Four-Point-Invoice-Transform-with-OpenCV/master/sample2/screen.png" alt="Screen" width="400" height="500" align="middle"/></td>
        <td><img src="https://raw.githubusercontent.com/FrancescElies/Four-Point-Invoice-Transform-with-OpenCV/master/sample2/original-warped.png" alt="Warped" width="400" height="500" align="middle"/></td>
    </tr>
</Table>

### Sample3 ###
Run `python four_point_object_extractor.py sample3/original.png`

<Table>
    <tr>
        <th>Original Image</th>
        <th>Edge Detection</th>
        <th>Warped Image</th>
    </tr>
     <tr>
        <td><img src="https://raw.githubusercontent.com/FrancescElies/Four-Point-Invoice-Transform-with-OpenCV/master/sample3/original.png" alt="original" width="400" height="500" align="middle"/></td>
        <td><img src="https://raw.githubusercontent.com/FrancescElies/Four-Point-Invoice-Transform-with-OpenCV/master/sample3/screen.png" alt="Screen" width="400" height="500" align="middle"/></td>
        <td><img src="https://raw.githubusercontent.com/FrancescElies/Four-Point-Invoice-Transform-with-OpenCV/master/sample3/original-warped.png" alt="Warped" width="400" height="500" align="middle"/></td>
    </tr>
</Table>
