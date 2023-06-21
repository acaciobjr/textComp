import os
import cv2
import pytesseract
from pdf2image import convert_from_path
import difflib

#caminhos
caminho1 = r"Diretório onde estará a lista original"
caminho2 = r"Diretório onde estará a lista com alterações"
caminho_tesseract = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = os.path.join(caminho_tesseract, "tesseract.exe")

def processar_texto(texto_limpo, caminho_arquivo):
    if texto_limpo:
        print("Texto no Diretório 1 encontrado.")
    else:
        avisoFalha = f"Não foi possível identificar texto no arquivo {caminho_arquivo}."
        print(avisoFalha)

def process_files(caminho):
    texto = ''
    with open('texto do Diretório1.txt', 'w', encoding='utf-8') as f:
        for nome_arquivo in os.listdir(caminho):
            caminho_arquivo = os.path.join(caminho, nome_arquivo)
            if nome_arquivo.endswith('.pdf'):
                try:
                    imagens = convert_from_path(caminho_arquivo)
                    for imagem in imagens:
                        temp_img_path = 'temp_img.jpg'
                        imagem.save(temp_img_path, 'JPEG')
                        img = cv2.imread(temp_img_path)
                        if img is not None:
                            texto += pytesseract.image_to_string(img)
                        os.remove(temp_img_path)
                except Exception as e:
                    print(f"Erro ao processar o arquivo PDF {caminho_arquivo}: {str(e)}")
            elif nome_arquivo.endswith('.jpeg'):
                try:
                    img = cv2.imread(caminho_arquivo)
                    if img is not None:
                        texto = pytesseract.image_to_string(img)
                        texto_limpo = texto.replace('  ', '').replace('   ', '').replace('-', '').replace('_', '').replace('—', '').replace('.', '').replace('TECNICO ENFERMAGEM', '').replace('HOSPITAL JACAREPAGUA', '')
                        f.write(texto_limpo + "\n")
                        processar_texto(texto_limpo, caminho_arquivo)
                except Exception as e:
                    print(f"Erro ao processar a imagem {caminho_arquivo}: {str(e)}")


process_files(caminho1)
def processar_texto2(texto_limpo2, caminho_arquivo):
    if texto_limpo2:
        print("Texto no Diretório 2 encontrado.")
    else:
        avisoFalha = f"Não foi possível identificar texto no arquivo {caminho_arquivo}."
        print(avisoFalha)

def process_files2(caminho):
    texto2 = ''
    with open('texto do Diretório2.txt', 'w', encoding='utf-8') as f:
        for nome_arquivo in os.listdir(caminho):
            caminho_arquivo = os.path.join(caminho, nome_arquivo)
            if nome_arquivo.endswith('.pdf'):
                try:
                    imagens = convert_from_path(caminho_arquivo)
                    for imagem in imagens:
                        temp_img_path = 'temp_img.jpg'
                        imagem.save(temp_img_path, 'JPEG')
                        img = cv2.imread(temp_img_path)
                        if img is not None:
                            texto2 += pytesseract.image_to_string(img)
                        os.remove(temp_img_path)
                except Exception as e:
                    print(f"Erro ao processar o arquivo PDF {caminho_arquivo}: {str(e)}")
            elif nome_arquivo.endswith('.jpeg'):
                try:
                    img = cv2.imread(caminho_arquivo)
                    if img is not None:
                        texto2 = pytesseract.image_to_string(img)
                        texto_limpo2 = texto2.replace('  ', '').replace('   ', '').replace('-', '').replace('_', '').replace('—', '').replace('.', '').replace('TECNICO ENFERMAGEM', '').replace('HOSPITAL JACAREPAGUA', '')
                        f.write(texto_limpo2 + "\n")
                        processar_texto2(texto_limpo2, caminho_arquivo)
                except Exception as e:
                    print(f"Erro ao processar a imagem {caminho_arquivo}: {str(e)}")

process_files2(caminho2)


def separando(caminho_texto1, caminho_texto2):
    with open('diferenca.txt', 'w', encoding='utf-8') as f:
        with open(caminho_texto1, 'r', encoding='utf-8') as arquivo1:
            texto1 = arquivo1.readlines()
        with open(caminho_texto2, 'r', encoding='utf-8') as arquivo2:
            texto2 = arquivo2.readlines()

        nomes1 = set(texto1)
        nomes2 = set(texto2)

        #Cria uma cópia de nomes1
        nomes_ausentes = nomes1.copy()  

        for nome in nomes1:
            if nome in nomes2:
                nomes_ausentes.remove(nome)

        nomess=nomes_ausentes.copy()
        for nm in nomes_ausentes:
            if nm in nomes2:
                nomess.remove(nm)

        print(nomess)
        #f.write('\n'.join(nomes_ausentes))

separando('texto do Diretório1.txt', 'texto do Diretório2.txt')
