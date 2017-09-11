from project.models import GlobalValue


def course_search(request, course_list):
    year = ''
    if 'search_year' in request.POST:
        year = request.POST['search_year'][:4]
        if year == u'所有':
            pass
        elif year != u'所有':
            course_list = course_list.filter(year=year)
    else:
        year = GlobalValue.objects.get(key='current_year').value
        course_list = course_list.filter(year=year)

    semester = ''
    if 'search_semester' in request.POST:
        semester = request.POST['search_semester']
        if semester == u'所有':
            pass
        elif semester == u'第一学期':
            course_list = course_list.filter(semester=1)
        elif semester == u'第二学期':
            course_list = course_list.filter(semester=2)
    else:
        current_semester = GlobalValue.objects.get(key='current_semester').value
        course_list = course_list.filter(semester=current_semester)
        if current_semester in [1, '1']:
            semester = u'第一学期'
        if current_semester in [2, '2']:
            semester = u'第二学期'

    return course_list, year, semester
