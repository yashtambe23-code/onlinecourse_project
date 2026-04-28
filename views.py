from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Enrollment, Submission, Choice

def submit(request, course_id):

    course = get_object_or_404(Course, pk=course_id)

    enrollment = Enrollment.objects.first()

    selected_choices = request.POST.getlist('choice')

    submission = Submission.objects.create(
        enrollment=enrollment
    )

    for choice_id in selected_choices:
        choice = Choice.objects.get(id=choice_id)
        submission.choices.add(choice)

    return redirect('show_exam_result', course_id=course.id, submission_id=submission.id)


def show_exam_result(request, course_id, submission_id):

    course = get_object_or_404(Course, pk=course_id)

    submission = get_object_or_404(Submission, pk=submission_id)

    total_score = 0
    possible_score = 0

    for question in course.question_set.all():

        possible_score += 1

        selected_ids = []

        for choice in submission.choices.filter(question=question):
            selected_ids.append(choice.id)

        if question.is_get_score(selected_ids):
            total_score += 1

    context = {
        'course': course,
        'submission': submission,
        'total_score': total_score,
        'possible_score': possible_score
    }

    return render(request, 'exam_result_bootstrap.html', context)
