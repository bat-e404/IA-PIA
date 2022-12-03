import sys
import matplotlib.pyplot as plt
import networkx as nx
 
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        ''' Este método asegura que el gráfico sea simétrico. En otras palabras, si hay una ruta del nodo A al B con un valor V, debe haber una ruta del nodo B al nodo A con un valor V. '''
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Devuelve los nodos del gráfico"
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Devuelve los vecinos de un nodo"
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Devuelve el valor de un borde entre dos nodos"
        return self.graph[node1][node2]


def print_result(previous_nodes, shortest_path, start_node, target_node):
        path = []
        node = target_node
    
        while node != start_node:
          path.append(node)
          node = previous_nodes[node]
 
        # Add the start node manually
        path.append(start_node)
        km = shortest_path[target_node]* 0.001
        t = km / 36 
        t *= 60
        t = int(t)
        print("Valor optimo - Distancia: {} Km.".format(str(km)))
        print("Tiempo total ≈ {} minutos.".format(str(t)))
        print(" -> ".join(reversed(path)))
        
def dijkstra_algorithm(graph, start_node):
        unvisited_nodes = list(graph.get_nodes())
        
        # Usaremos este dict para ahorrar el costo de visitar cada nodo y actualizarlo a medida que avanzamos en el gráfico  
        shortest_path = {}
 
       # Usaremos este dict para guardar la ruta más corta conocida a un nodo encontrado hasta ahora
        previous_nodes = {}
 
        # Usaremos max_value para inicializar el valor "infinito" de los nodos no visitados
        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        # Sin embargo, inicializamos el valor del nodo inicial con 0 
        shortest_path[start_node] = 0
    
        # El algoritmo se ejecuta hasta que visitamos todos los nodos
        while unvisited_nodes:
            # El bloque de código a continuación encuentra el nodo con la puntuación más baja
            current_min_node = None
            for node in unvisited_nodes: # Iterar sobre los nodos
                if current_min_node == None:
                   current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                   current_min_node = node
                
            # El bloque de código a continuación recupera los vecinos del nodo actual y actualiza sus distancias
            neighbors = graph.get_outgoing_edges(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    # También actualizamos la mejor ruta al nodo actual
                    previous_nodes[neighbor] = current_min_node
 
            # Después de visitar a sus vecinos, marcamos el nodo como "visitado"
            unvisited_nodes.remove(current_min_node)
    
        return previous_nodes, shortest_path

nodes = ['Pantitlan', 'Zaragoza', 'Gomez Farias', 'Boulevard Puerto Aereo', 'Balbuena', 'Moctezuma', 'San Lazaro', 'Candelaria', 'Merced', 'Pino Suarez', 'Isabel la Catolica', 'Salto del Agua', 'Balderas', 'Cuauhtemoc', 'Insurgentes', 'Sevilla', 'Chapultepec', 'Juanacatlan', 'Observatorio', 'Cuatro Caminos', 'Panteones', 'Tacuba', 'Cuitlahuac', 'Popotla', 'Colegio Militar', 'Normal', 'San Cosme', 'Revolucion', 'Hidalgo', 'Bellas Artes', 'Allende', 'Zocalo', 'San Antonio Abad', 'Chabacano', 'Viaducto', 'Xola', 'Villa de Cortes', 'Nativitas', 'Portales', 'Ermita', 'General Anaya', 'Tasquena', 'Indios Verdes', 'Deportivo 18 de Marzo', 'Potrero', 'La Raza', 'Tlatelolco', 'Guerrero', 'Juarez', 'Ninos Heroes', 'Hospital General', 'Centro Medico', 'Etiopia/Plaza de la Transparencia', 'Eugenia', 'Division del Norte', 'Coyoacan', 'Viveros/Derechos Humanos', 'Miguel Angel de Quevedo', 'Copilco', 'Universidad', 'Santa Anita', 'Fray Servando', 'Morelos', 'Canal del Norte', 'Consulado', 'Bondojito', 'Talisman', 'Martin Carrera', 'Politecnico', 'Instituto del Petroleo', 'Autobuses del Norte', 'Misterios', 'Valle Gomez', 'Eduardo Molina', 'Aragon', 'Oceania', 'Terminal Aerea', 'Hangares', 'El Rosario', 'Tezozomoc', 'Azcapotzalco', 'Ferreria', 'Norte 45', 'Vallejo', 'Lindavista', 'La Villa/Basilica', 'Aquiles Serdan', 'Camarones', 'Refineria', 'San Joaquin', 'Polanco', 'Auditorio', 'Constituyentes', 'Tacubaya', 'San Pedro de los Pinos', 'San Antonio', 'Mixcoac', 'Barranca del Muerto', 'Garibaldi', 'San Juan de Letran', 'Doctores', 'Obrera', 'La Viga', 'Coyuya', 'Iztacalco', 'Apatlaco', 'Aculco', 'Escuadron 201', 'Atlalilco', 'Iztapalapa', 'Cerro de la Estrella', 'UAM I', 'Constitucion de 1917', 'Puebla', 'Ciudad Deportiva', 'Velodromo', 'Mixiuhca', 'Jamaica', 'Lazaro Cardenas', 'Chilpancingo', 'Patriotismo', 'Agricola Oriental', 'Canal de San Juan', 'Tepalcates', 'Guelatao', 'Penon Viejo', 'Acatitla', 'Santa Marta', 'Los Reyes', 'La Paz', 'Ciudad Azteca', 'Plaza Aragon', 'Olimpica', 'Ecatepec', 'Muzquiz', 'Rio de los Remedios', 'Impulsora', 'Nezahualcoyotl', 'Villa de Aragon', 'Bosques de Aragon', 'Deportivo Oceania', 'Romero Rubio', 'Ricardo Flores Magon', 'Tepito', 'Lagunilla', 'Buenavista', 'Tlahuac', 'Tlaltenco', 'Zapotitlan', 'Nopalera', 'Olivos', 'Tezonco', 'Periferico Oriente', 'Calle 11', 'Lomas Estrella', 'San Andres Tomatlan', 'Culhuacan', 'Mexicaltzingo', 'Eje Central', 'Parque de los Venados', 'Zapata', 'Hospital 20 de Noviembre', 'Insurgentes Sur']

 
init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph["Pantitlan"]["Zaragoza"]=1320
init_graph["Pantitlan"]["Hangares"]=1644
init_graph["Pantitlan"]["Puebla"]=1380
init_graph["Pantitlan"]["Agricola Oriental"]=1409       
init_graph["Zaragoza"]["Gomez Farias"]=762
init_graph["Zaragoza"]["Pantitlan"]=1320
init_graph["Gomez Farias"]["Boulevard Puerto Aereo"]=611
init_graph["Gomez Farias"]["Zaragoza"]=762
init_graph["Boulevard Puerto Aereo"]["Balbuena"]=595    
init_graph["Boulevard Puerto Aereo"]["Gomez Farias"]=611
init_graph["Balbuena"]["Moctezuma"]=703
init_graph["Balbuena"]["Boulevard Puerto Aereo"]=595    
init_graph["Moctezuma"]["San Lazaro"]=478
init_graph["Moctezuma"]["Balbuena"]=703
init_graph["San Lazaro"]["Candelaria"]=866
init_graph["San Lazaro"]["Moctezuma"]=478
init_graph["San Lazaro"]["Morelos"]=1296
init_graph["San Lazaro"]["Ricardo Flores Magon"]=907
init_graph["Candelaria"]["Merced"]=698
init_graph["Candelaria"]["San Lazaro"]=866
init_graph["Candelaria"]["Morelos"]=1062
init_graph["Candelaria"]["Fray Servando"]=633
init_graph["Merced"]["Pino Suarez"]=745
init_graph["Merced"]["Candelaria"]=698
init_graph["Pino Suarez"]["San Antonio Abad"]=817
init_graph["Pino Suarez"]["Zocalo"]=745
init_graph["Pino Suarez"]["Merced"]=745
init_graph["Pino Suarez"]["Isabel la Catolica"]=382
init_graph["Isabel la Catolica"]["Salto del Agua"]=445
init_graph["Isabel la Catolica"]["Pino Suarez"]=382
init_graph["Salto del Agua"]["Balderas"]=458
init_graph["Salto del Agua"]["Isabel la Catolica"]=445
init_graph["Salto del Agua"]["San Juan de Letran"]=292
init_graph["Salto del Agua"]["Doctores"]=564
init_graph["Balderas"]["Cuauhtemoc"]=409
init_graph["Balderas"]["Salto del Agua"]=458
init_graph["Balderas"]["Ninos Heroes"]=665
init_graph["Balderas"]["Juarez"]=659
init_graph["Cuauhtemoc"]["Insurgentes"]=793
init_graph["Cuauhtemoc"]["Balderas"]=409
init_graph["Insurgentes"]["Sevilla"]=645
init_graph["Insurgentes"]["Cuauhtemoc"]=793
init_graph["Sevilla"]["Chapultepec"]=501
init_graph["Sevilla"]["Insurgentes"]=645
init_graph["Chapultepec"]["Juanacatlan"]=973
init_graph["Chapultepec"]["Sevilla"]=501
init_graph["Juanacatlan"]["Tacubaya"]=1158
init_graph["Juanacatlan"]["Chapultepec"]=973
init_graph["Observatorio"]["Tacubaya"]=1262
init_graph["Cuatro Caminos"]["Panteones"]=1639
init_graph["Panteones"]["Tacuba"]=1416
init_graph["Panteones"]["Cuatro Caminos"]=1639
init_graph["Tacuba"]["Cuitlahuac"]=637
init_graph["Tacuba"]["Panteones"]=1416
init_graph["Tacuba"]["Refineria"]=1295
init_graph["Tacuba"]["San Joaquin"]=1433
init_graph["Cuitlahuac"]["Popotla"]=620
init_graph["Cuitlahuac"]["Tacuba"]=637
init_graph["Popotla"]["Colegio Militar"]=462
init_graph["Popotla"]["Cuitlahuac"]=620
init_graph["Colegio Militar"]["Normal"]=516
init_graph["Colegio Militar"]["Popotla"]=462
init_graph["Normal"]["San Cosme"]=657
init_graph["Normal"]["Colegio Militar"]=516
init_graph["San Cosme"]["Revolucion"]=537
init_graph["San Cosme"]["Normal"]=657
init_graph["Revolucion"]["Hidalgo"]=587
init_graph["Revolucion"]["San Cosme"]=537
init_graph["Hidalgo"]["Bellas Artes"]=447
init_graph["Hidalgo"]["Revolucion"]=587
init_graph["Hidalgo"]["Guerrero"]=702
init_graph["Hidalgo"]["Juarez"]=251
init_graph["Bellas Artes"]["Allende"]=387
init_graph["Bellas Artes"]["Hidalgo"]=447
init_graph["Bellas Artes"]["Garibaldi"]=634
init_graph["Bellas Artes"]["San Juan de Letran"]=456
init_graph["Allende"]["Zocalo"]=602
init_graph["Allende"]["Bellas Artes"]=387
init_graph["Zocalo"]["Pino Suarez"]=745
init_graph["Zocalo"]["Allende"]=602
init_graph["San Antonio Abad"]["Chabacano"]=642
init_graph["San Antonio Abad"]["Pino Suarez"]=817
init_graph["Chabacano"]["Viaducto"]=774
init_graph["Chabacano"]["San Antonio Abad"]=642
init_graph["Chabacano"]["Obrera"]=1143
init_graph["Chabacano"]["La Viga"]=843
init_graph["Chabacano"]["Lazaro Cardenas"]=1000
init_graph["Chabacano"]["Jamaica"]=1031
init_graph["Viaducto"]["Xola"]=490
init_graph["Viaducto"]["Chabacano"]=774
init_graph["Xola"]["Villa de Cortes"]=698
init_graph["Xola"]["Viaducto"]=490
init_graph["Villa de Cortes"]["Nativitas"]=750
init_graph["Villa de Cortes"]["Xola"]=698
init_graph["Nativitas"]["Portales"]=924
init_graph["Nativitas"]["Villa de Cortes"]=750
init_graph["Portales"]["Ermita"]=748
init_graph["Portales"]["Nativitas"]=924
init_graph["Ermita"]["General Anaya"]=838
init_graph["Ermita"]["Portales"]=748
init_graph["Ermita"]["Eje Central"]=895
init_graph["Ermita"]["Mexicaltzingo"]=1805
init_graph["General Anaya"]["Tasquena"]=1330
init_graph["General Anaya"]["Ermita"]=838
init_graph["Tasquena"]["General Anaya"]=1330
init_graph["Indios Verdes"]["Deportivo 18 de Marzo"]=1166
init_graph["Deportivo 18 de Marzo"]["Potrero"]=966
init_graph["Deportivo 18 de Marzo"]["Indios Verdes"]=1166
init_graph["Deportivo 18 de Marzo"]["Lindavista"]=1075
init_graph["Deportivo 18 de Marzo"]["La Villa/Basilica"]=570
init_graph["Potrero"]["La Raza"]=1106
init_graph["Potrero"]["Deportivo 18 de Marzo"]=966
init_graph["La Raza"]["Tlatelolco"]=1445
init_graph["La Raza"]["Potrero"]=1106
init_graph["La Raza"]["Autobuses del Norte"]=975
init_graph["La Raza"]["Misterios"]=892
init_graph["Tlatelolco"]["Guerrero"]=1042
init_graph["Tlatelolco"]["La Raza"]=1445
init_graph["Guerrero"]["Hidalgo"]=702
init_graph["Guerrero"]["Tlatelolco"]=1042
init_graph["Guerrero"]["Buenavista"]=521
init_graph["Guerrero"]["Garibaldi"]=757
init_graph["Juarez"]["Balderas"]=659
init_graph["Juarez"]["Hidalgo"]=251
init_graph["Ninos Heroes"]["Hospital General"]=559
init_graph["Ninos Heroes"]["Balderas"]=665
init_graph["Hospital General"]["Centro Medico"]=653
init_graph["Hospital General"]["Ninos Heroes"]=559
init_graph["Centro Medico"]["Etiopia/Plaza de la Transparencia"]=1119
init_graph["Centro Medico"]["Hospital General"]=653
init_graph["Centro Medico"]["Chilpancingo"]=1152
init_graph["Centro Medico"]["Lazaro Cardenas"]=1059
init_graph["Etiopia/Plaza de la Transparencia"]["Eugenia"]=950
init_graph["Etiopia/Plaza de la Transparencia"]["Centro Medico"]=1119
init_graph["Eugenia"]["Division del Norte"]=715
init_graph["Eugenia"]["Etiopia/Plaza de la Transparencia"]=950
init_graph["Division del Norte"]["Zapata"]=794
init_graph["Division del Norte"]["Eugenia"]=715
init_graph["Coyoacan"]["Viveros/Derechos Humanos"]=908
init_graph["Coyoacan"]["Zapata"]=1153
init_graph["Viveros/Derechos Humanos"]["Miguel Angel de Quevedo"]=824
init_graph["Viveros/Derechos Humanos"]["Coyoacan"]=908
init_graph["Miguel Angel de Quevedo"]["Copilco"]=1295
init_graph["Miguel Angel de Quevedo"]["Viveros/Derechos Humanos"]=824
init_graph["Copilco"]["Universidad"]=1306
init_graph["Copilco"]["Miguel Angel de Quevedo"]=1295
init_graph["Universidad"]["Copilco"]=1306
init_graph["Santa Anita"]["Jamaica"]=758
init_graph["Santa Anita"]["Coyuya"]=968
init_graph["Santa Anita"]["La Viga"]=633
init_graph["Fray Servando"]["Candelaria"]=633
init_graph["Fray Servando"]["Jamaica"]=1033
init_graph["Morelos"]["Canal del Norte"]=910
init_graph["Morelos"]["Candelaria"]=1062
init_graph["Morelos"]["Tepito"]=498
init_graph["Morelos"]["San Lazaro"]=1296
init_graph["Canal del Norte"]["Consulado"]=884
init_graph["Canal del Norte"]["Morelos"]=910
init_graph["Consulado"]["Bondojito"]=645
init_graph["Consulado"]["Canal del Norte"]=884
init_graph["Consulado"]["Valle Gomez"]=679
init_graph["Consulado"]["Eduardo Molina"]=815
init_graph["Bondojito"]["Talisman"]=959
init_graph["Bondojito"]["Consulado"]=645
init_graph["Talisman"]["Martin Carrera"]=1129
init_graph["Talisman"]["Bondojito"]=959
init_graph["Martin Carrera"]["Talisman"]=1129
init_graph["Martin Carrera"]["La Villa/Basilica"]=1141
init_graph["Politecnico"]["Instituto del Petroleo"]=1188
init_graph["Instituto del Petroleo"]["Autobuses del Norte"]=1067
init_graph["Instituto del Petroleo"]["Politecnico"]=1188
init_graph["Instituto del Petroleo"]["Lindavista"]=1258
init_graph["Instituto del Petroleo"]["Vallejo"]=755
init_graph["Autobuses del Norte"]["La Raza"]=975
init_graph["Autobuses del Norte"]["Instituto del Petroleo"]=1067
init_graph["Misterios"]["Valle Gomez"]=969
init_graph["Misterios"]["La Raza"]=892
init_graph["Valle Gomez"]["Consulado"]=679
init_graph["Valle Gomez"]["Misterios"]=969
init_graph["Eduardo Molina"]["Aragon"]=860
init_graph["Eduardo Molina"]["Consulado"]=815
init_graph["Aragon"]["Oceania"]=1219
init_graph["Aragon"]["Eduardo Molina"]=860
init_graph["Oceania"]["Terminal Aerea"]=1174
init_graph["Oceania"]["Aragon"]=1219
init_graph["Oceania"]["Romero Rubio"]=809
init_graph["Oceania"]["Deportivo Oceania"]=863
init_graph["Terminal Aerea"]["Hangares"]=1153
init_graph["Terminal Aerea"]["Oceania"]=1174
init_graph["Hangares"]["Pantitlan"]=1644
init_graph["Hangares"]["Terminal Aerea"]=1153
init_graph["El Rosario"]["Tezozomoc"]=1257
init_graph["El Rosario"]["Aquiles Serdan"]=1615
init_graph["Tezozomoc"]["Azcapotzalco"]=973
init_graph["Tezozomoc"]["El Rosario"]=1257
init_graph["Azcapotzalco"]["Ferreria"]=1173
init_graph["Azcapotzalco"]["Tezozomoc"]=973
init_graph["Ferreria"]["Norte 45"]=1072
init_graph["Ferreria"]["Azcapotzalco"]=1173
init_graph["Norte 45"]["Vallejo"]=660
init_graph["Norte 45"]["Ferreria"]=1072
init_graph["Vallejo"]["Instituto del Petroleo"]=755
init_graph["Vallejo"]["Norte 45"]=660
init_graph["Lindavista"]["Deportivo 18 de Marzo"]=1075
init_graph["Lindavista"]["Instituto del Petroleo"]=1258
init_graph["La Villa/Basilica"]["Martin Carrera"]=1141
init_graph["La Villa/Basilica"]["Deportivo 18 de Marzo"]=570
init_graph["Aquiles Serdan"]["Camarones"]=1402
init_graph["Aquiles Serdan"]["El Rosario"]=1615
init_graph["Camarones"]["Refineria"]=952
init_graph["Camarones"]["Aquiles Serdan"]=1402
init_graph["Refineria"]["Tacuba"]=1295
init_graph["Refineria"]["Camarones"]=952
init_graph["San Joaquin"]["Polanco"]=1163
init_graph["San Joaquin"]["Tacuba"]=1433
init_graph["Polanco"]["Auditorio"]=812
init_graph["Polanco"]["San Joaquin"]=1163
init_graph["Auditorio"]["Constituyentes"]=1430
init_graph["Auditorio"]["Polanco"]=812
init_graph["Constituyentes"]["Tacubaya"]=1005
init_graph["Constituyentes"]["Auditorio"]=1430
init_graph["Tacubaya"]["San Pedro de los Pinos"]=1084
init_graph["Tacubaya"]["Constituyentes"]=1005
init_graph["Tacubaya"]["Observatorio"]=1262
init_graph["Tacubaya"]["Juanacatlan"]=1158
init_graph["Tacubaya"]["Patriotismo"]=1133
init_graph["San Pedro de los Pinos"]["San Antonio"]=606
init_graph["San Pedro de los Pinos"]["Tacubaya"]=1084
init_graph["San Antonio"]["Mixcoac"]=788
init_graph["San Antonio"]["San Pedro de los Pinos"]=606
init_graph["Mixcoac"]["Barranca del Muerto"]=1476
init_graph["Mixcoac"]["San Antonio"]=788
init_graph["Mixcoac"]["Insurgentes Sur"]=651
init_graph["Barranca del Muerto"]["Mixcoac"]=1476
init_graph["Garibaldi"]["Bellas Artes"]=634
init_graph["Garibaldi"]["Lagunilla"]=474
init_graph["Garibaldi"]["Guerrero"]=757
init_graph["San Juan de Letran"]["Salto del Agua"]=292
init_graph["San Juan de Letran"]["Bellas Artes"]=456
init_graph["Doctores"]["Obrera"]=761
init_graph["Doctores"]["Salto del Agua"]=564
init_graph["Obrera"]["Chabacano"]=1143
init_graph["Obrera"]["Doctores"]=761
init_graph["La Viga"]["Santa Anita"]=633
init_graph["La Viga"]["Chabacano"]=843
init_graph["Coyuya"]["Iztacalco"]=993
init_graph["Coyuya"]["Santa Anita"]=968
init_graph["Iztacalco"]["Apatlaco"]=910
init_graph["Iztacalco"]["Coyuya"]=993
init_graph["Apatlaco"]["Aculco"]=534
init_graph["Apatlaco"]["Iztacalco"]=910
init_graph["Aculco"]["Escuadron 201"]=789
init_graph["Aculco"]["Apatlaco"]=534
init_graph["Escuadron 201"]["Atlalilco"]=1738
init_graph["Escuadron 201"]["Aculco"]=789
init_graph["Atlalilco"]["Iztapalapa"]=732
init_graph["Atlalilco"]["Escuadron 201"]=1738
init_graph["Atlalilco"]["Mexicaltzingo"]=1922
init_graph["Atlalilco"]["Culhuacan"]=1671
init_graph["Iztapalapa"]["Cerro de la Estrella"]=717
init_graph["Iztapalapa"]["Atlalilco"]=732
init_graph["Cerro de la Estrella"]["UAM I"]=1135
init_graph["Cerro de la Estrella"]["Iztapalapa"]=717
init_graph["UAM I"]["Constitucion de 1917"]=1137
init_graph["UAM I"]["Cerro de la Estrella"]=1135
init_graph["Constitucion de 1917"]["UAM I"]=1137
init_graph["Puebla"]["Ciudad Deportiva"]=800
init_graph["Puebla"]["Pantitlan"]=1380
init_graph["Ciudad Deportiva"]["Velodromo"]=1110
init_graph["Ciudad Deportiva"]["Puebla"]=800
init_graph["Velodromo"]["Mixiuhca"]=821
init_graph["Velodromo"]["Ciudad Deportiva"]=1110
init_graph["Mixiuhca"]["Jamaica"]=942
init_graph["Mixiuhca"]["Velodromo"]=821
init_graph["Jamaica"]["Chabacano"]=1031
init_graph["Jamaica"]["Mixiuhca"]=942
init_graph["Jamaica"]["Fray Servando"]=1033
init_graph["Jamaica"]["Santa Anita"]=758
init_graph["Lazaro Cardenas"]["Centro Medico"]=1059
init_graph["Lazaro Cardenas"]["Chabacano"]=1000
init_graph["Chilpancingo"]["Patriotismo"]=955
init_graph["Chilpancingo"]["Centro Medico"]=1152
init_graph["Patriotismo"]["Tacubaya"]=1133
init_graph["Patriotismo"]["Chilpancingo"]=955
init_graph["Agricola Oriental"]["Canal de San Juan"]=1093
init_graph["Agricola Oriental"]["Pantitlan"]=1409
init_graph["Canal de San Juan"]["Tepalcates"]=1456
init_graph["Canal de San Juan"]["Agricola Oriental"]=1093
init_graph["Tepalcates"]["Guelatao"]=1161
init_graph["Tepalcates"]["Canal de San Juan"]=1456
init_graph["Guelatao"]["Penon Viejo"]=2206
init_graph["Guelatao"]["Tepalcates"]=1161
init_graph["Penon Viejo"]["Acatitla"]=1379
init_graph["Penon Viejo"]["Guelatao"]=2206
init_graph["Acatitla"]["Santa Marta"]=1100
init_graph["Acatitla"]["Penon Viejo"]=1379
init_graph["Santa Marta"]["Los Reyes"]=1783
init_graph["Santa Marta"]["Acatitla"]=1100
init_graph["Los Reyes"]["La Paz"]=1956
init_graph["Los Reyes"]["Santa Marta"]=1783
init_graph["La Paz"]["Los Reyes"]=1956
init_graph["Ciudad Azteca"]["Plaza Aragon"]=574
init_graph["Plaza Aragon"]["Olimpica"]=709
init_graph["Plaza Aragon"]["Ciudad Azteca"]=574
init_graph["Olimpica"]["Ecatepec"]=596
init_graph["Olimpica"]["Plaza Aragon"]=709
init_graph["Ecatepec"]["Muzquiz"]=1485
init_graph["Ecatepec"]["Olimpica"]=596
init_graph["Muzquiz"]["Rio de los Remedios"]=1155
init_graph["Muzquiz"]["Ecatepec"]=1485
init_graph["Rio de los Remedios"]["Impulsora"]=436
init_graph["Rio de los Remedios"]["Muzquiz"]=1155
init_graph["Impulsora"]["Nezahualcoyotl"]=1393
init_graph["Impulsora"]["Rio de los Remedios"]=436
init_graph["Nezahualcoyotl"]["Villa de Aragon"]=1335
init_graph["Nezahualcoyotl"]["Impulsora"]=1393
init_graph["Villa de Aragon"]["Bosques de Aragon"]=784
init_graph["Villa de Aragon"]["Nezahualcoyotl"]=1335
init_graph["Bosques de Aragon"]["Deportivo Oceania"]=1165
init_graph["Bosques de Aragon"]["Villa de Aragon"]=784
init_graph["Deportivo Oceania"]["Oceania"]=863
init_graph["Deportivo Oceania"]["Bosques de Aragon"]=1165
init_graph["Romero Rubio"]["Ricardo Flores Magon"]=908
init_graph["Romero Rubio"]["Oceania"]=809
init_graph["Ricardo Flores Magon"]["San Lazaro"]=907
init_graph["Ricardo Flores Magon"]["Romero Rubio"]=908
init_graph["Tepito"]["Lagunilla"]=611
init_graph["Tepito"]["Morelos"]=498
init_graph["Lagunilla"]["Garibaldi"]=474
init_graph["Lagunilla"]["Tepito"]=611
init_graph["Buenavista"]["Guerrero"]=521
init_graph["Tlahuac"]["Tlaltenco"]=1298
init_graph["Tlaltenco"]["Zapotitlan"]=1115
init_graph["Tlaltenco"]["Tlahuac"]=1298
init_graph["Zapotitlan"]["Nopalera"]=1276
init_graph["Zapotitlan"]["Tlaltenco"]=1115
init_graph["Nopalera"]["Olivos"]=1360
init_graph["Nopalera"]["Zapotitlan"]=1276
init_graph["Olivos"]["Tezonco"]=490
init_graph["Olivos"]["Nopalera"]=1360
init_graph["Tezonco"]["Periferico Oriente"]=1545
init_graph["Tezonco"]["Olivos"]=490
init_graph["Periferico Oriente"]["Calle 11"]=1111
init_graph["Periferico Oriente"]["Tezonco"]=1545
init_graph["Calle 11"]["Lomas Estrella"]=906
init_graph["Calle 11"]["Periferico Oriente"]=1111
init_graph["Lomas Estrella"]["San Andres Tomatlan"]=1060
init_graph["Lomas Estrella"]["Calle 11"]=906
init_graph["San Andres Tomatlan"]["Culhuacan"]=990
init_graph["San Andres Tomatlan"]["Lomas Estrella"]=1060
init_graph["Culhuacan"]["Atlalilco"]=1671
init_graph["Culhuacan"]["San Andres Tomatlan"]=990
init_graph["Mexicaltzingo"]["Ermita"]=1805
init_graph["Mexicaltzingo"]["Atlalilco"]=1922
init_graph["Eje Central"]["Parque de los Venados"]=1280
init_graph["Eje Central"]["Ermita"]=895
init_graph["Parque de los Venados"]["Zapata"]=563
init_graph["Parque de los Venados"]["Eje Central"]=1280
init_graph["Zapata"]["Hospital 20 de Noviembre"]=450
init_graph["Zapata"]["Parque de los Venados"]=563
init_graph["Zapata"]["Coyoacan"]=1153
init_graph["Zapata"]["Division del Norte"]=794
init_graph["Hospital 20 de Noviembre"]["Insurgentes Sur"]=725
init_graph["Hospital 20 de Noviembre"]["Zapata"]=450
init_graph["Insurgentes Sur"]["Mixcoac"]=651
init_graph["Insurgentes Sur"]["Hospital 20 de Noviembre"]=725

graph = Graph(nodes, init_graph)

nodo_inicio = input("Cual es la estacion de inicio?: ")
nodo_destino = input("Cual es la estacion final?: ")

previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=nodo_inicio)

print_result(previous_nodes, shortest_path, start_node=nodo_inicio, target_node=nodo_destino)


G = nx.DiGraph()
for origen_nombre , destino in init_graph.items():
    for destino_nombre, w in destino.items():
        G.add_edge(origen_nombre, destino_nombre, weight=w)


pos = nx.layout.kamada_kawai_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Estaciones del metro de la CDMX")
plt.show()

