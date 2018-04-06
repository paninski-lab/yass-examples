import logging
from datetime import datetime
from memory_profiler import profile
from yass import preprocess
import settings


if __name__ == '__main__':
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
