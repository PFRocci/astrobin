# Django
from django.conf.urls import patterns, url

# This app
from astrobin_apps_iotd.views import *


urlpatterns = patterns('',
    # Submissions
    url(
        r'^toggle-submission-ajax/(?P<pk>\d+)/$',
        IotdToggleSubmissionAjaxView.as_view(),
        name = 'iotd_toggle_submission_ajax'),
    url(
        r'^submission-queue/$',
        IotdSubmissionQueueView.as_view(),
        name = 'iotd_submission_queue'),

    # Votes
    url(
        r'^toggle-vote-ajax/(?P<pk>\d+)/$',
        IotdToggleVoteAjaxView.as_view(),
        name = 'iotd_toggle_vote_ajax'),
    url(
        r'^review-queue/$',
        IotdReviewQueueView.as_view(),
        name = 'iotd_review_queue'),

    # Judgements
    url(
        r'^toggle-iotd-judgement-ajax/(?P<pk>\d+)/$',
        IotdToggleJudgementAjaxView.as_view(),
        name = 'iotd_toggle_judgement_ajax'),
    url(
        r'^judgement-queue/$',
        IotdJudgementQueueView.as_view(),
        name = 'iotd_judgement_queue'),

    # Archive
    url(
        r'^archive/$',
        IotdArchiveView.as_view(),
        name = 'iotd_archive'),

    # Utils
    url(
        r'^submitters-for-image-ajax/(?P<pk>\d+)/$',
        IotdSubmittersForImageAjaxView.as_view(),
        name = 'iotd_submitters_for_image'),
    url(
        r'^reviewers-for-image-ajax/(?P<pk>\d+)/$',
        IotdReviewersForImageAjaxView.as_view(),
        name = 'iotd_reviewers_for_image'),
)
