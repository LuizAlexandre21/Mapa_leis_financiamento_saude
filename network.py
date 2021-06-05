from dash.dependencies import Input, Output
import dash 
import dash_core_components as dcc 
import dash_html_components as html 
import dash_cytoscape as cyto 
import plotly.express as px 

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("<h1>Dash Cytoscape:</h1>"),
    cyto.Cytoscape(
        elements=[
            {'data':{'id':'1988','label':'Constituição Federal'}},
            {'data':{'id':'8080','label':'Lei 8080'}},
            {'data':{'id':'8142','label':'Lei 8142'}},
            {'data':{'id':'1232','label':'Decreto 1232'}},
            {'data':{'id':'29','label':'Emenda Constitucional 29'}},
            {'data':{'id':'141','label':'Lei Complementar 141'}},
            {'data':{'id':'86','label':'Emenda Constitucional 86'}},
            {'data':{'id':'95','label':'Emenda Constitucional 95'}},    
            {'data':{'id':'6','label':'Portaria de Consolidação 6'}},
            {'data':{'id':'3992','label':'Portaria 3992'}},
            {'data':{'id':'CONSEMS','label':'Nota tecnica CONSEMS'}},
            {'data':{'id':'2997','label':'Portaria 2979'}},
            {'data':{'id':'488','label':'Portaria 488'}},
            {'data':{'id':'106','label':'Emenda Constitucional 106'}},  
            {'data':{'id':'109','label':'Emenda Constitucional 109'}},          
            {'data':{'source':'1988','target':'8080'}},
            {'data':{'source':'8080','target':'2997'}},
            {'data':{'source':'8080','target':'6'}},
            {'data':{'source':'8080','target':'488'}},
            {'data':{'source':'1988','target':'8142'}},
            {'data':{'source':'8142','target':'1232'}},
            {'data':{'source':'1232','target':'488'}},            
            {'data':{'source':'1232','target':'6'}},
            {'data':{'source':'6','target':'3992'}},
            {'data':{'source':'3992','target':'CONSEMS'}},
            {'data':{'source':'8142','target':'1232'}},
            {'data':{'source':'1232','target':'29'}},
            {'data':{'source':'1988','target':'29'}},
            {'data':{'source':'141','target':'8142'}},
            {'data':{'source':'141','target':'8080'}},
            {'data':{'source':'8142','target':'1232'}},
            {'data':{'source':'1988','target':'86'}},
            {'data':{'source':'86','target':'95'}},
            {'data':{'source':'1988','target':'106'}},
            {'data':{'source':'106','target':'109'}},
            {'data':{'source':'109','target':'95'}},
        ],
        style={'width': '100%', 'height': '500px'},
        layout = {'name':'breadthfirst'},
    )
])
app.run_server(debug=True)
