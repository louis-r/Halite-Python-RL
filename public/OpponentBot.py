import sys

mode = 'server' if (len(sys.argv) == 1) else 'local'
mode = 'local'  # TODO remove forcing

if mode == 'server':  # 'server' mode
    import hlt
else:  # 'local' mode
    import context

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    hlt = context.HLT(port=port)

from public.models.bot.improvedBot import ImprovedBot

bot = ImprovedBot()

while True:
    myID, game_map = hlt.get_init()
    hlt.send_init("OpponentBot")
    bot.setID(myID)

    while (mode == 'server' or hlt.get_string() == 'Get map and play!'):
        game_map.get_frame(hlt.get_string())
        moves = bot.compute_moves(game_map)
        hlt.send_frame(moves)
