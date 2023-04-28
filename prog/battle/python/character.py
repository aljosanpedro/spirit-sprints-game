class Character:
    # Attributes
    ACTION_TO_ANIM = {
            "attack" : "attack",
            "counter": "counter",
            "stand"  : "casting",
            "time"   : "hurt",
        }
    damage_health = 0
    
    
    # Methods
    def __init__(self, name, health, anim):
        self.name = name
        self.health = health
        self.anim = anim
        
        Character.status(self)
    
    
    def status(self):
        print(f"{self.name.upper()} [Health: {self.health}] [Animation: {self.anim.title()}]\n")
    
    
    def set_anim(self, anim):
        self.anim = anim
        
        Character.status(self)
        
    @staticmethod        
    def set_anim_both(anim, *characters):
        player, enemy = characters
        
        player.set_anim(anim)
        enemy.set_anim(anim)
             

    def damage(self, time_ratio):
        # recall: time is a ratio of time-left/total-time
        # 1.x multiplier
        
        time_factor = 1 + time_ratio
        print(f"TIME FACTOR: {time_factor}\n")
        
        total_damage = Character.damage_health * time_factor
        
        self.health -= total_damage
        self.health = int(self.health)
        
        # clamp health to 0 in case visual health bar is affected by negatives
        if self.health <= 0:
            self.health = 0

    
    @classmethod
    def apply_results(cls, action, result, time, *characters):
        player, enemy = characters
        
        # used dict here bc uniform dict -> general code
        player.anim = cls.ACTION_TO_ANIM[action]
        
        # used match case bc "lose" has 2 outcome AND health involved
        match result:
            case "win":
                player.status()
                
                enemy.damage(time)
                enemy.set_anim("hurt")
            case "lose":
                player.damage(time)
                player.set_anim("hurt")
                
                enemy.set_anim("attack")
            case "stale":
                player.status()
                enemy.status()
