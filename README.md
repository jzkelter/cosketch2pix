# cosketch2pix

Collaboratively create a sketch and then transform it into a painterly rendering. Perfect for surrealist exquisite corpses! Read more about the project [here](https://medium.com/@gcaniglia1/computational-creativity-t-4d37a120a0bb?source=friends_link&sk=9fe31872b18151034a75ca36138976fb).

## Installation

First, download the dependencies:

* Python 2.7
* Tensorflow 1.4.1+
* OpenCV 4.1.1+
* NetLogo 6.1.1+

Next, clone the repo. In the `models` folder, extract `gart_canny_256.tar.gz` from https://github.com/memo/webcam-pix2pix-tensorflow/releases.

Open `cosketch2pix.nlogo`, go to the "Code" tab, and change the file path of `py:setup` to wherever you have python dependencies installed on your computer.

Do not change the size of the canvas, as it's currently optimized to output 256x256px images. If you do need to change it back to this optimized size, go into Model settings in NetLogo, and make the Canvas a 20x20 block with a patch size of 12.8 pixels.

## Running the Activity

Open `cosketch2pix.nlogo`, click startup, then click setup, then click go.

The HubNet Control Center window contains the server address and port number. For other users to participate, they need to download NetLogo 6.1.1+ onto their computers, and then they need to open HubNet (which is installed along with NetLogo). They can then input the server address and port number to connect to the experience.

When everyone is done drawing, the host can press the "pix2pix" button to convert the drawing into the painterly rendering, which will appear on each person's computer.

On macOS, we recommend enabling "Mouse Keys" under Accessibility settings in System Preferences. This will allow using the 'i' key to click, which makes making curved lines easier. Otherwise, one just needs to point and click to place the lines. The 't' key toggles the pen tool, allowing the user to make unconnected lines (otherwise, they connect by default). The 'y' key is undo.
