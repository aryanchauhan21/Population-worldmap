from pygal.maps.world import World
import refined_dic


usable_dic = refined_dic.get_refined_dic()
map = World()
map.title = 'Population distribution across countries of world'
map.add('Data for 2010', usable_dic)
map.render_to_file('map.svg')
