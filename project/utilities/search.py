from project.models import GlobalValue

# TODO: 可简化 合并
# main.html 全局表单增加serach_year, seach_semester, search_audit_status, search_type


def search_course(request, cource_list):
    year = ''
    if 'location_year_post' in request.POST:
        year = request.POST['location_year_post']
        if year == u'所有':
            pass
        else:
            cource_list = cource_list.filter(year=year)
    elif 'search_year' in request.POST:
        year = request.POST['search_year'][:4]
        if year == u'所有':
            pass
        else:
            cource_list = cource_list.filter(year=year)
    elif 'extra_data' in request.POST and request.POST['extra_data'] != '':
        year = request.POST['extra_data'].split(',')[0]
        if year == u'所有':
            pass
        else:
            cource_list = cource_list.filter(year=year)
    else:
        year = GlobalValue.objects.get(key='current_year').value
        cource_list = cource_list.filter(year=year)

    semester = ''
    if 'location_semester_post' in request.POST:
        semester = request.POST['location_semester_post']
        if semester == u'所有':
            pass
        elif semester == u'第一学期':
            cource_list = cource_list.filter(semester=1)
        elif semester == u'第二学期':
            cource_list = cource_list.filter(semester=2)
    elif 'search_semester' in request.POST:
        semester = request.POST['search_semester']
        if semester == u'所有':
            pass
        elif semester == u'第一学期':
            cource_list = cource_list.filter(semester=1)
        elif semester == u'第二学期':
            cource_list = cource_list.filter(semester=2)
    elif 'extra_data' in request.POST and request.POST['extra_data'] != '':
        semester = request.POST['extra_data'].split(',')[1]
        if semester == u'所有':
            pass
        elif semester == u'第一学期':
            cource_list = cource_list.filter(semester=1)
        elif semester == u'第二学期':
            cource_list = cource_list.filter(semester=2)
    else:
        current_semester = GlobalValue.objects.get(key='current_semester').value
        cource_list = cource_list.filter(semester=current_semester)
        if current_semester in [1, '1']:
            semester = u'第一学期'
        if current_semester in [2, '2']:
            semester = u'第二学期'

    return cource_list, year, semester


def search_project(request, project_list):
    year = ''
    if 'location_year_post' in request.POST:
        year = request.POST['location_year_post']
        if year == u'所有':
            pass
        else:
            project_list = project_list.filter(year=year)
    elif 'search_year' in request.POST:
        year = request.POST['search_year'][:4]
        if year == u'所有':
            pass
        else:
            project_list = project_list.filter(year=year)
    elif 'extra_data' in request.POST and request.POST['extra_data'] != '':
        year = request.POST['extra_data']
        if year == u'所有':
            pass
        else:
            project_list = project_list.filter(year=year)
    else:
        year = GlobalValue.objects.get(key='current_year').value
        project_list = project_list.filter(year=year)

    return project_list, year


