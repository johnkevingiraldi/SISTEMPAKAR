# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:16:02 2021

@author: ASUS
"""

# Sistem-Pakar
Pengumpulan tugas mengenai materi DFS dan BFS atas nama John Kevin Giraldi (1184049) DFS dan DBS

#DFS adalah Algoritma yang berkebalikan dari BFS yang melakukan perhitungan secara terurut dari terawal, sedangkan DFS melakukan perhitungan secara terurut dari urutan terakhir.

#Dibawah merupakan function untuk menampung graph,start,dan visited none ini untuk membuat visited kosong dan dibawah kodingan terdapat if yang jika visited nya sma dengan none maka visited akan di set dan akan ditambahkanketika kodingan di jalankan

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

#Dibawah ini akan di mulai (start) lalu akan di perlihatkan graphnya. Ini akan dilakukan terus berulang kali lalu akan berhenti ketika sudah sesuai graphic yang ditentukan.

print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


*dan yang di bawah ini adalah graph nya
graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')


#BFS adalah  salah satu Algoritma pencarian jalur sederhana, dimana pencarian dimulai dari titik awal, kemudian dilanjutkan ke semua cabang titik tersebut secara terurut.

#Dibawah ini ada function BFS yang menampung graph dan root yang didalam nya terdapat  visited quieue yang menampung set dari data dan setelah itu akan di masukan ke root dan setelah itu queue akan di lakukan pengulangan while yang menampung deque yang merupakan bagian dari queue dan akan di tampilkan data sesuai queue nya dan setelah itu jika tidak ada yang visited akan di tampung dengan jumlah neighbor ang berkunjung

def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

      
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

#Dibawah ini untuk menampung graphnya lalu akan memunculkan hasil dari BFS
if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is bfs: ")
    bfs(graph, 0)