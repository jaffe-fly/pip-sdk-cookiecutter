import pytest
from logzero import logger


class TestSample:

    def test_sample(self):
        assert True

    @pytest.mark.run(order=2)
    def test_one(self):
        logger.info('======1======')
        assert True

    @pytest.mark.run(order=1)
    def test_two(self):
        logger.info('======2======')
        assert True
