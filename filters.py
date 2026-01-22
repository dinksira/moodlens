from PIL import ImageEnhance, ImageFilter

def apply_mood_filter(image, mood, intensity):
    """
    image: PIL Image
    mood: str
    intensity: float (0.0 - 1.0)
    """

    img = image.copy()

    if mood == "happy":
        img = ImageEnhance.Brightness(img).enhance(1 + 0.3 * intensity)
        img = ImageEnhance.Color(img).enhance(1 + 0.5 * intensity)
        img = ImageEnhance.Contrast(img).enhance(1 + 0.2 * intensity)

    elif mood == "sad":
        img = ImageEnhance.Brightness(img).enhance(1 - 0.2 * intensity)
        img = ImageEnhance.Color(img).enhance(1 - 0.5 * intensity)
        img = ImageEnhance.Contrast(img).enhance(1 - 0.2 * intensity)
        img = img.filter(ImageFilter.GaussianBlur(radius=2 * intensity))

    elif mood == "angry":
        img = ImageEnhance.Contrast(img).enhance(1 + 0.6 * intensity)
        img = ImageEnhance.Color(img).enhance(1 + 0.4 * intensity)
        img = img.filter(ImageFilter.SHARPEN)

    elif mood == "calm":
        img = ImageEnhance.Brightness(img).enhance(1 + 0.1 * intensity)
        img = ImageEnhance.Color(img).enhance(1 - 0.2 * intensity)
        img = img.filter(ImageFilter.GaussianBlur(radius=1.5 * intensity))

    else:  # neutral
        img = ImageEnhance.Contrast(img).enhance(1 + 0.1 * intensity)

    return img
