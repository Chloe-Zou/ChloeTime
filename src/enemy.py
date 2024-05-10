import pygame

class character:
  def __init__(self, stage, speed, power, health, stamina):
    self.stage = stage
    self.speed = speed
    self.power = power
    self.health = health
    self.stamina = stamina

  def enemyStrength(self, stage):
    return stage
  def speciality(self, power):
    if power == True:
      print("POWER CHARGED")
      return False
  def cook(self, stamina, health):
    return health, stamina
