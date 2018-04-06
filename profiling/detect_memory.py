"""
Memory profiling (line by line) for the detection step

See this for usage:

https://github.com/pythonprofilers/memory_profiler

Run with:

mprof run detect_memory.py PATH_TO_CONFIG_FILE

Plot results:

mprof plot
"""
from pathlib import Path
import logging
from datetime import datetime
from memory_profiler import profile
import yass
from yass import detect
import settings


if __name__ == '__main__':
    """Profiling memory in YASS pipeline
    """
    settings.run()
    start = datetime.now()
    logger = logging.getLogger(__name__)

    CONFIG = yass.read_config()

    logger.info('Detection started at second: %.2f',
                (datetime.now() - start).total_seconds())

    DIRECTORY = Path(CONFIG.data.root_folder, 'profiling')

    standarized_path = str(DIRECTORY / 'standarized.bin')
    standarized_params = str(DIRECTORY / 'standarized.yaml')
    channel_index = str(DIRECTORY / 'channel_index.npy')
    whiten_filter = str(DIRECTORY / 'whitening.npy')

    # detection
    profile(detect.run)(standarized_path,
                        standarized_params,
                        channel_index,
                        whiten_filter,
                        output_directory='profiling',
                        if_file_exists='overwrite',
                        save_results=True)

    logger.info('Detection finished at second: %.2f',
                (datetime.now() - start).total_seconds())
