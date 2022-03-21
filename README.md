<h1 align="center">
      AlgoritmosDeOrdenamento </a>
</h1>

<h4 align="center">
	🚧    Em construção...   🚧
</h4>

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre o projeto](#-sobre-o-projeto)
     * [ShellSort](#shellsort)
     	* [Como funciona](#como-funciona) 
     * [QuickSort](#quicksort)
     * [QuickSort + Insertion Sort](#quicksort--insertion-sort)
     * [Radix Sort](#radix-sort)
     	* [Eficiência](#eficiência)
   * [Funcionalidades](#gear-funcionalidades)
   * [Testes](#clipboard-testes)
   * [Complexidade](#chart_with_upwards_trend-complexidade)

<!--te-->

## 💻 Sobre o projeto

Este programa tem como objetivo analisar vários algoritmos de ordenamento, exportando para excel os tempos de execução para vários valores de estudo 

---


## QuickSort + Insertion Sort

## Radix Sort

Na ciência da computação, ** radix sort ** é uma classificação inteira não comparativa 
algoritmo que classifica os dados com chaves inteiras agrupando chaves por indivíduo 
dígitos que compartilham a mesma posição significativa e valor. Uma notação posicional
é obrigatório, mas porque os inteiros podem representar cadeias de caracteres 
(por exemplo, nomes ou datas) e números de ponto flutuante especialmente formatados, raiz 
sort não se limita a inteiros.


### Eficiência

O tópico da eficiência da classificação raiz em comparação com outros algoritmos de classificação é 
um tanto complicado e sujeito a muitos mal-entendidos. Se radix
sort é igualmente eficiente, menos eficiente ou mais eficiente do que o melhor 
algoritmos baseados em comparação dependem dos detalhes das suposições feitas. 
A complexidade da ordenação de raiz é `O (wn)` para chaves `n` que são inteiros de tamanho de palavra` w`. 
Às vezes, `w` é apresentado como uma constante, o que tornaria a ordenação radix melhor 
(para `n` suficientemente grande) do que os melhores algoritmos de classificação baseados em comparação, 
em que todos realizam comparações `O (n log n)` para classificar as chaves `n`. No entanto, em
geral `w` não pode ser considerado uma constante: se todas as chaves` n` são distintas, 
então `w` tem que ser pelo menos` log n` para uma máquina de acesso aleatório ser capaz de 
armazene-os na memória, o que dá, na melhor das hipóteses, uma complexidade de tempo `O (n log n)`. Este
pareceria tornar a classificação radix no máximo igualmente eficiente quanto a melhor 
classificações baseadas em comparação (e pior se as chaves forem muito mais longas do que `log n`).

![Radix Sort](https://www.researchgate.net/publication/291086231/figure/fig1/AS:614214452404240@1523451545568/Simplistic-illustration-of-the-steps-performed-in-a-radix-sort-In-this-example-the.png)




---

## :gear: Funcionalidades

- [x] Criar vários tipos de arrays numéricos
- [x] Ordenar arrays numéricos
- [x] Exportar dados para excel

## :clipboard: Testes

Para os testes realizados usaram-se arrays de 500.000 até 10.000.000 elementos, com intervalos de 500.000.\
Os arrays podiam estar desordenados, ordenados decrescentemete, 99% ordenados e 95% ordenados.

## :chart_with_upwards_trend: Complexidade

| Nome                  | Melhor          | Média               | Pior                | Mémoria   | Estável   | comentários |
| --------------------- | :-------------: | :-----------------: | :-----------------: | :-------: | :-------: | :--------   |
| **Insertion sort**    | n               | n<sup>2</sup>       | n<sup>2</sup>       | 1         | Sim       |             |
| **Quick sort**        | n&nbsp;log(n)   | n&nbsp;log(n)       | n<sup>2</sup>       | log(n)    | Não       | O Quicksort geralmente é feito no local com o espaço de pilha O  O(log(n)) stack space |
| **Shell sort**        | n&nbsp;log(n)   | depende da sequência de lacunas | n&nbsp;(log(n))<sup>2</sup>     | 1      | Não    |                   |
| **Radix sort**        | n * k           | n * k               | n * k               | n + k     | Sim       | k - comprimento da chave mais longa |
