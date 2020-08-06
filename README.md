# MISP_TIE_SET_REPUTATION

Prerequisites: (For user want to create new project)
- Python 3, python3-venv, pip, pip3, visual Code (can change other IDE)

Additional Step: (For user want to create new project)
It is strongly recommended to use a virtual environment

Step 0: Active MISP_TIE_SET_REPUTATION project (you can change project name)
  source MISP_TIE_SET_REPUTATION/bin/activate

Step 1: Install PyMISP
  pip3 install wheel
  pip3 install pymisp
  
Step 2: Install requests
  pip3 install requests
  
Step 3: Download OpenDXL SDK zip file and OpendDXL TIE SDK zip file, and install them
  Go to site https://github.com/opendxl/opendxl-client-python/releases/tag/5.6.0.3 and download OpenDXL SDK zip file
  Go to site https://github.com/opendxl/opendxl-tie-client-python/releases/tag/0.3.0 and download OpendDXL TIE SDK zip file
  Go to folder contain 2 zips file and unzip, install file .whl (Example is Downloads folder)
  
  cd Downloads/
  unzip dxlclient-python-sdk-5.6.0.3.zip
  unzip dxltieclient-python-dist-0.3.0.zip
  pip3 install dxlclient-python-sdk-5.6.0.3/lib/dxlclient-5.6.0.3-py2.py3-none-any.whl
  pip3 install dxltieclient-python-dist-0.3.0/lib/dxltieclient-0.3.0-py2.py3-none-any.whl
  
Configuration:
  You must create folder config that contain all config file
  
Step 1: move to MISP_TIE_SET_REPUTATION project and create config folder
  cd MISP_TIE_SET_REPUTATION/
  mkdir config
  
Step 2: create Command Line Provisioning
  dxlclient provisionconfig config myserver client1 -u myuser -p mypass
  
  In this:
    config: config folder
    myserver: EPO server ip
    client1: ip client
    myuser: EPO server username
    mypass: EPO server password
    
  On success, output similar to the following should be displayed:
    INFO: Saving csr file to config/client.csr
    INFO: Saving private key file to config/client.key
    INFO: Saving DXL config file to config/dxlclient.config
    INFO: Saving ca bundle file to config/ca-bundle.crt
    INFO: Saving client certificate file to config/client.crt
    
  Step 3: create misp_key.ini
    vim config/misp_key.ini
    
    Edit them:
    [MISP_KEY_INFO]
    misp_url = #this is misp url
    misp_key = #this is Automation API key
    
    save and exit
    
  
RUN PROJECT:
    You can git clone myproject and create Configuration step to run project or you can refer my project to write method/ folder and main.py file. 
      
      source MISP_TIE_SET_REPUTATION/bin/activate
      cd MISP_TIE_SET_REPUTATION/
      bin/python3 main.py



  
  
  
  
  
  

  




