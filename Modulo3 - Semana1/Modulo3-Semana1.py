import requests

class Modelos:
    def __init__(self, codigo: str):
        url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo}/modelos/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            self.modelos = data['modelos']
            self.passo = 0
            self.tamanho = len(self.modelos)
             
        else:
            print ('Falha ao carregar!')

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.passo >= self.tamanho:
                raise StopIteration
        
        resposta = list(self.modelos)[self.passo]
        self.passo = self.passo + 1
        return resposta
        
mod = Modelos('3')

for m in mod:
    print ('Codigo:', m['codigo'], '\tNome:', m['nome'])