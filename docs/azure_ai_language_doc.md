# Análise de Texto com Azure AI Language - Documentação de Testes

Este documento registra a experiência prática com o **Azure AI Language** no portal **Azure AI Foundry**, incluindo testes de extração de entidades, frases-chave e resumo de textos. O objetivo é documentar o processo e os insights obtidos durante os exercícios.

---

## 1. Introdução ao Processamento de Linguagem Natural (PLN)

O **Processamento de Linguagem Natural (PLN)** é um ramo da IA que lida com linguagem escrita e falada.  
Com o Azure AI Language, é possível:

- Extrair significado semântico de textos ou falas
- Identificar entidades nomeadas
- Extrair frases-chave
- Resumir textos
- Analisar sentimentos

> **Anotação:** Durante os testes, percebi que o serviço consegue distinguir nomes de lugares e pessoas mesmo em textos curtos, o que é útil para análise rápida de feedback de clientes.

---

## 2. Criando um Projeto no Azure AI Foundry

1. Acesse o portal: [Azure AI Foundry](https://ai.azure.com)  
2. Faça login e feche dicas iniciais.  
3. Navegue até **Criar → Novo Projeto**  
4. Configure:
   - **Assinatura**: sua assinatura Azure  
   - **Grupo de Recursos**: crie ou selecione um existente  
   - **Região**: Leste dos EUA, França Central, Coreia Central, Europa Ocidental ou Oeste dos EUA  
5. Aguarde a criação e acesse a página de visão geral do projeto.  
6. No menu à esquerda, selecione **Playgrounds → Playground de Idiomas**.

> **Anotação:** O tempo de criação do projeto varia, mas vale a pena esperar para ter todos os recursos ativados.

---

## 3. Teste: Extração de Entidades Nomeadas

### Procedimento
- Inserir avaliação de hotel e executar o bloco **Extrair entidades nomeadas**  
- Revisar saídas e pontuações de confiança

> **Insight:** A pontuação de confiança é essencial para decidir quais entidades considerar no processamento automatizado.  
> **Dica:** Para textos longos, o serviço ainda mantém boa precisão, mas pode ser interessante dividir o texto em blocos menores.

---

## 4. Teste: Extração de Frases-Chave

- Inserir avaliação e executar **Extrair frases-chave**

> **Insight:** Frases extraídas ajudam a resumir rapidamente o feedback do cliente sem precisar ler o texto completo.  
> **Observação:** O serviço tende a capturar informações mais relevantes quando o texto contém descrições detalhadas.

---

## 5. Teste: Resumir Texto

- Inserir avaliação e executar **Resumir texto**

> **Insight:** A sumarização extrativa é muito útil para relatórios automatizados.  
> **Dica:** Verifique se frases-chave importantes não foram omitidas; às vezes, é necessário ajustar o texto de entrada.

---

## 6. Limpeza de Recursos

- Excluir recursos desnecessários no portal para evitar custos.

---

## 7. Insights Gerais

- Entidades nomeadas, frases-chave e resumo funcionam bem para análise rápida de avaliações  
- Documentação detalhada ajuda a replicar testes em outros projetos  
- Testes manuais foram essenciais para entender a precisão e limitações do serviço
