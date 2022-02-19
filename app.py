#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
import joblib

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        print(rates)
        #Linear Regression Model 
        model1 = joblib.load("DBSReg")
        pred1 = model1.predict([[float(rates)]])
        s1 = "Predicted DBS share price based on Linear Regression Model is: " + str(pred1)
        #Decision Tree Model 
        model2 = joblib.load("DBSDT")
        pred2 = model2.predict([[float(rates)]])
        s2 = "Predicted DBS share price based on Decision Tree Model is: " + str(pred2)
        #Neural Network Model
        model3 = joblib.load("DBSNN")
        pred3 = model3.predict([[float(rates)]])
        s3 = "Predicted DBS share price based on Neural Network Model is: " + str(pred3)
        return(render_template("index.html", result1=s1,result2=s2,result3=s3))
    else:
        return(render_template("index.html", result1="2",result2="2",result3="2"))


# In[4]:


if __name__ =="__main__":
    app.run()


# In[ ]:




