game_level = 10
enemies = ['skeleton','zombie','alien']
def cr_en():
    new_enemy = "l"
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)


my_global_var = 1


def my_function():
    # Only accessible within my_function()
    my_local_var = 2


for _ in range(10):
    # Accessible anywhere
    my_block_var = 3
    print(my_block_var)