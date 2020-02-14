
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import json


import random
import seaborn as sns 
import matplotlib.pyplot as plt 

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests 
import time
import pandas as pd




def link_preProcess(kk):
    jkl=''
    ooo=[]
    semi_out=[]
    final_out=[]
    for i in kk:
        pp=str(i)
        for j in pp:
            print(j)
            if(j=='&'):
                break;
            else:
                jkl=jkl+j

        print(jkl)

        ooo.append(jkl)
        jkl=''          

    for i in ooo:
        if(i=='None'):
            continue
        else:
            semi_out.append(i.replace('<a href="/url?q=', '').replace('<a href=',''))

    return semi_out




df1=['ENTER KEY WORD','SEARCH BY IMAGE'];
range_=len(df1)

app = dash.Dash()

body = {
'background-color':'#F29C6B',
},
        
ALLOWED_TYPES = (
    "text", "number", "password", "email", "search",
    "tel", "url",
),




app.layout = html.Div([
            html.Div(
            className="app-header",
            children=[
                html.Div('Search with keyword', className="app-header--title")
            ]
        ),
            
  ############################################################          
       html.Div([
    dcc.Dropdown(
        id='dropdown',
        style={'height': '30px', 'width': '98%',
               'margin': '20px'
               
               
               },
        options=[{'label': df1[i] , 'value': i} for i in range(range_)],
        value='a'
    ),
    html.Div(id='dd-output-container'),
        html.Div(id="table1"),


        ]),
    
  ############################################################
html.Div(
        id="db-input",
        children=[
        html.I("Insert Images"),
        html.Br(),
        dcc.Input(id="input1",className="in1", type="text", placeholder="db name"),
        dcc.Input(id="input2",className="in1", type="text", placeholder="user name ", debounce=True),
        dcc.Input(id="input3",className="in1", type="text", placeholder="ip"),
        dcc.Input(id="input4",className="in1", type="text", placeholder="password ", debounce=True),
        dcc.Input(id="input5",className="in1", type="text", placeholder="table name ", debounce=True),
        html.Div(id="output"),
    ]
    
), 

html.Div(
        id="csv-input",
        children=[
        html.I("Please enter and submit"),
        html.Br(),
        dcc.Input(id="input6",className="in1", type="text", placeholder="file name"),
        html.Button('Submit', id='button1'),

        html.Div(id="output1"),
    ]
    
), 
#    html.Div(id='output')
],#style={'background-color': '#F29C6B',} 



)

####################################################
@app.callback(
    dash.dependencies.Output('db-input', 'style'),
    [dash.dependencies.Input('dropdown', 'value')])
def update_output(value):
#    return 'You have selected {}'.format(value)
    if(value==1):
        return {'display':'block'}
    else:
        return {'display':'none'}


####################################################
@app.callback(
    dash.dependencies.Output('csv-input', 'style'),
    [dash.dependencies.Input('dropdown', 'value')])
def update_output2(value):
#    return 'You have selected {}'.format(value)
    if(value==0):
        return {'display':'block'}
    else:
        return {'display':'none'}

##########################################
@app.callback(
    Output("output", "children"),
    [Input("input1", "value"), Input("input2", "value")],
)
def update_output1(input1, input2):
    return u'Input 1 db name {} and Input 2 user name {}'.format(input1, input2)




    
@app.callback(
    dash.dependencies.Output('output1', 'children'),
    [dash.dependencies.Input('button1', 'n_clicks')],
    [dash.dependencies.State('input6', 'value')])
def read_csv(n_clicks, value):
    driver= webdriver.Chrome(executable_path=r"C:\Users\TAMESH\Downloads\chromedriver_win32\chromedriver.exe")
    time.sleep(2)
    driver.get("https://www.google.com/")
    time.sleep(4)
    data='sars virus'
    elementID= driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    elementID.send_keys(data)
    time.sleep(1)
    elementID.send_keys(Keys.ENTER)
    time.sleep(6)
    url=driver.current_url
    print(url)
    r = requests.get(url) 
    section_table=[]
    Price_table=[]
    city_names_=[]
    ooo=[]
    soup = BeautifulSoup(r.content, 'html5lib') 
    aa=soup.prettify()
    print(soup.prettify())
    GG=[]
    GH=[]
    aaa=soup.find_all(class_='BNeawe vvjwJb AP7Wnd')
    for i in aaa:
        GG.append((((i.text).strip()).replace('�', '')).replace('...', ''))
        
    print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")   
    a1=soup.find_all(class_='BNeawe s3v9rd AP7Wnd')
    for i in a1:
        GH.append((((i.text).strip()).replace('�', '')).replace('...', ''))
        
    
    kk=[]
    subSeed_links=soup.find_all(class_='kCrYT')
    for i in subSeed_links:
        kk.append(i.a)
    #     print((i.a))
    
    
    
    links_=link_preProcess(kk)
    count=1;
    ghj=[]
    ghjk=[]
    mmm=''
    for single_link in links_:
    #     print(single_link) 
        try:
            r = requests.get(single_link) 
            section_table=[]
            Price_table=[]
            city_names_=[]
            ooo=[]
            soup = BeautifulSoup(r.content, 'html5lib') 
    #         aa=soup.prettify()
    #         print(soup.prettify())
            para=soup.find_all('p')
            if(para==[]):
                continue
            else:
                print(count)
                count=count+1
                print(single_link)
    #             print(para)
    #             ghjk.append(count)
    #             ghjk.append(single_link)
                mm=''
                for i in para:
    #                 print(i.text)
                      ghj.append(i.text)
    #                 ghj.append('html.P(\''+i.text+'\')')
#                    mm=mm+'html.P(\''+i.text+'\'),'
#                    print(mm)
                ghjk.append(ghj)
                 
#                mmm=mmm+mm
#                for i in para:
#                    print(i.text)
#                    ghj.append(i.text)
#                    mm=mm+i.text
#                ghjk.append(ghj)
#                mmm=mmm+mm
                
    #         print(para)
    #         for i in para:
    #             print(i.text)
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        except:
            continue





#    return '"{}" and the button has been clicked {} times'.format(
#        ghjk,
#        n_clicks
        #)
    hari=pd.concat([pd.DataFrame([i], columns=['A']) for i in ghj],ignore_index=True)
    hari.to_csv('haha.csv')

    data = hari.to_dict('rows')
    columns =  [{"name": i, "id": i,} for i in (hari.columns)]
    return dt.DataTable(data=data, columns=columns,style_cell={'textAlign': 'left','width': '250px'},)















if __name__ == '__main__':
    app.run_server(debug=True,port=8003)
    
    
    



