import pygal.maps.world as module
import population_dic


country_code_dic = module.COUNTRIES

refined_population_dic = {}
for x, y in country_code_dic.items():
    for key, value in population_dic.get_dic().items():
        if key == y:
            refined_population_dic[x] = value

def get_refined_dic():
    return refined_population_dic

