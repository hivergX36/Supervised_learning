import re 

class regression:
    
    def __init__(self):
        Labels = []
        Predictor = []
        covariance = 0 
        variance = 0 
        
        
    def checknumber(self,lignes,indice):
        ParsedList = []
        compteur1 = 0
        compteur2 = 0
        while(lignes[indice][compteur1] != "," and lignes[indice][compteur2] != ","):
              while(lignes[indice][compteur2] != ","):
                    compteur2 += 1
              print(lignes[indice][compteur1:compteur2])
              ParsedList.append(int(lignes[indice][compteur1:compteur2]))
              compteur1 = compteur2 + 1
              compteur2 = compteur1

   
              if compteur1 > len(lignes[indice]) - 1:
                    break
        return ParsedList
        
    def parse_data(self,text):
        fichier = open(text, "r",encoding="utf8")
        lines = fichier.readlines()
        lines = [lines[i] for i in range(len(lines)) if lines[i] != "\n"]
        lines = [ re.sub("\n", "", lines[i]) for i in range(len(lines))]
        print(lines)
        self.Labels = self.checknumber(lines,1)
        self.Predictor = self.checknumber(lines,3)
        
    def regression_coefficient(self):
        number_value = len(self.Labels)
        sum_y = sum(y for y in self.Labels)
        sum_x = sum(x for x in self.Predictor)
        mean_x = sum_x/number_value
        mean_y = sum_y/number_value
        sum_x_square = sum(x * x for x in self.Predictor)
        sum_xy = sum(x * y for x in self.Predictor for y in self.Labels)
        print("sum_y", sum_y)
        print("sum_x", sum_x)
        print("sum_x_square", sum_x_square)
        print("sum_xy", sum_xy)
        print("mean_x:", mean_x)
        print("mean_y", mean_y)
        self.covariance = (sum_xy - sum_x * sum_y) / 
        s

        