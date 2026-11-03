class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # I will use simply sorted(str) == sorted(str)
        palabras = {}
        sublista = []
        sublistas = []
        for i in range(len(strs)):
            valor = "".join(sorted(strs[i]))
            if valor not in palabras.keys():
                palabras[valor] = [strs[i]]
            else:
                palabras[valor].append(strs[i])
            
        return list(palabras.values())