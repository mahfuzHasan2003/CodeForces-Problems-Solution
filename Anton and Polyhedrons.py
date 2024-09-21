polyhedrons_have = []
n = int(input())
for i in range(n) :
    polyhedrons_have.append(input())
print((polyhedrons_have.count("Tetrahedron")*4) + (polyhedrons_have.count("Cube")*6) + (polyhedrons_have.count("Octahedron")*8) + (polyhedrons_have.count("Dodecahedron")*12) + (polyhedrons_have.count("Icosahedron")*20))