import places

stash = []

class Map(object):
    places = {
        'nest': places.Nest(),
        'front_yard': places.FrontYard(),
        'tree_1': places.Tree1(),
        'front_porch': places.FrontPorch(),
        'flower_bed': places.FlowerBed(),
        'back_yard': places.BackYard(),
        'tree_2': places.Tree2(),
        'tree_3': places.Tree3(),
        'patio': places.Patio(),
        'vegetable_garden': places.VegetableGarden(),
        'finished': places.Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.places.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self, stash):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        #self.stash = stash

        while current_scene != last_scene:
                next_scene_name = current_scene.enter(stash)
                current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter(stash)

a_map = Map('nest')
a_game = Engine(a_map)
a_game.play(stash)