#NOTE: Test stuff here.


from classes.animations.animation import Animation
from classes.animations.easing import ease_in

animation = Animation(
    start_val=0,
    end_val=100,
    duration=4,
    easing_function=ease_in
)

current_value = animation.update(1)

print("Current value:", current_value)
print("Animation finished:", animation.finished_status)
