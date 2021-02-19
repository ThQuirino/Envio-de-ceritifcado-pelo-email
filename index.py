import pandas as pd
from PIL import Image,ImageDraw, ImageFont
from valeEmail import sendEmail
class Contrato:
    def __init__(self,seu_email):
        self.password=''
        self.vetorDados={}
        self.seu_email=seu_email

    def read_Csv(self):
        ##passe aqui o caminho do seu arquivo csv
        valor_csv = pd.read_csv('contatos.csv')
        return valor_csv
    
    def writeImage(self,nomes):
      
        cont=0
        ##caminho do seu certificado
        foto_url='certificado2.png'
        imagem =Image.open(foto_url).convert('RGBA')
        font = ImageFont.truetype('CACPINAF.ttf',65)
        txt = Image.new("RGBA", imagem.size, (255,255,255,0))
        desenho_certificado= ImageDraw.Draw(txt)
        self.password=input("Digite a sua senha do email:\n")
        
        for nome in nomes[['Nome'][0]]:
            email=nomes[['E-mail'][0]][cont]
            txt = Image.new("RGBA", imagem.size, (255,255,255,0))
            desenho_certificado= ImageDraw.Draw(txt)
            ##mudar o local aonde a assinatura ficará
            desenho_certificado.text((600,360),nome,font=font,fill=(0,0,0,255))
            out = Image.alpha_composite(imagem, txt)
            nome_certificado=nome.replace(' ','_')+'.png'
            ##caso queria uma nova coluna como informação para enviar ao seu email, não esqueça 
            # de passar o novo valor no vetorEmail separado com virgula
            self.vetorDados[cont]= f'{nome_certificado},{email}'
            out.save(nome_certificado,'PNG',resolution=100.0)
            cont+=1
        
        for i in self.vetorDados:
            self.vetorDados[i]=self.vetorDados[i].split(',')

        sendEmail(self.password,self.seu_email).enviarEmail(self.vetorDados)
            
##seu email precisa ser um Gmail
digite_seu_email='seuEmail.com'
chamada= Contrato(digite_seu_email)
leitura=chamada.read_Csv()
chamada.writeImage(leitura)

