#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from graphviz import Graph
import string

class AdjListGraph:
    def __init__(self):
        self.adj = dict()  # Список смежности
        self.attributes = dict()  # Список атрибутов вершин

    def add_vertices(self, n):
        """ Добавить n вершн в граф.
        :param int n: колиичество вершин для добавления
        """
        for i in range(n):
            self.adj.append(list())
            self.attributes.append({})

    def remove_vertex(self, v):
        """ Удалить вершину из графа
        :param int v: индекс вершинаы графа
        """
        self.adj.pop(v)
        self.attributes.pop(v)

    def number_of_vertices(self):
        """ Возвращает количество вершин графа
        :rtype: int
        """
        return len(self.adj)

    def add_edge(self, u, v):
        """ Добавить ребро, соединяющее вершины с индексами u и v
        :param int u: индекс вершины графа
        :param int v: индекс вершины графа
        """
        self.adj[u].add(v)
        self.adj[v].add(u)

    def remove_edge(self, u, v):
        """ Удалить ребро, соединяющее вершины с индексами u и v
        :param int u: индекс вершины графа
        :param int v: индекс вершины графа
        """
        self.adj[u].remove(v)
        self.adj[v].remove(u)

    def number_of_edges(self):
        """ Возвращает количество ребер в графе
        :rtype: int
        """
        count = 0
        for i in self.adj:
            for j in i:
                count += 1
        return count // 2

    def neighbors(self, v):
        """ Возвращает список индексов вершин, соседних с данной
        :param int v: индекс вершины графа
        :rtype: list of int
        """
        return list(self.adj[v])

    def draw(self, filename='test.gv'):
        """
        Отрисовывает граф используя библиотеку Graphviz. Больше примеров:
        https://graphviz.readthedocs.io/en/stable/examples.html
        """
        g = Graph('G', filename=filename, format='png')

        for v, attr in self.attributes.items():
            if 'color' in attr:
                g.attr('node', style='filled', fillcolor=attr['color'])
                if attr['color'] == 'black':
                    g.attr('node', fontcolor='white')
                else:
                    g.attr('node', fontcolor='black')
            else:
                g.attr('node', style='', color='', fontcolor='', fillcolor='')

            text = ''
            if 'name' in attr:
                text += '{} '.format(attr['name'])
            text += '({})'.format(v)
            for k, a in attr.items():
                if k == 'name':
                    continue
                if k == 'color':
                    continue
                text += '\n{}: {}'.format(k, a)

            g.node(str(v), text)

        for u in self.adj.keys():
            for v in self.adj[u]:
                if u <= v:
                    g.edge(str(u), str(v))

        g.view()


def main():
    g = AdjListGraph()
    g.add_vertices(5)
    for i, c in zip(range(5), string.ascii_lowercase):
        g.attributes[i]['name'] = c

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.remove_edge(1, 2)
    print(g.number_of_edges())
    print(g.number_of_vertices())
    print(g.neighbors(1))
    print(g.adj)
    print(g.attributes)


g.draw()


if __name__ == "__main__":
    main()