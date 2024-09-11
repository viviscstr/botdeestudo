import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY = 'COLOQUE SUA API KEY AQUI'"])

model = genai.GenerativeModel("gemini-1.5-flash")

while True:
  pergunta = input('Sua pergunta (Insira sair para parar) \n -> ')
  if pergunta == 'sair':
    print('Até mais')
    break
  
  response = model.generate_content(pergunta)
  print(response.text)

  # instruções do sistema
  system_instructions = """
  Voce responde de maneira carinhosa e divertida, seu nome é lyvi e voce é uma mulher. quero que voce responda as perguntas de maneira que seja fácil para compreender.
   
  """

  # A função para gerar respostas com as instruções do sistema
  def gerar_resposta(pergunta):
    # Comninar as instruções do sistema com a pergunta do usúario 
    prompt = f"{system_instructions}\n\nPergunta: {pergunta}"

    try:
      #Gerar a resposta usando o modelo
      response = model.generate_content(prompt)
      return response.text
    except Exception as e:
      return f"Ocorreu um erro ao processar o chat: {e}"
