"""
CPU profiling using line_profiler

To run:

kernprof -l preprocess_cpu.py

Inspect results:

python -m line_profiler preprocess_cpu.py.lprof

More info:

https://github.com/rkern/line_profiler
"""
import logging
from datetime import datetime
from yass import preprocess
import settings

if __name__ == '__main__':
    """Profiling memory in YASS pipeline
    """
    settings.run()
    start = datetime.now()
    logger = logging.getLogger(__name__)

    logger.info('Preprocessing started at second: %.2f',
                (datetime.now() - start).total_seconds())

    # preprocessing
    (standarized_path, standarized_params, channel_index,
     whiten_filter) = profile(preprocess.run)(output_directory='profiling',
                                              if_file_exists='overwrite')

    logger.info('Preprocessing finished at second: %.2f',
                (datetime.now() - start).total_seconds())
