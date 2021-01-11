# image-to-scan

If you have an image of a document and you would like to crop
everything outside the document and correct the angle from which the
photo was taken, in that case this command line tool might be for you.


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
- Download an executable for windows, linux or macos from the [release page](https://github.com/FrancescElies/image-to-scan/releases)

`image-to-scan` depends on `opencv` and `numpy` which together will take around `200MiB`

If installed with `pip` or `pipx` you should be able to call `image-to-scan` from the command line.

## Run it ##

Run `image-to-scan tests/samples/02/original.jpg`

<Table>
    <tr>
        <th>Original Image</th>
        <th>Output Image</th>
    </tr>
    <tr>
        <td><img src="https://raw.githubusercontent.com/FrancescElies/image-to-scan/master/tests/samples/02/original.jpg" alt="original" width="400" height="500" align="middle"/></td>
        <td><img src="https://raw.githubusercontent.com/FrancescElies/image-to-scan/master/tests/samples/02/original-scanned.jpg" alt="Warped" width="400" height="500" align="middle"/></td>
    </tr>
    <tr>
        <td><code>tests/samples/02/original.jpg</code></td>
        <td><code>tests/samples/02/original-scanned.jpg</code></td>
    </tr>
</Table>
