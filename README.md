# EDII - Projeto Final [3ª Unidade]


Discentes:

Arthur Felipe Rodrigues Costa

Carlos Antonio Miranda Filho

Igor Cirne Borges de Oliveira

Este projeto tem como propósito analisar o perfil de duas diferentes cidades e comparar suas estruturas, mais especificamente suas estradas e áreas voltadas para ciclovia. Para isso, vamos extrair informações das redes através de informações do OpenStreetMap.


Inicialmente vamos usar Tibau do Sul, no estado do Rio Grande do Norte, como referência para pegarmos essas informações através do número de nós e arestas, densidade, comprimento total das ruas e medidas de centralidades. A partir daí, vamos comparar algumas dessas referências no momento em que alteramos a rede para ciclovias e refletirmos sobre mobilidade e planejamento urbano da cidade. Após Tibau do Sul, vamos usar a cidade de Gramado, no Rio Grande do Sul, para extrairmos os mesmos dados e fazer comparações com a cidade objeto de nosso estudo e gerar possíveis soluções sobre mobilidade urbana e planejamento de cidades mais acessíveis para ciclistas. Para ambas, serão usadas bibliotecas do OpenStreetMap (osmnx) e NetworkX (networkx) via linguagem Python para obtermos os dados geográficos e das redes de ambas as cidades. Outra cidade a ser comparada será Florianópolis, no estado de Santa Catarina.


O motivo pelo qual Tibau do Sul foi a cidade a ser focada foi que, por ser uma cidade com uma praia de destaque turístico internacional, é interessante que se possa pensar em um esforço para melhorar a mobilidade urbana e investir em meios benéficos de redução da poluição do ar pelo ciclismo. Embora isso sirva de estímulo também para se pensar em manter uma boa qualidade de vida, no Brasil ainda há um pequeno número de ciclovias, incluindo as capitais, onde apenas 4% cresceu de 2022 para 2023, segundo a Aliança Bike (Associação Brasileira do Setor de Bicicletas). Outro problema é que áreas sem ciclovias significa que os ciclistas terão que dividir espaços nas estradas com os motoristas e motociclistas, o que pode acarretar em acidentes de trânsito.


Para analisarmos, foram obtidos os grafos da centralidade intermediadora (betwenness centrality) tanto para as áreas de rodovia quanto de ciclovia. Este tipo de centralidade é importante para obtermos o fluxo de informação da rede, pegando um nó e calculando os caminhos mais curtos de outros nós da rede. Em uma cidade, esse tipo de grafo serve para pegarmos “pontes” importantes que ligam um ponto a outro numa cidade, não sendo possível fazer o trajeto em alguma localidade sem passar por elas. Na parte de Tibau do Sul, a parte crítica dessa centralidade encontra-se na cor amarela e ela se liga à Praia de Pipa. Dentro de Pipa, por sua vez, existem mais áreas dessa centralidade, o que indica a existência de caminhos que servem de ligações de um ponto a outro, sem eles o acesso a certas localidades não seria possível.

**Link do vídeo:** [Projeto Final - Análise de estruturas cicloviárias(Youtube)](https://youtu.be/WUe07l_UmYc)
**Link do Alternativo:** [Projeto Final - Análise de estruturas cicloviárias(Google Drive)](https://drive.google.com/file/d/1xKAq9sb3onKrWWH4IIlR_8a3sQUq5Rou/view?usp=drive_link)


**Referências:**


TOMAZELI, Tela. Metas do Gramado de Bicicleta. *Gramado de Bicicleta*, 2016. Disponível em: [Gramado de Bicicleta](http://gramadodebicicleta.blogspot.com). Acesso em: 15. dez. 2023.


ALIANÇA BIKE. **Ciclovias e ciclofaixas avançam 4% em 1 ano e capitais brasileiras atingem 4.365 km**. Disponível em: [Ciclovias e ciclofaixas avançam 4% em 1 ano e capitais brasileiras atingem 4.365 km](https://aliancabike.org.br/cicloviasnascapitais23/). Acesso em: 15 dez. 2023.


COSCIA, M. **The Atlas for the Aspiring Network Scientist**. IT – University of Copenhagen. 2021.


SOUZA, E. Mobilidade Estadão.**Florianópolis amplia 21% da malha cicloviária no primeiro semestre de 2023**. Disponível em: [Florianópolis amplia 21% da malha cicloviária no primeiro semestre de 2023](https://mobilidade.estadao.com.br/meios-de-transporte/bicicleta/florianopolis-amplia-21-da-malha-cicloviaria-no-primeiro-semestre-de-2023/). Acesso em: 16. dez. 2023.


Observatório da Bicicleta. **Florianópolis lidera ranking de ciclovias e ciclofaixas por habitante [dentre as capitais]**. Disponível em: [Florianópolis lidera ranking de ciclovias e ciclofaixas por habitante (dentre as capitais)](https://observatoriodabicicleta.org.br/florianopolis-lidera-ranking-de-ciclovias-e-ciclofaixas-por-habitante-dentre-as-capitais/). Acesso em: 16. dez. 2023.


Prefeitura de Florianópolis. **Florianópolis é a segunda Capital com mais ciclovias e ciclofaixas por habitante, segundo pesquisa da Aliança Bike**. Disponível em: [Florianópolis é a segunda Capital com mais ciclovias e ciclofaixas por habitante, segundo pesquisa da Aliança Bike](https://www.pmf.sc.gov.br/noticias/index.php?pagina=notpagina&noti=24739). Acesso em: 16. dez. 2023.



