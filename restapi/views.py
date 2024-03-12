import colorsys

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import secrets


@csrf_exempt
def get_colors(request):
    if(request.method=='POST'):
        colors = []
        for i in range(5):
            # Gernrate RGB if it's True
            if secrets.SystemRandom().choice((True, False)):
                rgb_color = rgb_random_color()
                colors.append({
                    "type": 'rgb',
                    "red": rgb_color[0],
                    "green": rgb_color[1],
                    "blue": rgb_color[2]
                })
            else:
                hsl_color = hsl_random_color()
                colors.append({
                    "type": "hsl",
                    "hue": hsl_color[0],
                    "saturation": hsl_color[1],
                    "lightness": hsl_color[2]
                })
        return JsonResponse(colors, safe=False)

def rgb_random_color():
    color = [secrets.SystemRandom().randint(0, 255), secrets.SystemRandom().randint(0, 255), secrets.SystemRandom().randint(0, 255)]
    return color

def hsl_random_color():
    color = [secrets.SystemRandom().randint(0, 360), secrets.SystemRandom().randint(0, 100), secrets.SystemRandom().randint(0, 100)]
    return color
