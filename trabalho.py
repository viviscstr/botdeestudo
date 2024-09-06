import os
import google.generativeai as genai

genai.configure(api_key=)
model = genai.GenerativeModel("gemini-1.5-flash")

while True:
  pergunta = input('Sua perguntas (Insira sair para parar) \n -> ')
  if pergunta == 'sair':
    print('Até mais')
    break
  
  response = model.generate_content(pergunta)
  print(response.text)

  # instruções do sistema
  system_instructions = """
  Voce responde de forma genial e divertida, de uma maneira que fique muito simples de compreender qualquer assunto.
  quero que seja uma mulher ,seu nome é lyvi ela é sincera e muito carinhosa.
   
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
      return f"Ocorreu um erro ao processar a pergunta: {e}"
    
  while True:
    pergunta = input('Sua pergunta (Insira "sair" para parar) \n ->')
    if pergunta.lower() == 'sair':
      print('Até mais! Foi divertido conversar com você. ')
      break
    resposta = gerar_resposta(pergunta)
    print(resposta)


  
