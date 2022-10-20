from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import pandas as pd
import os
from pandas import DataFrame, read_csv

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("base.html")

@app.route('/test')
def test():
    return render_template("test.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/login')
def login_page():
    return render_template("login.html")

@app.route('/compute')
def compute_page():
    return render_template("forest_fire.html")

@app.route('/student1')
def student_input_page1():
    return render_template("student1.html")

@app.route('/student2')
def student_input_page2():
    return render_template("student2.html")

@app.route('/group0')
def student_group_zero():
    return render_template("lessthan.html")

@app.route('/group1')
def student_group_one():
    return render_template("between.html")

@app.route('/group2')
def student_group_two():
    return render_template("morethan.html")

@app.route('/afterupload')
def after_upload(p):
    return render_template("showtable.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[]
    for x in request.form.values():
    	int_features.append(x)
    final=[int_features]
    print(int_features)
    print(final)
    prediction=model.predict(final)
    ybar=['sem-1','sem-2','sem-3','sem-4','sem-5']
    if prediction<0.5:
        return render_template('lessthan.html', labels=ybar,values=int_features)#'<Less than or equal to 6.75 CGPA'
    elif prediction<1.5:
        return render_template('between.html', labels=ybar,values=int_features)#'Between 6.75 CGPA and 8.00 CGPA'
    else:
        return render_template('morethan.html', labels=ybar,values=int_features)#'More than 8.00 CGPA'


app.config['FILE_UPLOADS']=r'C:\Users\savio\Downloads\Meliorem\Meliorem'

@app.route('/upload_file',methods=['POST','GET'])
def upload_file():
    #if request.method == 'POST':
    #if request.form.get("upload"):
    if request.files:
        test_file = request.files['test_file']
        selectValue = request.form.get('cars')
        selectValue1 = request.form.get('sems')
        test_file.save(os.path.join(app.config['FILE_UPLOADS'], test_file.filename))
        print('File saved')
        #perform()
        data = pd.read_csv(test_file.filename)
        print(data.head())
        df=data[['sem-1','sem-2','sem-3','sem-4','sem-5']]
        yhat = model.predict(df)
        data['Class']='24'
        for index, row in data.iterrows():
            data.loc[index, 'Class'] = yhat[index]
        boys = data.Student_ID
        #girls = data[data.Gender == 0]
        #g=[]
        labels = []
        values1 = []
        values2 = []
        values3 = []
        values4 = []
        values5 = []
        values6 = []
        for i in boys:
            labels.append(i)
        for i in df['sem-1']:
            values1.append(i)
        for i in df['sem-2']:
            values2.append(i)
        for i in df['sem-3']:
            values3.append(i)
        for i in df['sem-4']:
            values4.append(i)
        for i in df['sem-5']:
            values5.append(i)
        for i in range(0,len(boys)):
            j = (values1[i] + values2[i] + values3[i] + values4[i] + values5[i])/5
            j = round(j,2)
            values6.append(j)

        #for i in girls['sem-1']:
            #g.append(i)
        data.to_csv("test-set.csv", index=False)
        p=data.to_html(header="true", table_id="table")
        if selectValue=='saab' and selectValue1=='sem-1':
            return render_template('forest_fire.html',labels=labels,values=values6)
    #    elif selectValue=='saab' and selectValue1=='sem-2':
    #    elif selectValue=='saab' and selectValue1=='sem-3':
    ##    elif selectValue=='saab' and selectValue1=='sem-4':
    #        return render_template('forest_fire.html',labels=labels,values=values4)
    #    elif selectValue=='saab' and selectValue1=='sem-5':
        else:
            return p


if __name__ == '__main__':
    app.run(debug=True)
