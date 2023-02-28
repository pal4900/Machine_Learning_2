from flask import Flask
from sales.logger import logging
from sales.exception import SalesException

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    logging.info("Logger") 
    return 'Starting Machine Learning Project'


if __name__ =="__main__":
    app.run(debug=True)
