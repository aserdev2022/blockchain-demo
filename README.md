**Activate the vritual enviroment**

````
$ ~ => source /home/[yourname]/[your project]/etc/blockchain-env/bin/activate
````

**install all packages**

````
$~ => pip3 install -r /home/[your name]/[the project]/requirments.txt
````

**get ready for the download**

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

**Run the application and API**

Make sure to activate the virtual environment.

````
$~ => python3 -m backend.app
````

**Run a peer instance**

Make sure to activate the virtual environment.

````
$~ => export PEER=True && python3 -m backend.app
````

**Run the frontend**

In the frontend directory:
````
$~ => npm run start
````

**Seed the backend with data**

Make sure to activate the virtual environment.

````
$~ => export SEED_DATA=True && python3 -m backend.app
````

