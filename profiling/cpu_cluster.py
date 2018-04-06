from pathlib import Path
import logging
from datetime import datetime
import yass
from yass import cluster
import settings


if __name__ == '__main__':
    settings.run()
    start = datetime.now()
    logger = logging.getLogger(__name__)

    CONFIG = yass.read_config()

    logger.info('Clustering started at second: %.2f',
                (datetime.now() - start).total_seconds())

    DIRECTORY = Path(CONFIG.data.root_folder, 'profiling')

    scores_clear = str(DIRECTORY / 'scores_clear.npy')
    spike_index_clear = str(DIRECTORY / 'spike_index_clear.npy')

    # detection
    profile(cluster.run)(scores_clear, spike_index_clear,
                         output_directory='profiling',
                         if_file_exists='overwrite',
                         save_results=True)

    logger.info('Clustering finished at second: %.2f',
                (datetime.now() - start).total_seconds())
