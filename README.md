<h1 align="center">
      AlgoritmosDeOrdenamento </a>
</h1>

<h4 align="center">
	🚧   Concluido   🚧
</h4>

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre o projeto](#-sobre-o-projeto)
     * [ShellSort](#shellsort)
     * [QuickSort](#quicksort)
     * [QuickSort + Insertion Sort](#quicksort--insertion-sort)
     * [Radix Sort](#radix-sort)
   * [Funcionalidades](#gear-funcionalidades)
   * [Testes](#clipboard-testes)
   * [Complexidade](#chart_with_upwards_trend-complexidade)

<!--te-->


## 💻 Sobre o projeto

Este programa tem como objetivo analisar vários algoritmos de ordenamento, exportando para excel os tempos de execução para vários valores de estudo 

---
## ShellSort


## QuickSort


## QuickSort + Insertion Sort


## Radix Sort


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
