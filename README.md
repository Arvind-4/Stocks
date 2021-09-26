
# Stocks

The Website is Live on [stockanalysis4you](https://stockanalysis4you.herokuapp.com/) .

Here's a list of the packages we will use to accomplish this:

-   Django
-   HTML5
-   CSS3
-   Gunicorn
- whitenoise
-   and more .

## Code 

### Install Virtualenv 
```
pip install virtualenv
cd /path/to/folder
mkdir stocks
cd stocks
python -m venv .
```
### Activate the Virtualenv
```
source scripts/activate
```
### Install Dependencies
```
cd /path/to/folder/stocks
mkdir src
cd src 
git clone https://github.com/Arvind-4/Stocks.git .
pip install -r requirements.txt
```


### Run the Code
```
cd /path/to/folder/health_website/src
./run.sh
```

### Create Super User
```
cd /path/to/folder/health_website/src
./superuser.sh
```
