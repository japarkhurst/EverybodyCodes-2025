input = '''Plant 1 with thickness 1:
- free branch with thickness 1

Plant 2 with thickness 1:
- free branch with thickness 1

Plant 3 with thickness 1:
- free branch with thickness 1

Plant 4 with thickness 17:
- branch to Plant 1 with thickness 15
- branch to Plant 2 with thickness 3

Plant 5 with thickness 24:
- branch to Plant 2 with thickness 11
- branch to Plant 3 with thickness 13

Plant 6 with thickness 15:
- branch to Plant 3 with thickness 14

Plant 7 with thickness 10:
- branch to Plant 4 with thickness 15
- branch to Plant 5 with thickness 21
- branch to Plant 6 with thickness 34'''

from dataclasses import dataclass

@dataclass
class Branch():
    source: int
    to: int
    thickness: int
    
@dataclass
class Plant():
    id: int
    thickness: int
    brightness: int = 0
    branches: list


for row in input.split('\n'):
    if not row:
        continue
    if row.startswith('Plant'):
        
