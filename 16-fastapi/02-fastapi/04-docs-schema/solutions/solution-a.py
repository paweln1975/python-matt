
class AstronautIn(Schema):
    firstname: str
    lastname: str
    age: int | None = None
    height: float | None = None
    weight: float | None = None
    missions: list[str] | None = None


@app.post('/astronaut')
def post(astro: AstronautIn):
    with open(FILE, mode='w') as file:
        data = astro.json()
        file.write(data)
    return {'details': 'created'}


@app.get('/astronaut')
def get():
    with open(FILE, mode='r') as file:
        return json.load(file)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, restart=True)
