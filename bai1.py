dict = {"A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": ["E","H"],
        "E": [],
        "F": [],
        "G": [],
        "H": [],}
def xuat_duong_di(start, finish, father):
    print(father)
    duong_di = []
    dinh_hien_tai = finish
    while dinh_hien_tai != start:
        duong_di.append(dinh_hien_tai)
        dinh_hien_tai = father[dinh_hien_tai]
    duong_di.append(start)
    duong_di.reverse()
    print("Đường đi từ {} tới {}: {}".format(start, finish, duong_di))

def dfs(graph, start, finish):
    MO = []  # Tập hợp các đỉnh chưa được xét
    DONG = []  # Tập hợp các đỉnh đã được xét
    CHA = {}  # Tạo một từ điển để lưu cha của mỗi đỉnh
    MO.append(start)  # Thêm đỉnh bắt đầu vào tập MO
    while MO:
        n = MO.pop()  # Lấy một đỉnh từ tập MO
        if n in finish:  # Nếu đỉnh đó là đỉnh đích, trả về True
            print("Đường đi từ {} tới {} tồn tại.".format(start, n))
            xuat_duong_di(start, n, CHA)
            return True
        DONG.append(n)  # Thêm đỉnh n vào tập DONG
        for v in reversed(graph.get(n, [])):  # Duyệt qua các đỉnh kề của n
            if v not in DONG:  # Kiểm tra xem v đã được xét chưa
                MO.append(v)  # Thêm v vào tập MO
                if v not in CHA:
                 CHA[v] = n  # Gán n là cha của v
    return False  # Trả về False nếu không tìm thấy đường đi đến đỉnh đích

def bfs(graph, start, finish):
    MO = []
    DONG = []
    CHA = {}
    MO.append(start)
    while MO:
        n = MO.pop(0)
        if n in finish:
            print("Đường đi từ {} tới {} tồn tại.".format(start, n))
            xuat_duong_di(start, n, CHA)
            return True
        DONG.append(n)  # Thêm đỉnh n vào tập DONG
        for v in graph.get(n, []):  # Duyệt qua các đỉnh kề của n
            if v not in DONG:  # Kiểm tra xem v đã được xét chưa
                MO.append(v)  # Thêm v vào tập MO
                if v not in CHA:
                  CHA[v] = n  # Gán n là cha của v
    return False  # Trả về False nếu không tìm thấy đường đi đến đỉnh đích

start = "A"
finish = ["G", "H"]
print("Dùng BFS:")
if bfs(dict, start, finish) == False:
    print("Không tồn tại đường đi từ {} tới {}.".format(start, finish))