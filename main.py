from fastapi import FastAPI

app = FastAPI()

@app.post('/api/signup')
def signup():
    pass

@app.post('/api/activate')
def activate():
    pass

@app.post('/api/login')
def login():
    pass

@app.post('/api/add-sent')
def add_sent():
    pass

@app.post('/api/add-recived')
def add_recived():
    pass

@app.post('/api/add-debt')
def add_dept():
    pass

@app.delete('/api/delete-debt')
def delete_debt():
    pass

@app.post('/api/add-demand')
def add_demand():
    pass

@app.delete('/api/delete-demand')
def delete_demand():
    pass

@app.get('/api/depts')
def depts():
    pass

@app.get('/api/demands')
def demands():
    pass

@app.get('/api/report')
def report():
    pass

@app.get('/api/health')
def health():
    return {'msg': 'Ok'}