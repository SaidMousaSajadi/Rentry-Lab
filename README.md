# Rentry Lab

This is a project related to [Rentry.co](https://rentry.co), which makes the projects defined as code in Rentry to be easily downloaded and sent from Linux and Windows environments. This project is designed for Linux and Windows OS. For how to use them, the following educational videos are located in the following links:
## Instruction

Windows: 
1. Install Git
[Git Web Page](https://git-scm.com/downloads)
Then add the ./git/bin path to environment paths.
2. Install [Rentry Project](https://pypi.org/project/rentry/)
```
pip install rentry
```
3. Install rentrylab
```
pip install -i https://test.pypi.org/simple/ rentrylab
```

Linux: 
1. Install [Rentry Project](https://pypi.org/project/rentry/)
```
wget https://raw.githubusercontent.com/radude/rentry/master/rentry -O ./rentry && chmod +x ./rentry
```
2. Install rentrylab
```
pip3 install -i https://test.pypi.org/simple/ rentrylab
```


## Usage
**To Get File:**

To get a  code file from [rentry.co](https://pypi.org/project/rentry/), just type these two lines of code at the beginning of your file("Receive.py") and run it, your file will be updated.
```
import os ; from rentrylab import RentryLab
RentryLab.myrentry().GetFromRentry("https://rentry.co/NewPage011",os.path.join(os.path.dirname(__file__)),"Receive","python",".py")
```

**To Send File:**

To send a code file to [rentry.co](https://pypi.org/project/rentry/), just add these two lines to the end of your file("Send.py"), and run it, your file will be uploaded.
Be careful, RentryLab will not upload your last 3 lines containing the following commands:
```
import os ; from rentrylab import RentryLab
RentryLab.myrentry().SendToRentry("https://rentry.co/NewPage011",'password',os.path.join(os.path.dirname(__file__)),'Send','python','.py',['#YourHeader' , '**Python Language**'])
```

**To Create File:**

It will be added in the next version.


**Do you want to see how to use it visually???**

[windows](https://youtu.be/re4J3bZkKAI)

[Linux](https://youtu.be/z5igWHFaPVE)

[PythonAnyWhere](https://youtu.be/5iGLaaf8baU)
