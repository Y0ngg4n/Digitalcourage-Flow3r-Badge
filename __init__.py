import st3m.run, random

from st3m.application import Application, ApplicationContext
from st3m.input import InputState
from ctx import Context

import leds
import audio


class Digitalcourage(Application):
    def __init__(self, app_ctx: ApplicationContext) -> None:
        super().__init__(app_ctx)
        self.LEDS = [[255, 255, 255] for i in range(40)]

    def draw(self, ctx: Context) -> None:
        ctx.image_smoothing = False
        ctx.rectangle(-120, -120, 240, 240)
        ctx.rgb(1, 1, 1)
        ctx.fill()
        leds.set_all_rgb(255, 204, 0)
        ctx.image(
            "/flash/sys/apps/digitalcourage/Digitalcourage.png",
            -120, -21, 240, 42
        )
        leds.update()