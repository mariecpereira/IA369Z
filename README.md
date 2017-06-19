
# READ ME - Corpus callosum diffusion properties differences in systemic lupus patients

 - Here you will find all the implementation necessary to reproduce the paper. 
 - For an illustrative notebook [link](http://nbviewer.jupyter.org/github/mariecpereira/IA369Z/blob/0f9c68668f11ce301f9467db9b108b2d36f48e56/deliver/18062017_Paper_MECPv2.ipynb)
 - The research paper is available at [link](https://github.com/mariecpereira/IA369Z/blob/master/deliver/Paper_IA369Z-.pdf)
 

## - What is this repository for? 

This repository is part of the IA369Z project course from School of Electrical and Computer Engineering (FEEC) at the University of Campinas. The algorithms contained here are part of the study of the paper "Corpus callosum diffusion properties differences in systemic lupus patients" and describe the ROQS segmentation method, the Witelson and Hofer and Frahm's parcellation methods. As well as the statistical analysis of the diffusion properties of the subjects. 

## - How do I get set up? 

Do not freak out! It is easier than you think. Let's get started: 

### 1 - Setting up the environment:

There are two different manners to reproduce this paper using Jupyter Notebook: 
 - through Anaconda (locally)
 - through Docker image 
 
###### It is advisable to use Docker, since the image will reproduce the promptly environment created by the author. If you rather use Anaconda instead, be aware of the fact that other installations you already had installed in your computer might affect reproducibility.

####  1.1 - Anaconda:  

- Install Anaconda 4.3.1 for Python 2.7.13 [Windows](https://www.continuum.io/downloads#windows), [Mac](https://www.continuum.io/downloads#macos) or [Linux](https://www.continuum.io/downloads#linux)

- To install the neuroimaging package, open up a terminal and type the following command: `pip install nibabel`. For more information [link](http://nipy.org/nibabel/installation.html)

- Go ahead and clone this repository typing the following command in your terminal: `git clone https://github.com/mariecpereira/IA369Z`

- In the same terminal, type: `jupyter notebook` 

- In your browser, paste the URL, the IPython Notebook is running at: http://0.0.0.0:8888/

- Follow the instructions and access the files into the deliver folder to reproduce the paper

####  1.2 - Docker Image:  

##### Docker on Mac (iOS version 10.10.5)

- Install Docker [link](https://store.docker.com/editions/community/docker-ce-desktop-mac)

- Go ahead and clone this repository typing the following command in your terminal: `git clone https://github.com/mariecpereira/IA369Z`

- Open the terminal in your computer and enter the command to run the image and to create the container: `sudo docker run -p 8888:8888 -v <the path you cloned IA369Z repository>:/home/ds/notebooks mecp/ia369z`

- In your browser, paste the URL, the IPython Notebook is running at: http://0.0.0.0:8888/

- Follow the instructions and access the files into the deliver folder to reproduce the paper


##### Docker on UBUNTU (version 16.04 LTS) [Reference](https://github.com/ecalio07/enron-paper/tree/master/environment)

- Install Docker [link](https://store.docker.com/editions/community/docker-ce-server-ubuntu)

- Go ahead and clone this repository typing the following command in your terminal: `git clone https://github.com/mariecpereira/IA369Z`

- Open the terminal in your computer and enter the command to run the image and to create the container: `sudo docker run -d -p 8888:8888 -v <the path you cloned IA369Z repository>:/home/ds/notebooks mecp/ia369z`

- In your browser, paste the URL, the IPython Notebook is running at: http://0.0.0.0:8888/

- Follow the instructions and access the files into the deliver folder to reproduce the paper


##### Docker on Windows (versions 8 and 10) [Reference](https://github.com/ecalio07/enron-paper/tree/master/environment)

- Install Docker, for Windows 10 Professional and Enterprise 64-bits [link](https://store.docker.com/editions/community/docker-ce-desktop-windows) OR Install Docker Toolbox for other Windows versions [link](https://www.docker.com/products/docker-toolbox)

- Go ahead and clone this repository typing the following command in your terminal, cloned directory must be inside C:\Users\{user} directory: `git clone https://github.com/mariecpereira/IA369Z`

- Open the terminal in your computer and enter the command to run the image and to create the container: `docker run -p 8888:8888 -v <the path you cloned IA369Z repository>:/home/ds/notebooks mecp/ia369z`

- In your browser, paste the URL, the IPython Notebook is running at: http://192.168.99.100:8888

- Follow the instructions and access the files into the deliver folder to reproduce the paper


### 2 - Which libraries do I need? 

It does not matter if you are reproducing this paper using Anaconda or Docker, it is necessary to download the following libraries into the EXACTLY root path (deliver folder) you cloned this repository.  

   - `dtimp` [download here](https://www.dropbox.com/s/cfgjexkqaa98yzz/dtimp.zip?dl=0)
   - `functions_will` [download here](https://www.dropbox.com/s/2mlw8twa516581f/functions_will.zip?dl=0)
   - `ia636` [download here](https://www.dropbox.com/s/z3vrav4mudh6h5e/ia636.zip?dl=0)
   - `ia870` [download here](https://www.dropbox.com/s/o2g35kpbmb183mt/ia870.zip?dl=0)
   
### 3 - How do I get the data?

For a data sample email: mariecpereira@gmail.com  

## - How do I run tests? 

Once you got all the requirements listed above set up, all you need to do is to run and test the code/data. Make sure that everything is at the same local folder.

## - Who do I talk to? 
For questions or more details email: mariecpereira@gmail.com
