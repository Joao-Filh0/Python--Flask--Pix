# Python-Flask-Pix

[Python](https://www.python.org/) | [Fask](https://flask.palletsprojects.com/en/2.0.x/) | [Pix](https://www.bcb.gov.br/estabilidadefinanceira/pix?modalAberto=regulamentacao_pix) 


Nesse projeto mostrarei como implentar forma de pagamento "PIX" utilizando a linguaagem de progamação python e seu framework flask.
Utilizei  Pague Seguro para testes.
Esse projeto reune todos os processos exigidos pela [BCB](https://www.bcb.gov.br/estabilidadefinanceira/pix) 

<img src="https://www.python.org/static/img/python-logo-large.c36dccadd999.png?1576869008" width="80px"/> <img src="https://pedroglp.com/dist/flaskic.png" width="150px"/> <img src="https://www.bcb.gov.br/content/estabilidadefinanceira/piximg/logo_pix.png" width="200px"/>                                                   


## Configuração

### Requisitos

- Python >= 3.7.0
- Flask==1.0.2
- Flask-Cors==1.10.3
- Flask-RESTful==0.3.9
- libscrc==1.6
- requests==2.26.0 


**Nota** : Essas foram as versões das libs utilizadas por min, tendo em conta é o que esta funcionando até o presente momento.

### Instalar libs
- Segue alguns comandos que precisará rodar.

```bash
pip install Flask==1.0.2 Flask-Cors==1.10.3 Flask-RESTful==0.3.9 libscrc==1.6 requests==2.26.0
```
### Adcionado credenciais
Vá até /constants/data/ onde podera colocar suas credencias que foram fornecidas pelo banco.
No arquivo constants/permissions.py adicione seu arquivo .pem e .key .


```CERTIFICATES = (__credentalsPath("Seu arquivo .pem"),__credentalsPath("Seu Arquivo .key"))```


Ainda no arquivo constants/permissions.py cole seu CLIENTE_ID e seu CLIENT_SECRET nas váriaveis.

```__CLIENT_ID__ = "Cole aqui seu CLIENT_ID"
__CLIENT_SECRET__ = "Cole Aqui seu CLIENT_SECRET" ```

### Configurando webhooks

Cole na chave `webhookUrl` a url da api que quer configurar.

```webhook_data =  {"webhookUrl": "Api de sua Url Hook"}```

 









#### Autor `Joao Alves`
- [LINKEDIN](https://www.linkedin.com/in/joao-alves-505b541a8)
- `email :` militaof522@gmail.com 

 
 


