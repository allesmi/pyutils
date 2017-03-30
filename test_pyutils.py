import pytest
import pyutils

def test_get_pairs():
	# Empty list
	assert pyutils.get_pairs([]) == []

	# Happy cases
	assert pyutils.get_pairs([1, 2]) == [(1, 2)]
	assert pyutils.get_pairs([1, 2, 3, 4]) == [(1, 2), (3, 4)]

	# Input can't be evenly divided
	with pytest.raises(AssertionError):
		pyutils.get_pairs([1])

def test_get_triples():
	# Empty list
	assert pyutils.get_triples([]) == []

	# Happy cases
	assert pyutils.get_triples([1, 2, 3]) == [(1, 2, 3)]
	assert pyutils.get_triples([1, 2, 3, 4, 5, 6]) == [(1, 2, 3), (4, 5, 6)]

	# Input can't be evenly divided
	with pytest.raises(AssertionError):
		pyutils.get_triples([1])