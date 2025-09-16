# Exploração de Fala com Azure AI Speech - Documentação de Testes

Este documento registra a experiência prática com o **Azure AI Speech** no portal **Azure AI Foundry**, incluindo testes de transcrição de áudio e conversão de texto em fala.

---

## 1. Introdução ao Azure AI Speech

O **Azure AI Speech** permite:

- Transcrever fala em texto em tempo real  
- Converter texto em fala audível  
- Criar aplicativos que automatizam transcrição de reuniões ou entrevistas  

> **Anotação:** Durante os testes, percebi que a transcrição em tempo real é extremamente útil para reuniões rápidas e anotações instantâneas.

---

## 2. Criando um Projeto no Azure AI Foundry

- Configurar projeto e recursos no portal
- Acessar **Playground de Fala**

> **Insight:** Sempre verifique a região selecionada; a latência da transcrição em tempo real pode variar dependendo do local.

---

## 3. Teste: Conversão de Fala em Texto

- Carregar arquivo `WhatAICanDo.m4a`  
- Executar transcrição em tempo real  
- Revisar saída de texto

> **Insight:** A transcrição manteve boa precisão, mas o áudio deve estar claro e sem ruídos excessivos.  
> **Dica:** Arquivos longos podem ser divididos para melhor performance.

---

## 4. Limpeza de Recursos

- Excluir recursos não utilizados para evitar custos.

---

## 5. Insights Gerais

- A transcrição em tempo real é confiável e rápida  
- Útil para aplicações de produtividade (reuniões, entrevistas, legendas)  
- Documentação detalhada facilita replicação e compartilhamento dos testes
