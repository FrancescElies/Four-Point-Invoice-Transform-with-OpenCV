# image-to-scan: cli tool that transforms a photo of a document to a scanned document

If you have an image of a document maybe you would like to crop
everything outside the document and correct the angle from which the
photo was taken, in that case this command line tool might help.

<details>
<summary>Notes</summary>
<pre style="display:block; font-family:monospace; margin: 1em 0; white-space: pre;">
Originally forked from <a href="https://github.com/KMKnation/Four-Point-Invoice-Transform-with-OpenCV">KMKnation/Four-Point-Invoice-Transform-with-OpenCV</a>

This code is inspired from <a href="https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/">4 Point OpenCV getPerspective Transform Example</a>
</pre>
</details>


## Installation ##
- Via [pipx](https://pipxproject.github.io/pipx/) `pipx install image_to_scan` if you want to install inside an isolated environment.
- Via pip `pip install image_to_scan` to an enviroment of your choice.

After installing it an entry point `image-to-scan` will be added.

## Run it ##

Run `image-to-scan tests/samples/02/original.jpg`

<Table>
    <tr>
        <th>Original Image</th>
        <th>Output Image</th>
    </tr>
    <tr>
        <td><img src="https://raw.githubusercontent.com/FrancescElies/Four-Point-Invoice-Transform-with-OpenCV/master/tests/samples/02/original.jpg" alt="original" width="400" height="500" align="middle"/></td>
        <td><img src="https://raw.githubusercontent.com/FrancescElies/Four-Point-Invoice-Transform-with-OpenCV/master/tests/samples/02/original-scanned.jpg" alt="Warped" width="400" height="500" align="middle"/></td>
    </tr>
</Table>

Run `image-to-scan tests/samples/03/original.jpg`

<Table>
    <tr>
        <th>Original Image</th>
        <th>Output Image</th>
    </tr>
     <tr>
        <td><img src="https://raw.githubusercontent.com/FrancescElies/Four-Point-Invoice-Transform-with-OpenCV/master/tests/samples/03/original.jpg" alt="original" width="400" height="500" align="middle"/></td>
        <td><img src="https://raw.githubusercontent.com/FrancescElies/Four-Point-Invoice-Transform-with-OpenCV/master/tests/samples/03/original-scanned.jpg" alt="Warped" width="400" height="500" align="middle"/></td>
    </tr>
</Table>
