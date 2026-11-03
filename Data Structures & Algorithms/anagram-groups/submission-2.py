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
            
        for key in palabras.keys():
            sublista = []
            for value in palabras[key]:
                sublista.append(value)
            sublistas.append(sublista)

        return sublistas