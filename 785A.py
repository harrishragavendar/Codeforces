facemap = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}
n = int(input())
faces = 0
for _ in range(n):
    faces += facemap[input()]
print(faces)