def search_course_audit(request, cource_list):
    year = ''
    if 'location_year_post' in request.POST:
        year = request.POST['location_year_post']
        if year == u'所有':
            pass
        elif year != u'所有':
            cource_list = cource_list.filter(year=year)
    elif 'search_year' in request.POST:
        year = request.POST['search_year'][:4]
        if year == u'所有':
            pass
        elif year != u'所有':
            cource_list = cource_list.filter(year=year)
    elif 'extra_data' in request.POST and request.POST['extra_data'] != '':
        year = request.POST['extra_data'].split(',')[0]
        if year == u'所有':
            pass
        else:
            cource_list = cource_list.filter(year=year)
    else:
        year = GlobalValue.objects.get(key='current_year').value
        cource_list = cource_list.filter(year=year)

    semester = ''
    if 'location_semester_post' in request.POST:
        semester = request.POST['location_semester_post']
        if semester == u'所有':
            pass
        elif semester == u'第一学期':
            cource_list = cource_list.filter(semester=1)
        elif semester == u'第二学期':
            cource_list = cource_list.filter(semester=2)
    elif 'search_semester' in request.POST:
        semester = request.POST['search_semester']
        if semester == u'所有':
            pass
        elif semester == u'第一学期':
            cource_list = cource_list.filter(semester=1)
        elif semester == u'第二学期':
            cource_list = cource_list.filter(semester=2)
    elif 'extra_data' in request.POST and request.POST['extra_data'] != '':
        semester = request.POST['extra_data'].split(',')[1]
        if semester == u'所有':
            pass
        elif semester == u'第一学期':
            cource_list = cource_list.filter(semester=1)
        elif semester == u'第二学期':
            cource_list = cource_list.filter(semester=2)
    else:
        current_semester = GlobalValue.objects.get(key='current_semester').value
        cource_list = cource_list.filter(semester=current_semester)
        if current_semester in [1, '1']:
            semester = u'第一学期'
        if current_semester in [2, '2']:
            semester = u'第二学期'

    audit_status = ''
    if 'location_audit_status_post' in request.POST:
        audit_status = request.POST['location_audit_status_post']
        if audit_status == u'所有':
            pass
        elif audit_status == u'审核未通过':
            cource_list = cource_list.filter(audit_status=1)
        elif audit_status == u'未审核':
            cource_list = cource_list.filter(audit_status=2)
        elif audit_status == u'已审核':
            cource_list = cource_list.filter(audit_status=3)
    elif 'audit_status' in request.POST:
        audit_status = request.POST['audit_status']
        if audit_status == u'所有':
            pass
        elif audit_status == u'审核未通过':
            cource_list = cource_list.filter(audit_status=1)
        elif audit_status == u'未审核':
            cource_list = cource_list.filter(audit_status=2)
        elif audit_status == u'已审核':
            cource_list = cource_list.filter(audit_status=3)
    elif 'extra_data' in request.POST and request.POST['extra_data'] != '':
        audit_status = request.POST['extra_data'].split(',')[2]
        if audit_status == u'所有':
            pass
        elif audit_status == u'审核未通过':
            cource_list = cource_list.filter(audit_status=1)
        elif audit_status == u'未审核':
            cource_list = cource_list.filter(audit_status=2)
        elif audit_status == u'已审核':
            cource_list = cource_list.filter(audit_status=3)
    else:
        audit_status = u'所有'

    return cource_list, year, semester, audit_status


def search_project_audit(request, project_list):
    year = ''
    if 'location_year_post' in request.POST:
        year = request.POST['location_year_post']
        if year == u'所有':
            pass
        elif year != u'所有':
            project_list = project_list.filter(year=year)
    elif 'search_year' in request.POST:
        year = request.POST['search_year'][:4]
        if year == u'所有':
            pass
        elif year != u'所有':
            project_list = project_list.filter(year=year)
    elif 'extra_data' in request.POST and request.POST['extra_data'] != '':
        year = request.POST['extra_data'].split(',')[0]
        if year == u'所有':
            pass
        else:
            project_list = project_list.filter(year=year)
    else:
        year = GlobalValue.objects.get(key='current_year').value
        project_list = project_list.filter(year=year)

    audit_status = ''
    if 'location_audit_status_post' in request.POST:
        audit_status = request.POST['location_audit_status_post']
        if audit_status == u'所有':
            pass
        elif audit_status == u'审核未通过':
            project_list = project_list.filter(audit_status=1)
        elif audit_status == u'未审核':
            project_list = project_list.filter(audit_status=2)
        elif audit_status == u'已审核':
            project_list = project_list.filter(audit_status=3)
    elif 'audit_status' in request.POST:
        audit_status = request.POST['audit_status']
        if audit_status == u'所有':
            pass
        elif audit_status == u'审核未通过':
            project_list = project_list.filter(audit_status=1)
        elif audit_status == u'未审核':
            project_list = project_list.filter(audit_status=2)
        elif audit_status == u'已审核':
            project_list = project_list.filter(audit_status=3)
    elif 'extra_data' in request.POST and request.POST['extra_data'] != '':
        audit_status = request.POST['extra_data'].split(',')[1]
        if audit_status == u'所有':
            pass
        elif audit_status == u'审核未通过':
            project_list = project_list.filter(audit_status=1)
        elif audit_status == u'未审核':
            project_list = project_list.filter(audit_status=2)
        elif audit_status == u'已审核':
            project_list = project_list.filter(audit_status=3)
    else:
        audit_status = u'所有'

    return project_list, year, audit_status
