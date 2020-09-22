# -*- coding: utf-8 -*-
from __future__ import print_function

inf = float('inf')
def relax(W, u, v, D, P):
    d = D.get(u,inf) + W[u][v] # 推定最短経路
    if d < D.get(v,inf): # 実際に最短経路の場合、
        D[v], P[v] = d, u # 推定値と親ノードを更新
        return True # 変更があったことを返す

def bellman_ford(G, s):
    D, P = {s:0}, {} # sに対して初期値ゼロの辞書; 親なし
    for i, rnd in enumerate(G): # n = len(G) ラウンド
        changed = False # 変化がない
        print("round", i)
        for u in G: # あるノードから...
            for v in G[u]: # ... あるノードへ...
                if relax(G, u, v, D, P): # uからvへ近道になっているか?
                    changed = True # はい! それならば近道になっている
                    print(D)
        if not changed:
            break # 変化がなかった場合: 終了
    else: # nラウンドで終了しなかった場合?
        raise ValueError('negative cycle') # 負の閉路を削除
    return D, P # そうでない場合、DとPは正しい

a, b, c, d, e, f, g, h = range(8)
G = {
a: {b:2, c:1, d:3, e:9, f:4},
b: {c:4, e:3},
c: {d:8},
d: {e:7},
e: {f:5},
f: {c:2, g:2, h:2},
g: {f:1, h:6},
h: {f:9, g:8}
}

bellman_ford(G, a)
