from project.models import GlobalValue


def search(request, source_list):

    year = ''
    if 'search_year' in request.POST:
        year = request.POST['search_year'][:4]
        if year == u'所有':
            pass
        elif year != u'所有':
            source_list = source_list.filter(year=year)
    else:
        year = GlobalValue.objects.get(key='current_year').value
        source_list = source_list.filter(year=year)

    semester = ''
    if 'search_semester' in request.POST:
        semester = request.POST['search_semester']
        if semester == u'所有':
            pass
        elif semester == u'第一学期':
            source_list = source_list.filter(semester=1)
        elif semester == u'第二学期':
            source_list = source_list.filter(semester=2)
    else:
        current_semester = GlobalValue.objects.get(key='current_semester').value
        source_list = source_list.filter(semester=current_semester)
        if current_semester in [1, '1']:
            semester = u'第一学期'
        if current_semester in [2, '2']:
            semester = u'第二学期'

    return source_list, year, semester


def audit_search(request, source_list):

    year = ''
    if 'search_year' in request.POST:
        year = request.POST['search_year'][:4]
        if year == u'所有':
            pass
        elif year != u'所有':
            source_list = source_list.filter(year=year)
    else:
        year = GlobalValue.objects.get(key='current_year').value
        source_list = source_list.filter(year=year)

    semester = ''
    if 'search_semester' in request.POST:
        semester = request.POST['search_semester']
        if semester == u'所有':
            pass
        elif semester == u'第一学期':
            source_list = source_list.filter(semester=1)
        elif semester == u'第二学期':
            source_list = source_list.filter(semester=2)
    else:
        current_semester = GlobalValue.objects.get(key='current_semester').value
        source_list = source_list.filter(semester=current_semester)
        if current_semester in [1, '1']:
            semester = u'第一学期'
        if current_semester in [2, '2']:
            semester = u'第二学期'

    audit_status = ''
    if 'audit_status' in request.POST:
        audit_status = request.POST['audit_status']
        if audit_status == u'所有':
            pass
        if audit_status == u'未审核':
            source_list = source_list.filter(audit_status=0)
        if audit_status == u'审核未通过':
            source_list = source_list.filter(audit_status=1)
        if audit_status == u'已审核':
            source_list = source_list.filter(audit_status=2)
    else:
        audit_status = u'所有'

    return source_list, year, semester, audit_status
