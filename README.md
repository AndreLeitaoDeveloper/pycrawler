# pycrawler
crawler testing python

A ideia Geral é fazer um parse a uma RSS feed, e gravar os elementos como campos numa collection 'noticias' em mongoDB. Verificar se a noticia ja está inserida. (abordar a melhor forma para tal).

Pensar nos recursos necessarios, exemplo: pymongo para falar com o mongo, algo que faça parse ao xml (google it:p )

para instalar modulos do python em baixo como exemplo:
> pip install pymongo


##1 - fazer um request a http://feeds.feedburner.com/PublicoRSS?format=xml


##2 - fazer parse aos elementos da rss (xml)


### Exemplo do xml da RSS
```
<item>
      <title>O riso é um campo de batalha (mas teremos sempre Lionel Richie)</title>
      <description>Em &lt;i&gt;AH/ HA&lt;/i&gt;, Lisbeth Gruwez baralha aquilo que normalmente pensamos sobre o riso. Esta sexta, no Teatro Campo Alegre, no Porto, a coreógrafa belga mostra a estranheza como modo de superação.&lt;img src="http://feeds.feedburner.com/~r/PublicoRSS/~4/tGXCdGwgxeM" height="1" width="1" alt=""/&gt;</description>
      <link>https://www.publico.pt/culturaipsilon/noticia/o-riso-e-um-campo-de-batalha-mas-teremos-sempre-lionel-richie-1752073</link>
      <category>Cultura-Ípsilon</category>
      <pubDate>Fri, 25 Nov 2016 09:54:00 GMT</pubDate>
      <dc:creator>Mariana Duarte</dc:creator>
      <guid>//www.publico.pt/culturaipsilon/noticia/o-riso-e-um-campo-de-batalha-mas-teremos-sempre-lionel-richie-1752073</guid>
    </item>
```
