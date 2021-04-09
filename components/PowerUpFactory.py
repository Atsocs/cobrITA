import random
from components.PowerUp import PowerUp


class PowerUpFactory:
    """
    Class to control the power-up creation
    """
    def __init__(self, items):
        """
        :param items: dict that contains the possible power-ups with different powers and probabilities
        """
        self.dict = items
        self.collectable_powerups = []

    def maybe_create_powerup(self, snake_positions):
        """
        Simplified creation method
        """
        # max of three power-ups on the map
        if len(self.collectable_powerups) > 2:
            return
        k = random.random()
        if k > 0.5:
            self.collectable_powerups.append(PowerUp(0))  # 0: effect key
            end = len(self.collectable_powerups) - 1
            self.collectable_powerups[end].randomize_position(snake_positions)

    def get_positions(self):
        """
        Method to get collectable power-up positions
        :return: list with power-up coordinates
        """
        return [p.position for p in self.collectable_powerups]
