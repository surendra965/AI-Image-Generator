
from django.shortcuts import render
from .forms import ImagePromptForm
from .utils import build_pollinations_url

def home(request):
    image_url = None
    if request.method == "POST":
        form = ImagePromptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data["prompt"]
            size = form.cleaned_data.get("size", "512")
            image_url = build_pollinations_url(prompt, size)
    else:
        form = ImagePromptForm()

    return render(request, "home.html", {"form": form, "image_url": image_url})
