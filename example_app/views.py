from django.shortcuts import redirect, render

from example_app.cat import cat


def example_2(request):
    return render(request, template_name='example.html', context={'cat': cat})


def example(request):
    cat["name"] = request.GET.get('name', 'John')
    return redirect("example_2")
