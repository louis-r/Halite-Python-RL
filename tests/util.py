import json
import urllib.request
import numpy as np


def game_states_from_url(GAME_URL):
    """
    We host known games on aws server and we run the tests according to these games, from which we know the output
    :param GAME_URL: The url of the game on the server (string).
    :return:
    """
    game = json.loads(urllib.request.urlopen(GAME_URL).readline().decode("utf-8"))

    owner_frames = np.array(game["frames"])[:, :, :, 0][:, np.newaxis, :, :]
    strength_frames = np.array(game["frames"])[:, :, :, 1][:, np.newaxis, :, :]
    production_frames = np.repeat(np.array(game["productions"])[np.newaxis, np.newaxis, :, :], len(owner_frames),
                                  axis=0)
    moves = np.array(game['moves'])

    game_states = np.concatenate(([owner_frames, strength_frames, production_frames]), axis=1)
    return game_states / np.array([1, 255, 10])[:, np.newaxis, np.newaxis], moves
