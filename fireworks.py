"""Some functions to animate setting off firweorks with Sculptor class."""
import shapes


class Firework(shapes.Sculptor):
    def __init__(self, moving_turtle, animation_turtle, base_ycor, background_color):
        super().__init__(moving_turtle)
        self.screen.tracer(False)
        self.pen.up()  # should stay up, because it only leads path
        self.bg_color = background_color
        self.explosion_animation_frequency = 3
        # lift off physics properties
        self.height = None  # set at start
        self.base_xcor = None  # set at start
        self.base_ycor = base_ycor
        self.pen.speed(0)
        self.starting_lift_off_radius = 60
        self.lift_off_radius = 40
        self.lift_off_curvature = None
        self.lift_off_extent_unit = 8
        self.lift_off_animation_step = 8
        # lift off animation properties
        self.animation_pen = animation_turtle
        self.animation_pen.speed(0)
        self.animation_shaper = shapes.Sculptor(self.animation_pen)
        self.animation_pen.pensize(2)
        self.lift_off_particle_size = 8

    def start(self, base_xcor, height, size, color, angle, curvature_angle, shape):
        """Start the process of firing off firework: lift firework off and make it explode"""
        self.base_xcor = base_xcor
        self.height = height
        self.lift_off_curvature = curvature_angle
        self.animation_pen.pensize(1)
        self.lift_off(shape, color)
        self.animation_pen.pensize(2)
        self.explode(shape, self.explosion_animation_frequency, size, color, angle)

    def lift_off(self, shape_function, color):
        """Move firework upwards on curved line, also rotate the firework while lifting it up"""
        self.pen.flyto(self.base_xcor, self.base_ycor)
        # set firework to vertical position
        self.pen.seth(0)
        self.pen.lt((180-self.lift_off_curvature)//2)
        current_extent = 0
        while self.pen.ycor() <= self.height:
            # move a unit upward
            self.pen.circle(self.lift_off_radius, self.lift_off_extent_unit)
            # start animation at each animation step
            if not current_extent % self.lift_off_animation_step:
                self.lift_off_animation(shape_function, color)
            # change direction if reached predefined point of circle segment (lift_off_extent)
            if current_extent >= self.lift_off_curvature:
                self.lift_off_radius = -self.lift_off_radius
                current_extent = 0
            else:
                current_extent += self.lift_off_extent_unit

    def lift_off_animation(self, shape_function, color):
        """Rotate firework around itself."""
        create_shape = shape_function
        self.animation_pen.flyto(self.pen.xcor(), self.pen.ycor())
        self.animation_pen.rt(4)
        create_shape(self.lift_off_particle_size, color, fill=True)
        self.screen.update()
        create_shape(self.lift_off_particle_size, self.bg_color, fill=True)

    def explode(self, shape_function, frequency, size, color, angle):
        """Do animation of firework explosion.
        While swelling the shape of firework is filled with color,
        in the end it has color inside."""
        create_shape = shape_function
        self.animation_pen.seth(angle)
        for current_size in range(1, size, frequency):
            create_shape(current_size, color, fill=True)
            self.screen.update()
            create_shape(current_size, self.bg_color, fill=True)
        create_shape(size, color, fill=False)
        self.screen.update()
