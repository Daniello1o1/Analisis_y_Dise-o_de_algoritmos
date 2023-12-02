import time
class Graph():
    def __init__(self):
        self.vertex = []
        self.edges = []
    def add_vertex(self, vertex):
        self.vertex.append(vertex)
    def add_edges(self, vertex1, vertex2, pond):
        sw1 = False
        sw2 = False
        i = 0
        while sw1 == False and i < len(self.vertex):
            sw1 = True if self.vertex[i] == vertex1 else False
            i = i + 1
        i = 0
        while sw2 == False and i < len(self.vertex):
            sw2 = True if self.vertex[i] == vertex2 else False
            i = i + 1
        if sw1 and sw2:
            self.edges.append([vertex1, vertex2, pond])
        elif sw1 == False:
            print(f"El vertice {vertex1} no existe")
        else:
            print(f"El vertice {vertex2} no existe")
    def dijkstra1(self, start, end):

        tab = []
        for i in range(0, len(self.vertex)):
            tab.append([self.vertex[i],["",0]])
        return self.dijkstra2(tab,start,end,1)
        
        
    def dijkstra2(self, tab, start, end, c):
        if start == end:
            print(tab)
            pos = 0
            for i in range(len(tab)):
                if tab[i][0] == start:
                    pos = i
            min = tab[pos][1][1]
            for i in range(1,c):
                if tab[pos][i][1] ==0:
                    min = tab[pos][i+1][1]
                elif tab[pos][i][1]<min:
                    min = tab[pos][i][1]
            return min
        else:
            if c > 1:
                n = 0
                for i in range(0,len(tab)):
                    if tab[i][0] == start:
                        n = tab[i][c-1][1]
                for i in range(0, len(self.edges)):
                    if self.edges[i][0] == start:
                        for j in range(0,len(tab)):
                            if self.edges[i][1] == tab[j][0]:
                                tab[j].append([self.edges[i][0],self.edges[i][2]+n])
                            else:
                                tab[j].append([tab[j][c-1][0],tab[j][c-1][1]])
            else:
                for i in range(0, len(self.edges)):
                    if self.edges[i][0] == start:
                        for j in range(0,len(tab)):
                            if self.edges[i][1] == tab[j][0]:
                                tab[j][c][0] = "A"
                                tab[j][c][1] += self.edges[i][2]
            print(tab)
            i = 0
            while i < len(tab):
                if tab[i][0] == start:
                    tab.pop(i)
                i += 1
            
            if c > 1:
                for i in range(0, len(tab)):
                    if tab[i][c][1] > tab[i][c-1][1] and tab[i][c-1][1]!=0:
                        tab[i][c][1] = tab[i][c-1][1]
                        tab[i][c][0] = tab[i][c-1][0]
            
            piv = tab[0][0]
            min = tab[0][c][1]
            for i in range(0, len(tab)):
                if tab[i][c][1] < min and tab[i][c][1] !=0:
                    min = tab[i][c][1]
                    piv = tab[i][0]
            
            return self.dijkstra2(tab,piv,end,c+1)
    def dijTime(self,start,end):
        inicio_T = time.time()
        r = self.dijkstra1(start,end)
        final_T = time.time()
        dif_T = final_T - inicio_T
        print("Tiempo de ejecucion: ",dif_T)
        return r
        
                        
        
grafo1 = Graph()
grafo2 = Graph()
grafo3 = Graph()
grafo4 = Graph()
grafo5 = Graph()
grafo1.add_vertex("A")
grafo1.add_vertex("B")
grafo1.add_vertex("C")
grafo1.add_vertex("D")
grafo1.add_vertex("E")
grafo1.add_edges("A","C",30)
grafo1.add_edges("A","B",100)
grafo1.add_edges("B","C",20)
grafo1.add_edges("C","D",10)
grafo1.add_edges("D","B",15)
grafo1.add_edges("C","E",60)
grafo1.add_edges("D","E",50)
print("El camino mas corto entre A y E es de ", grafo1.dijTime("A","E"))
grafo2.add_vertex("A")
grafo2.add_vertex("B")
grafo2.add_vertex("C")
grafo2.add_vertex("D")
grafo2.add_vertex("E")
grafo2.add_edges("A","C",1)
grafo2.add_edges("A","B",3)
grafo2.add_edges("C","B",7)
grafo2.add_edges("C","D",2)
grafo2.add_edges("D","B",5)
grafo2.add_edges("B","E",1)
grafo2.add_edges("D","E",7)
print("El camino mas corto entre A y E es de ", grafo2.dijTime("A","E"))
grafo3.add_vertex("A")
grafo3.add_vertex("B")
grafo3.add_vertex("C")
grafo3.add_vertex("D")
grafo3.add_edges("A","C",8)
grafo3.add_edges("A","B",5)
grafo3.add_edges("B","C",9)
grafo3.add_edges("C","D",6)
grafo3.add_edges("B","D",2)
print("El camino mas corto entre A y D es de ", grafo3.dijTime("A","D"))
grafo4.add_vertex("V1")
grafo4.add_vertex("V2")
grafo4.add_vertex("V3")
grafo4.add_vertex("V4")
grafo4.add_edges("V1","V2",6)
grafo4.add_edges("V1","V4",3)
grafo4.add_edges("V1","V3",4)
grafo4.add_edges("V4","V2",4)
grafo4.add_edges("V3","V2",3)
print("El camino mas corto entre V1 y V2 es de ", grafo4.dijTime("V1","V2"))
grafo5.add_vertex("A")
grafo5.add_vertex("B")
grafo5.add_vertex("C")
grafo5.add_vertex("E")
grafo5.add_edges("A","C",2)
grafo5.add_edges("A","B",3)
grafo5.add_edges("A","E",6)
grafo5.add_edges("B","E",9)
grafo5.add_edges("C","E",9)
print("El camino mas corto entre A y E es de ", grafo5.dijTime("A","E"))
