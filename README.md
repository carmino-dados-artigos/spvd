# Repositório científico — variação dimensional longitudinal

Este repositório organiza os dados, scripts, resultados e o site complementar da pesquisa sobre predição da variação dimensional de concretos com macrofibras e aditivos compensadores de retração.

## GitHub Pages

Configure o GitHub Pages para publicar a partir da branch principal e da pasta `/docs`.

## Execução local do site

```bash
cd docs
python -m http.server 8000
```

Acesse `http://localhost:8000`.

## Estrutura

- `docs/`: site estático.
- `dados/`: dados originais e processados.
- `src/`: scripts dos nove experimentos.
- `resultados/`: arquivos produzidos pelos experimentos.
- `modelos/`: artefato do modelo.
- `relatorios/`: documentação consolidada e relatórios por experimento.

## Observação metodológica

Os 1.447 registros longitudinais derivam de 207 amostras experimentais e não devem ser interpretados como unidades independentes. A validação é agrupada por `amostra_id`.


## Visualização ampliada dos resultados

As páginas dos nove experimentos em `docs/experimentos/` incorporam o conteúdo dos relatórios Markdown correspondentes. A página `docs/dados.html` carrega a base longitudinal completa (1.447 registros × 19 colunas) com busca e paginação no navegador. Para que o carregamento do CSV funcione localmente, execute um servidor HTTP na pasta `docs`, por exemplo: `python -m http.server 8000`.
