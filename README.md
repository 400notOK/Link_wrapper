# Bitly url wrapper
Util to wrap URLs via Bit.ly service. Has additional option for get count clicks on Bit.ly links which you created.

### Installing

Get script:
```buildoutcfg
git clone https://github.com/400notOK/Link_wrapper.git
```

Create [bit.ly](https://bitly.com) `GENERIC ACCESS TOKEN` for work with API. 
Specify your token in `.env` file `BITLY_ACCESS_TOKEN=<your token>`.

Example:
```buildoutcfg
echo `BITLY_ACESS_TOKEN`=<your token>
```

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```buildoutcfg
pip install -r requirements.txt
```

### Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org).