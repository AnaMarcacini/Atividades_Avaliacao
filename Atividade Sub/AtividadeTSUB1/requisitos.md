Data de entrega : antes da P4


# Requisitos
-sumario
- Conta - ok
- Jogos  - ok
- feedback - ok
- reembolso  --> dentro de conta
- compra --> dentro de conta 
- prazo // tempo
- trofeús 
- usuários
- login
- Códigos



# Conta 
- dinheiro
(programa antigo)
- dados de pagamento
- perfil - jogos
data da compra - (prazo de arrependimento)

        LINKS
        reembolso
        compra programa já feito.
        Usuario compra o jogo e dá para outro usuario
        

# Jogos
- quais jogos
-  preço
- Jogos linkados semelhantes
- Usuario compra o jogo e dá para outro usuario

# feedback
* perfil do jogo

        Link com jogo
        
* usuario

        Link com o usuario --> ele tem o jogo? // enfatizar que foi ele que comentou

# prazo // tempo
- contador de tempo 

    Usado por --> reembolso dentro de conta e talvez dentro de cliente

        Opcional: Contador de horas de jogo



# trofeús 
- vitórias
- conquistas
- medalhas
- 

# usuários
- Nome/ nickname
- Link com a conta ?

        possibilidade de merge com usuario
        Login
        Usuario compra o jogo e dá para outro usuario

## Busca
    Usuário
    Jogos
    temas de jogo (ação, arcade, etc)
    contas // transferencia de jogos de um para o outro venda entre usuarios


</br></br></br></br></br></br></br></br>
#################################################
</br></br>


# Notas Proof 
## Classes
- Usuario
- Jogo
- Plataforma
- Transação
- Conta
- Perfil
- Pagamento -- metodo de pagamento - filhos

        #FILHOS
        - Cartão
                - credito
                - Debito
        - Boleto
        - Pix
        - MercadoPago
        - PayPal
        - Credito da Conta (variavel da conta)

- Feedback
       
                
- Trofeus 
- Cupom -> expira
- Pontos Promocionais
- Cartão Presente
- Carrinho de compras

        minhas ideias:
                vetor de produtos(no caso jogos)
                valor total (usado depois em metodo de pagamento e para aplicar descontas (compras a cima de....))
#

## Classes com Enumeração
- Usuario
- Jogo
        
        Enumerações 
                Ação
                RPG
                JRPG
                MOBA
                Shooter
                FPS
                ......
- Plataforma

        Enumerações
                PC
                        WINDOWS
                        lINUX
                        MACOS
                PS5
                PS4
                XBOX_SX
                XBOX_ONE
                SWITCH
                MOBILE
- Transação
- Conta
- Perfil
- Pagamento -- metodo de pagamento - filhos

        #FILHOS
        - Cartão
                - credito
                - Debito
        - Boleto
        - Pix
        - MercadoPago
        - PayPal
        - Credito da Conta (variavel da conta)

- Feedback
        Enumerações 
                Positivo 
                Negativo
                Neutro

- Trofeus -- Enumerações 

        Enumerações : 
                Platina
                Ouro
                Prata
                Bronze
                Ferro
- Cupom -> expira
        
        Enumerações
                Desconto
                CashBack
                Pontos Promocionais
                Brinde
- Pontos Promocionais
- Cartão Presente

        Enumerações:
                Jogo 
                Creditos
- Carrinho de compras

        minhas ideias:
                vetor de produtos(no caso jogos)
                valor total (usado depois em metodo de pagamento e para aplicar descontas (compras a cima de....))
#




























































</br></br></br></br></br></br></br></br></br></br></br></br>

<details>
  <summary> <H1> ⭐️NOTAS de Aula </H1>
 </summary>
Waterfall = Começar a codar direto sem falar com o cliente

--> Ruim 
mudanças do cliente
mal entendimento do cliente sobre o produto
prazo errado

--> melhor alternativa Aoyle --> cliente participa da conversa

  </details>