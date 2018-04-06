from pathlib import Path
import logging
from datetime import datetime
import yass
from yass import deconvolute
import settings


if __name__ == '__main__':
    settings.run()
    start = datetime.now()
    logger = logging.getLogger(__name__)

    CONFIG = yass.read_config()

    logger.info('Deconvolution started at second: %.2f',
                (datetime.now() - start).total_seconds())

    DIRECTORY = Path(CONFIG.data.root_folder, 'profiling')

    spike_index_all = str(DIRECTORY / 'spike_index_all.npy')
    templates = str(DIRECTORY / 'templates.npy')

    profile(deconvolute.run)(spike_index_all, templates,
                             output_directory='profiling')

    logger.info('Deconvolution finished at second: %.2f',
                (datetime.now() - start).total_seconds())
