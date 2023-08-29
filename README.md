# capture_image

## Install python3.11

### Note: if you want to install python only for this script
* Install virtual environment by below command

> python -m venv c:\path\to\myenv

* Now activate python virtual environment

(For windows) Run Below command in CMD window

> myenv\Script\activate.bat

(For Linux) Run Below command in CMD window

> source /path/to/venv/bin/activate

* Run the script by using below command

> python capture_image.py --seconds time --path path_to_store_image

* Ex:
> python capture_image.py --seconds 20 --path D:\capture_image\images

* Argument description.
    --seconds: For how many seconds you wanted capture the image 
    --minutes: For how many minutes you wanted capture the image 
    --hours: For how many hours you wanted capture the image
    --path: Where you wanted to save the image.
    
    Note: Please give only one argument for time(seconds, minutes or hours)
