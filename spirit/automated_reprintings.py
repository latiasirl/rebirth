# tool by latiasirl to help with reprints. feel free to ignore

SET = "PZ6"

import os
path = f"C:/Users/maya/Projects/rebirth/spirit/assets/cards/{SET}"
file_list = os.listdir(path)
print(file_list)

# get every file name in \assets\cards\PZ6
# create a .py file with that name in a "test" subfolder of this
# write

for image in file_list:
  card_name_num = image[:-4]
  card_name = card_name_num.split("_")[0]
  card_num = card_name_num.split("_")[1]
  with open(f"game/scripts/cards/{SET}_test/{card_name_num}.py", "w") as new_py:
    template = f"""from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../FIRSTSET/{card_name}_FIRSTNUM.py"),
              collector_number={card_num}, rarity=Rarities.Rare,
              set_code="{SET}", key="{SET}",
              regulation_mark="MARKMARK")"""
    new_py.write(template)
