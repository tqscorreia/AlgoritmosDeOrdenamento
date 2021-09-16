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
## ShellSort

Shellsort é um tipo de comparação no local. Pode ser visto como uma generalização do Bubble Sort ou Insertion Sort.\
O método começa classificando pares de elementos distantes um do outro, então progressivamente reduz a lacuna entre os elementos a serem comparados.\
Inicia com elementos distantes, pode mover alguns elementos fora do lugar 
elementos na posição mais rápido do que um vizinho mais próximo simples 
intercâmbio.

![Shellsort](https://upload.wikimedia.org/wikipedia/commons/d/d8/Sorting_shellsort_anim.gif)
## Como funciona
Para nosso exemplo e facilidade de compreensão, usamos o intervalo de `4`. Faça uma sub-lista virtual de todos os valores localizados no intervalo de 4 posições. Aqui estes valores são `{35, 14}`, `{33, 19}`, `{42, 27}` e `{10, 44}`

![Shellsort](https://www.tutorialspoint.com/data_structures_algorithms/images/shell_sort_gap_4.jpg)

Comparamos os valores em cada sub-lista e os trocamos (se necessário) na matriz original. Após esta etapa, a nova matriz deve ser semelhante a esta

![Shellsort](https://www.tutorialspoint.com/data_structures_algorithms/images/shell_sort_step_1.jpg)

Então, pegamos o intervalo de 2 e esta lacuna gera duas sublistas

- `{14, 27, 35, 42}`, `{19, 10, 33, 44}`

![Shellsort](https://www.tutorialspoint.com/data_structures_algorithms/images/shell_sort_gap_2.jpg)

Comparamos e trocamos os valores, se necessário, na matriz original. Após esta etapa, a matriz deve ficar assim

![Shellsort](https://www.tutorialspoint.com/data_structures_algorithms/images/shell_sort_step_2.jpg)

> UPD: na imagem abaixo há um erro de digitação e a matriz de resultados deve estar  `[14, 10, 27, 19, 35, 33, 42, 44]`.

Por fim, classificamos o restante do array usando o intervalo de valor 1. A classificação por shell usa a classificação por inserção para classificar o array.

![Shellsort](https://www.tutorialspoint.com/data_structures_algorithms/images/shell_sort.jpg)

## QuickSort

Quicksort é um algoritmo de divisão e conquista.
Quicksort primeiro divide uma grande matriz em duas menores 
submatrizes: os elementos baixos e os elementos altos.
O Quicksort pode então classificar recursivamente as submatrizes

As etapas são:

1. Escolha um elemento, denominado pivô, da matriz.
2. Particionamento: reordene a matriz para que todos os elementos com 
valores menores que o pivô vêm antes do pivô, enquanto todos 
elementos com valores maiores do que o pivô vêm depois dele 
(valores iguais podem ser usados em qualquer direção). Após este particionamento,
o pivô está em sua posição final. Isso é chamado de
operação de partição.
3. Aplique recursivamente as etapas acima à submatriz de 
elementos com valores menores e separadamente para o 
submatriz de elementos com valores maiores.

Visualização animada do algoritmo quicksort.

![Quicksort](https://www.tutorialspoint.com/data_structures_algorithms/images/quick_sort_partition_animation.gif)


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
