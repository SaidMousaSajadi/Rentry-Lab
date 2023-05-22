# Rentry Lab

This is a project related to [Rentry.co](https://rentry.co), which makes the projects defined as code in Rentry to be easily downloaded and sent from Linux and Windows environments. This project is designed for Linux and Windows OS. For how to use them, the following educational videos are located in the following links:
## Instruction

Windows: 
1. Install [Git](https://git-scm.com/downloads)
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
**To Create URL:**

To create a new URL, just run the following command using RentryLab:
[Please follow the rules of rentry.co, do not spam and avoid creating unnecessary URLs.](https://rentry.co/what#rules)
```
import os ; from rentrylab import RentryLab
RentryLab.myrentry().CreateRentry("https://rentry.co/NewPage011",'password',os.path.join(os.path.dirname(__file__)),StartText='Built with RentryLab'):
```

**To Send Code:**

To send a code file to [rentry.co](https://pypi.org/project/rentry/), just add these two lines to the end of your file(`"Send.py"`), and run it, your file will be uploaded.
Be careful, RentryLab will not upload your last 3 lines containing the following commands:
```
import os ; from rentrylab import RentryLab
RentryLab.myrentry().SendToRentry("https://rentry.co/NewPage011",'password',os.path.join(os.path.dirname(__file__)),'Send','python','.py',['#YourHeader' , '**Python Language**'])
```

**To Get Codes:**

To get codes file from [rentry.co](https://pypi.org/project/rentry/), just type these two lines of code at the beginning of your file(`"Receive.py"`) and run it, your file will be updated.
This method extracts all parts of a URL containing Python codes.
```
import os ; from rentrylab import RentryLab
RentryLab.myrentry().GetFromRentry("https://rentry.co/NewPage011",os.path.join(os.path.dirname(__file__)),"Receive","python",".py")
```

**To Send Data:**

To send dictionary data, proceed as follows:
First, create an url page for data (Here `Data1`).
Then, create a dictionary or create it with your own algorithm (Here `Dict`).
Finally, send it to the generated URL.
```
import os ; from rentrylab import RentryLab
RentryLab.myrentry().CreateRentry("https://rentry.co/Data1",'password',os.path.join(os.path.dirname(__file__)),StartText='To Test Data'):
Dict = {'Headers' : ['DEPTH','BS','CALI','GR','DT','RT','PHIE'],
        'r0' : [1829.2572,12,22.0052,46.6003,117.0969,0.879,0.052045],
        'r1' : [1829.4096,12,21.9816,46.2312,'Cell','Cell','Cell'],
        'r2' : [1829.4096,12,21.9816,46.2312,'Cell','Cell','OK']}
RentryLab.myrentry().SendDataToRentry('https://rentry.co/Data1','password',os.path.join(os.path.dirname(__file__)),Dict,HeaderList=['# Data1','## Added with RentryLab'])
```

**To Get Data:**

You can get URL tables data as List of Dictionary:
```
import os ; from rentrylab import RentryLab
DictList = RentryLab.myrentry().GetDataFromRentry('https://rentry.co/Data1',os.path.join(os.path.dirname(__file__)))
# print(DictList)
```

**To Append Code:**

This method adds code to the `Top` or `Down` of a URL:
Here we added the contents of the `Append.py` file to `Down` of URL.
```
import os ; from rentrylab import RentryLab
RentryLab.myrentry().AppendToRentry("https://rentry.co/NewPage011",'NewPage011',os.path.join(os.path.dirname(__file__)),'Append','python','.py','Down',['## Append','!!!note End Row'])
```

**To Append Data:**

This method adds table data to the `Top` or `Down` of a URL:
Here we added the contents of the `Dict1` to Top of URL.
```
import os ; from rentrylab import RentryLab
Dict1 = {'Headers' : ['DiPTH','BS','CALI','GR','DT','QT'],
        'r0' : [1829.2572,12,22.0052,46.6003,117.0969,0.879],
        'r1' : [1829.4096,12,21.9816,46.2312,'Cell','Nan'],
        'r2' : [1829.4096,12,21.9816,46.2312,'GO','NOW']}
RentryLab.myrentry().AppendDataToRenty('https://rentry.co/Data1','Data1',os.path.join(os.path.dirname(__file__)),Dict1,'Top',HeaderList=['!!!danger 5:40 5/22/2023','## Data Append to Top'])
```

**Do you want to see how to Send or Get Codes visually?**

[Send and Get Code to Windows](https://youtu.be/re4J3bZkKAI)

[Send and Get Code to Linux](https://youtu.be/z5igWHFaPVE)

[Send and Get Code to PythonAnyWhere](https://youtu.be/5iGLaaf8baU)

**Do you want to see how works all syntax visually?**

[Send and Get Code to Windows](https://youtu.be/re4J3bZkKAI)
