import os
import cv2
import pytesseract
from pdf2image import convert_from_path
import difflib

#caminhos
caminho1 = r"C:\Users\Rose\Documents\listComp\Diretorio1"
caminho2 = r"C:\Users\Rose\Documents\listComp\Diretorio2"
caminho_tesseract = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = os.path.join(caminho_tesseract, "tesseract.exe")

def processar_texto(texto, caminho_arquivo):

    if texto:
        print("Texto no Diretório 1 encontrado.")
    else:
        avisoFalha = f"Não foi possível identificar texto no arquivo {caminho_arquivo}."
        print(avisoFalha)

def process_files(caminho):
    with open('texto do Diretório1.txt', 'w', encoding='utf-8') as f:
        for nome_arquivo in os.listdir(caminho):
            caminho_arquivo = os.path.join(caminho, nome_arquivo)
            texto = ''
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
                        f.write(texto + "\n")
                except Exception as e:
                    print(f"Erro ao processar a imagem {caminho_arquivo}: {str(e)}")

            processar_texto(texto, caminho_arquivo)

process_files(caminho1)


def processar_texto2(texto2, caminho_arquivo2):

    if texto2:
        print("Texto no Diretório 2 encontrado.")
    else:
        avisoFalha = f"Não foi possível identificar texto no arquivo {caminho_arquivo}."
        print(avisoFalha)

def process_files2(caminho):
    with open('texto do Diretório2.txt', 'w', encoding='utf-8') as f:
        for nome_arquivo in os.listdir(caminho):
            caminho_arquivo2 = os.path.join(caminho, nome_arquivo)
            texto2 = ''
            if nome_arquivo.endswith('.pdf'):
                try:
                    imagens = convert_from_path(caminho_arquivo2)
                    for imagem in imagens:
                        temp_img_path = 'temp_img.jpg'
                        imagem.save(temp_img_path, 'JPEG')
                        img = cv2.imread(temp_img_path)
                        if img is not None:
                            texto2 += pytesseract.image_to_string(img)
                        os.remove(temp_img_path)
                except Exception as e:
                    print(f"Erro ao processar o arquivo PDF {caminho_arquivo2}: {str(e)}")
            elif nome_arquivo.endswith('.jpeg'):
                try:
                    img = cv2.imread(caminho_arquivo2)
                    if img is not None:
                        texto2 = pytesseract.image_to_string(img)
                        f.write(texto2 + "\n")
                except Exception as e:
                    print(f"Erro ao processar a imagem {caminho_arquivo2}: {str(e)}")

            processar_texto2(texto2, caminho_arquivo2)

process_files2(caminho2)


#def separando(texto, texto2):
 #   with open('texto.txt', 'w', encoding='utf-8') as f:
 #       diferenca = difflib.ndiff(texto1.splitlines(), texto2.splitlines())
 #       linhas_diferentes = [linha for linha in diferenca if linha.startswith('- ') or linha.startswith('+ ')]
 #       return '\n'.join(linhas_diferentes)

    # Exemplo de uso
    #texto = "Este é o primeiro texto.\nEle tem algumas diferenças."
    #texto2 = "Este é o primeiro texto.\nEle tem algumas diferenças.\n2"

    #diferencas = separando(texto, texto2)
    #f.write(diferencas + "\n")
    #print(diferencas)
