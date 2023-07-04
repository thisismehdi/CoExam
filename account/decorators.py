# this decorator for the unauthenticated users
def isNot_authenticated(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return func(request, *args, **kwargs)
    return wrapper
# this decorator for is Teachers
def is_teacher(func):
    def wrapper(request,*args,**kwargs):
        if TeacherProfile.objects.filter(user=request.user).exists():
            return func(request,*args,**kwargs)
        return redirect('home')
    return wrapper
# this decorator for is Students
def is_student(func):
    def wrapper(request,*args,**kwargs):
        if StudentProfile.objects.filter(user=request.user).exists():
            return func(request,*args,**kwargs)
        return redirect('home')
    return wrapper