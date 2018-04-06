"""
Memory profiling (line by line) for the templates step

See this for usage:

https://github.com/pythonprofilers/memory_profiler

Run with:

mprof run cluster_templates.py PATH_TO_CONFIG_FILE

Plot results:

mprof plot
"""
from pathlib import Path
import logging
from datetime import datetime
from memory_profiler import profile
import yass
from yass import templates
import settings


if __name__ == '__main__':
    """Profiling memory in YASS pipeline
    """
    settings.run()
    start = datetime.now()
    logger = logging.getLogger(__name__)

    CONFIG = yass.read_config()

    logger.info('Templates started at second: %.2f',
                (datetime.now() - start).total_seconds())

    DIRECTORY = Path(CONFIG.data.root_folder, 'profiling')

    spike_train_cluster = str(DIRECTORY / 'spike_train_cluster.npy')

    # detection
    profile(templates.run)(spike_train_cluster,
                           output_directory='profiling',
                           if_file_exists='overwrite',
                           save_results=True)

    logger.info('Templates finished at second: %.2f',
                (datetime.now() - start).total_seconds())
