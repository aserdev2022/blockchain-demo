# Activate the virtual environment

my py3 interpreter is in the virtual-env and my pakages

````
$ ~ => source blockchain-demo/bin/activate
````

# install all packages

````
$~ => pip3 install -r requirments.txt
````

# get ready for the download

**1- install python3**

you need py3 for running and debug

```
$~ => apt install python3
```

or


```
https://www.python.org/
```



**2- install git**

```
$~ => apt install git
```

or

```
https://git-scm.com/downloads
```

**3-install a code editor {optional}**

**1-vscode**

```
$~ => apt install code-oss
```

or

```
https://code.visualstudio.com/
```

2- pycharm {a good choice}

```
$~ => apt install snapd
```

```
$~ => snap install pycharm-community --classic
```

or

```
https://www.jetbrains.com/pycharm/download/ 
```

**2-import python to vscode**

```
https://youtu.be/cUAK4x_7thA
```

# ok the last step!

```
$~ => git clone https://github.com/aserdev2022/aser-blockchain-py.git
```

**and now open the project and run anything and change anything**

# run the tests

make sure to activate the virtual environment

```
$~ => python3 -m pytest backend/tests

```

# Run the application and API

Make sure to activate the virtual environment.

````
$~ => python3 -m backend.app
````

# Run a peer instance

Make sure to activate the virtual environment.

````
$~ => export PEER=True && python3 -m backend.app
````

# Run the frontend

In the frontend directory:
````
$~ => npm run start
````

# Seed the backend with data

Make sure to activate the virtual environment.

````
$~ => export SEED_DATA=True && python3 -m backend.app
````

# best tips for py3 projects

**make a venv before running any project**

```
$~ => python3 -m venv [name your venv] 
```

**activate it**

```
$~ => source [your venv]/bin/activate
```

**add some tests!**

tests help you to discover some bugs in your projects and try some code before you add it to the app

**1- install pytest**

```
$~ => pip3 install pytest==7.2.0
```

**2- create some tests**

create a file called 'test_[the thing you want to test].py'



now to run the test

```
$~ => python3 -m pytest
```

now if you see an error that means there is a bug or problem in your project

if you see 'test passed' that means that your project is fine


# set up pycharm for python

**first install pycharm ide**

```
$~ => apt install snapd
```

```
$~ => snap install pycharm-community --classic
```

or

```
https://www.jetbrains.com/pycharm/download/ 
```

now open pycharm


**Install some useful plugins**

**1-Requirements**

this plugin helps you to install requirements.txt packages 

ok to use it open your ide and create a requirements.txt file 

now add any python packages do you want to install

**example: my requirements.txt file**
```
pytest==7.2.0
Kivy~=2.1.0
pip==22.3.1
attrs~=22.1.0
wheel==0.38.4
docutils~=0.19
pluggy~=1.0.0
exceptiongroup~=1.0.1
iniconfig~=1.1.1
pyparsing~=3.0.9
setuptools==65.5.1
Flask==2.2.2
pubnub==7.0.1
requests==2.28.1
cryptography==38.0.3
Flask-Cors==3.0.10
```

**now to install the packages**

```
$~ => pip3 install -r requirements.txt
```

now wait for it to install

# some important notes

if you see the '$~ =>' in my commands that means that iam using bash

**if you want to use and install bash in windows**


****

```
https://git-scm.com/downloads
```

and install git

in the installer select 'install git bash'

or

install unix environments


**note:macos or linux has bash built in to use it open the terminal**








# iam sorry for the long description -_-
