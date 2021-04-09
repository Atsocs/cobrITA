import random
from components.PowerUp import PowerUp


class PowerUpFactory:
    """
    Class to control the power-up creation
    """
    def __init__(self, items, item_limit=None):
        """
        :param items: dict that contains the possible power-ups with different powers and probabilities
        :param item_limit: max number of power-ups to be displayed at the same time on the map
        """
        self.dic = items
        if item_limit is None:
            item_limit = 3
        self.item_limit = item_limit
        self.collectable_powerups = []

    def maybe_create_powerup(self, prohibited=None):
        """
        Simplified creation method
        """
        if prohibited is None:
            prohibited = []
        if len(self.collectable_powerups) >= self.item_limit:
            return
        k = random.random()
        # may define here probabilities to each power-up
        if k > 0.7:
            # Accelerate effect
            self.collectable_powerups.append(PowerUp(self.dic['Accelerate']))
            self.collectable_powerups[-1].randomize_position(prohibited)
        elif k < 0.2:
            # Reverse effect
            self.collectable_powerups.append(PowerUp(self.dic['Reverse']))
            self.collectable_powerups[-1].randomize_position(prohibited)

    def get_positions(self):
        """
        Method to get collectable power-up positions
        :return: list with power-up coordinates
        """
        return [p.position for p in self.collectable_powerups]
