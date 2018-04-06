from pathlib import Path
import logging
from datetime import datetime
from memory_profiler import profile
import yass
from yass import templates
import settings


if __name__ == '__main__':
    settings.run()
    start = datetime.now()
    logger = logging.getLogger(__name__)

    CONFIG = yass.read_config()

    logger.info('Templates started at second: %.2f',
                (datetime.now() - start).total_seconds())

    DIRECTORY = Path(CONFIG.data.root_folder, 'profiling')

    spike_train_cluster = str(DIRECTORY / 'spike_train_cluster.npy')

    profile(templates.run.__wrapped__)(spike_train_cluster,
                                       output_directory='profiling',
                                       if_file_exists='overwrite',
                                       save_results=True)

    logger.info('Templates finished at second: %.2f',
                (datetime.now() - start).total_seconds())
