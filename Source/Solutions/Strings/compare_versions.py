def compare_version(v1: str, v2: str):
    arr_v1 = v1.split('.')
    arr_v2 = v2.split('.')
    
    n = len(arr_v1)
    m = len(arr_v2)
    
    for i in range(max(n, m)):
        version1 = int(arr_v1[i]) if i < n else 0
        version2 = int(arr_v2[i]) if i < m else 0
        if version1 > version2:
            return 1
        elif version1 < version2:
            return -1
    
    return 0

print(f"Expected: 1, Computed result: ", compare_version("2.0.0", "1.0"))
print(f"Expected: 1, Computed result: ", compare_version("1.3.2.1", "1.3.2"))
print(f"Expected: -1, Computed result: ", compare_version("1.0", "2.0"))
print(f"Expected: -1, Computed result: ", compare_version("1.2.3.1", "1.2.3.4"))
print(f"Expected: 0, Computed result: ", compare_version("1.0", "1.0.0"))