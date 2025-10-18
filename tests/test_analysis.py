import pytest

from analysis import comments_analysis


def test_comments_analysis():
    # Using a sample video ID for testing
    video_id = '-H9Cfk-3f8Y'

    result = comments_analysis(video_id)

    assert isinstance(result, list)
    assert 'label' in result[0]
    assert 'score' in result[0]