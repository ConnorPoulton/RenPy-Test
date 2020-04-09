init python:
    class SwordMiniGame(renpy.Displayable):


        def __init__(self, child, child_x, child_y, click_accel, **kwargs):
            super(SwordMiniGame, self).__init__(**kwargs)
            self.child = renpy.displayable(child)
            self.width = config.screen_width
            self.height = config.screen_height
            self.child_x = child_x
            self.child_y = child_y
            self.child_y_resting = child_y
            self.time = 0
            self.time_limit = 100
            self.total_force = 0
            self.total_force_target = 80
            self.click_velocity = 40
            self.click_accel = click_accel
            self.velocity = 0
            self.gravity = -1
            self.gravity_accel = -0.5
            self.friction_accel = 0.2
            self.lastTime = None
            self.dTime = 0
            self.player_won = None


        def render(self, width, height, st, at):

            self.update(st, at)

            t = Transform(self.child, xpos = 0, ypos = 0)
            child_render = renpy.render(t, width, height, st, at)
            render = renpy.Render(self.width, self.height)
            render.blit(child_render, (self.child_x, self.child_y))
            renpy.redraw(self, 0)

            return render


        def event(self, ev, x, y, st):
            import pygame

            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                if self.velocity < self.click_velocity:
                    friction = (self.friction_accel * self.total_force)
                    print (friction)
                    self.velocity += ((self.click_accel  - friction) * self.dTime)

            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_k:
                self.player_won = False

            if self.player_won != None:
                return self.player_won

            return self.child.event(ev, x, y, st)


        def update(self, st, at):

            #update deltaTime
            if self.lastTime == None:
                self.lastTime = st
            self.dTime = st - self.lastTime
            self.lastTime = st
            #update total time passed
            self.time += self.dTime

            if self.velocity > self.gravity:
                self.velocity += (self.gravity_accel * self.dTime)

            if self.child_y < self.child_y_resting:
                self.child_y -= self.velocity
                self.total_force += self.velocity
            elif self.velocity > 0:
                self.child_y -= self.velocity
                self.total_force += self.velocity

            if self.total_force >= self.total_force_target:
                self.player_won = True
            elif self.time >= self.time_limit:
                self.player_won = False




        def visit(self):
            return [ self.child ]
