import random, colorsys

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def get_colors(request):
    if(request.method=='POST'):
        colors = []
        for i in range(5):
            # Generate random rgb color
            rgb_color = rgb_random_color()

            # Convert RGB to HSL if it's true
            if random.choice((True, False)):
                hsl_color = colorsys.rgb_to_hls(rgb_color[0], rgb_color[1], rgb_color[2])
                colors.append({
                    "type": 'hsl',
                    "red": hsl_color[0],
                    "green": hsl_color[1],
                    "blue": hsl_color[2]
                })
            else:
                colors.append({
                    "type": "rgb",
                    "hue": rgb_color[0],
                    "saturation": rgb_color[1],
                    "lightness": rgb_color[2]
                })
            colors.append(rgb_random_color())
        return JsonResponse(colors, safe=False)

def rgb_random_color():
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    return color